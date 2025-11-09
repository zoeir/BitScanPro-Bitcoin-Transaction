#!/usr/bin/env python3
# ===================================================
#  BitScanPro Bitcoin Transaction (Python 3 CLI Version)
# ===================================================

import sys
import os

# Check if dependencies are installed
try:
    from secp256k1 import *
    from sighash import *
except ImportError:
    print("ERROR: Required modules not found!")
    print("Please install dependencies:")
    print("  pip install pycryptodome")
    print("\nAnd clone the repository:")
    print("  git clone https://github.com/zoeir/Bitcoin-Message-Transaction.git")
    print("  cd Broadcast-Bitcoin-Transaction")
    print("  python3 main.py")
    sys.exit(1)


# ---------- Functions ----------
def create_op_return_script(message):
    """Create OP_RETURN script with embedded message"""
    message_hex = message.encode('utf-8').hex()
    message_bytes = bytes.fromhex(message_hex)
    op_return_opcode = b'\x6a'

    data_length = len(message_bytes)
    if data_length <= 75:
        length_byte = bytes([data_length])
    elif data_length <= 255:
        length_byte = b'\x4c' + bytes([data_length])
    else:
        raise ValueError("Message is too long. Maximum allowed is 80 bytes for OP_RETURN.")

    return op_return_opcode + length_byte + message_bytes


def create_transaction_with_op_return(private_key_wif, utxo_txid, utxo_index,
                                      utxo_value, recipient_address,
                                      send_amount, message, fee=1000,
                                      testnet=True):
    """Create Bitcoin transaction with OP_RETURN message"""
    pk = PrivateKey.parse(private_key_wif)

    tx_in = TxIn(bytes.fromhex(utxo_txid), utxo_index, b'', 0xffffffff)
    tx_in._script_pubkey = Tx.get_address_data(pk.address())['script_pubkey']
    tx_in._value = utxo_value
    tx_ins = [tx_in]

    # Calculate change (returned to sender)
    change_amount = utxo_value - send_amount - fee
    if change_amount < 0:
        raise ValueError("Insufficient funds to cover the amount and transaction fee.")

    # Transaction outputs
    tx_outs = []
    tx_outs.append(TxOut(0, create_op_return_script(message)))
    tx_outs.append(TxOut(send_amount, Tx.get_address_data(recipient_address)['script_pubkey'].serialize()))
    if change_amount > 546:  # dust limit
        tx_outs.append(TxOut(change_amount, Tx.get_address_data(pk.address())['script_pubkey'].serialize()))

    tx = Tx(1, tx_ins, tx_outs, 0, testnet=testnet)
    signature(tx, 0, pk)

    # Return both transaction and change amount
    return tx, change_amount


def validate_message_length(message):
    """Check if message exceeds 80 bytes"""
    message_bytes = len(message.encode('utf-8'))
    if message_bytes > 80:
        print(f"\n⚠️  WARNING: Message too long: {message_bytes} / 80 bytes!")
        return False
    print(f"✓ Message length: {message_bytes} / 80 bytes")
    return True


def get_user_input():
    """Collect transaction parameters from user"""
    print("\n" + "="*60)
    print(" BITCOIN MESSAGE TRANSACTION CREATOR")
    print("="*60)
    
    # Private Key
    private_key_wif = input("\nEnter your Private Key (WIF): ").strip()
    
    # UTXO Information
    print("\n--- UTXO Information ---")
    utxo_txid = input("Enter UTXO TXID: ").strip()
    utxo_index = int(input("Enter UTXO Index (default 0): ").strip() or "0")
    utxo_value = int(input("Enter UTXO Value (satoshi): ").strip())
    
    # Transaction Details
    print("\n--- Transaction Details ---")
    recipient_address = input("Enter Recipient Address: ").strip()
    send_amount = int(input("Enter Send Amount (satoshi): ").strip())
    fee = int(input("Enter Transaction Fee (satoshi, default 1000): ").strip() or "1000")
    
    # OP_RETURN Message
    print("\n--- OP_RETURN Message ---")
    message = input("Enter your message (up to 80 bytes): ").strip()
    
    if not validate_message_length(message):
        confirm = input("Continue anyway? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Transaction cancelled.")
            sys.exit(0)
    
    # Network Selection
    print("\n--- Network Selection ---")
    use_testnet_input = input("Use Testnet? (y/n, default y): ").strip().lower()
    use_testnet = use_testnet_input != 'n'
    
    return {
        'private_key_wif': private_key_wif,
        'utxo_txid': utxo_txid,
        'utxo_index': utxo_index,
        'utxo_value': utxo_value,
        'recipient_address': recipient_address,
        'send_amount': send_amount,
        'fee': fee,
        'message': message,
        'testnet': use_testnet
    }


def display_transaction_info(pk, params, change_amount, raw_tx_hex):
    """Display transaction information"""
    print("\n" + "="*60)
    print(" BITCOIN TRANSACTION (OP_RETURN)")
    print("="*60)
    print(f"\nYour BTC Address:         {pk.address()}")
    print(f"Recipient Address:        {params['recipient_address']}")
    print(f"Send Amount:              {params['send_amount']} satoshi")
    print(f"Transaction Fee:          {params['fee']} satoshi")
    print(f"Change Returned:          {change_amount} satoshi (returned to your address)")
    print(f"\nOP_RETURN Message:        {params['message']}")
    print(f"Message Hex:              {params['message'].encode('utf-8').hex()}")
    print(f"\nRawTX (Hex):\n{raw_tx_hex}\n")
    print("="*60)


def save_to_file(raw_tx_hex, message, change_amount, filename="RawTX_OP_RETURN.txt"):
    """Save transaction to file"""
    try:
        with open(filename, 'w') as f:
            f.write("="*60 + "\n")
            f.write(" BITCOIN TRANSACTION WITH OP_RETURN\n")
            f.write("="*60 + "\n\n")
            f.write(f"RawTX (Hex):\n{raw_tx_hex}\n\n")
            f.write(f"Message: {message}\n")
            f.write(f"Message Hex: {message.encode('utf-8').hex()}\n")
            f.write(f"Change Returned: {change_amount} satoshi\n")
        print(f"✓ Transaction saved to file: {filename}\n")
        return True
    except Exception as e:
        print(f"✗ Failed to save file: {e}\n")
        return False


def show_broadcast_links():
    """Display broadcast service links"""
    print("You can broadcast the transaction using:")
    print("  • https://cryptou.ru/bitscanpro/transaction")
    print()


def main():
    """Main execution function"""
    try:
        # Get user input
        params = get_user_input()
        
        # Create transaction
        print("\n⏳ Creating transaction...")
        tx, change_amount = create_transaction_with_op_return(
            private_key_wif=params['private_key_wif'],
            utxo_txid=params['utxo_txid'],
            utxo_index=params['utxo_index'],
            utxo_value=params['utxo_value'],
            recipient_address=params['recipient_address'],
            send_amount=params['send_amount'],
            message=params['message'],
            fee=params['fee'],
            testnet=params['testnet']
        )
        
        # Serialize transaction
        raw_tx_hex = tx.serialize().hex()
        pk = PrivateKey.parse(params['private_key_wif'])
        
        # Display results
        display_transaction_info(pk, params, change_amount, raw_tx_hex)
        
        # Save to file
        save_to_file(raw_tx_hex, params['message'], change_amount)
        
        # Show broadcast links
        show_broadcast_links()
        
        print("✓ Transaction created successfully!\n")
        
    except ValueError as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n✗ Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

