# ===================================================
#  BitScanPro Bitcoin Transaction (Google Colab Version)
# ===================================================

# Install dependencies (run once if needed)
# !pip install ipywidgets zmq urllib3 requests pycryptodome

# Clone source code repository if not yet downloaded
# !git clone https://github.com/zoeir/BitScanPro-Bitcoin-Transaction.git > /dev/null 2>&1
# %cd BitScanPro-Bitcoin-Transaction

# Import required modules
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from secp256k1 import *
from sighash import *

# ---------- Functions ----------
def create_op_return_script(message):
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


# ---------- User Interface (CyberPunk Style Applied) ----------

header_html = widgets.HTML("""
    <h2 style='color:#FF65A3;letter-spacing:2px;margin-bottom:10px;text-shadow:0 2px 20px #23C9FF;'>BitScanPro Bitcoin Transaction</h2>
    <p style='font-size:18px; color:#C3FF00; background:#090930; padding:10px; border-radius:10px;'>Create and encode OP_RETURN Bitcoin transactions with a <span style='color:#23C9FF; font-weight:bold;'>interface.</span> <br></p>

""")

private_key_wif = widgets.Text(
    placeholder='Enter your private key (WIF)',
    description='Private Key (WIF):',
    layout=widgets.Layout(width='95%', margin='8px 0', border='2px solid #FF65A3', font_size='16px', background_color='#181830', color='#23C9FF')
)
utxo_txid = widgets.Text(
    placeholder='Enter UTXO TXID',
    description='UTXO TXID:',
    layout=widgets.Layout(width='95%', margin='8px 0', border='2px solid #23C9FF', font_size='16px', background_color='#181830', color='#FF65A3')
)
utxo_index = widgets.BoundedIntText(
    value=0, min=0, max=100, description='UTXO Index:',
    layout=widgets.Layout(width='40%', margin='8px 0 0 0', background_color='#181830', color='#C3FF00')
)
utxo_value = widgets.IntText(
    value=0, description='UTXO Value (satoshi):',
    layout=widgets.Layout(width='55%', margin='8px 0 0 0', background_color='#181830', color='#FF65A3')
)
fee = widgets.IntSlider(
    value=1000, min=500, max=10000, step=100, description='Transaction Fee (sat):',
    style={'handle_color': '#C3FF00'},
    layout=widgets.Layout(width='65%', margin='8px 0 0 0', background_color='#1010A0', color='#C3FF00')
)
send_amount = widgets.IntText(
    value=0, description='Send Amount (sat):',
    layout=widgets.Layout(width='55%', margin='8px 0 0 0', background_color='#181830', color='#FF65A3')
)
recipient_address = widgets.Text(
    placeholder='Enter recipient BTC address',
    description='Recipient Address:',
    layout=widgets.Layout(width='95%', margin='8px 0', border='2px solid #C3FF00', font_size='16px', background_color='#181830', color='#23C9FF')
)
message = widgets.Textarea(
    placeholder='Enter your OP_RETURN message (up to 80 bytes)',
    description='Message:',
    layout=widgets.Layout(width='98%', height='80px', margin='8px 0', border='2px solid #23C9FF', font_family='monospace', font_size='17px', background_color='#1A003D', color='#FF65A3')
)
byte_warning = widgets.HTML(value="<span style='color:#CCCCCC'>0 / 80 bytes</span>")
use_testnet = widgets.Checkbox(
    value=True, description='Use Testnet',
    layout=widgets.Layout(margin='8px 0', background_color='#202047', color='#C3FF00')
)
submit_button = widgets.Button(
    description='Create Bitcoin Transaction',
    button_style='',
    layout=widgets.Layout(width='60%', height='45px', margin='15px 0', padding='5px', background_color='#23C9FF'),
    style={'font_weight':'bold', 'font_size':'18px', 'button_color':'#FF65A3', 'text_color':'#0F0F23'}
)

def update_message_length(change):
    current_bytes = len(change['new'].encode('utf-8'))
    if current_bytes > 80:
        byte_warning.value = f"<span style='color:#FF2300; font-weight:bold;'>Message too long: {current_bytes} / 80 bytes!</span>"
    else:
        byte_warning.value = f"<span style='color:#23C9FF'>{current_bytes} / 80 bytes</span>"

message.observe(update_message_length, 'value')

form = widgets.VBox([
    header_html,
    widgets.HBox([private_key_wif, utxo_txid]),
    widgets.HBox([utxo_index, utxo_value, send_amount, fee]),
    recipient_address,
    message,
    byte_warning,
    use_testnet,
    submit_button
], layout=widgets.Layout(border='3px solid #23C9FF', padding='22px', background_color='#191970', box_shadow='0 4px 24px #1A003D'))

display(form)

# ---------- Processing ----------
def on_submit_clicked(b):
    clear_output(wait=True)
    display(form)
    try:
        tx, change_amount = create_transaction_with_op_return(
            private_key_wif=private_key_wif.value,
            utxo_txid=utxo_txid.value,
            utxo_index=utxo_index.value,
            utxo_value=int(utxo_value.value),
            recipient_address=recipient_address.value,
            send_amount=int(send_amount.value),
            message=message.value,
            fee=int(fee.value),
            testnet=use_testnet.value
        )
        raw_tx_hex = tx.serialize().hex()
        pk = PrivateKey.parse(private_key_wif.value)

        print("\n===============================")
        print(" BITCOIN TRANSACTION (OP_RETURN)")
        print("===============================")
        print(f"Your BTC Address:         {pk.address()}")
        print(f"Recipient Address:        {recipient_address.value}")
        print(f"Send Amount:              {send_amount.value} satoshi")
        print(f"Transaction Fee:          {fee.value} satoshi")
        print(f"Change Returned:          {change_amount} satoshi")
        print(f"\nOP_RETURN Message:        {message.value}")
        print(f"\nRawTX (Hex):\n{raw_tx_hex}\n")

        with open("RawTX_OP_RETURN.txt", 'w') as f:
            f.write(raw_tx_hex + "\n")
            f.write(f"\nMessage: {message.value}\n")
            f.write(f"Hex: {message.value.encode('utf-8').hex()}\n")
            f.write(f"Change Returned: {change_amount} satoshi\n")

        print("✓ Saved to file: RawTX_OP_RETURN.txt\n")
        print("You can broadcast the transaction using:\nhttps://cryptou.ru/bitscanpro/transaction\n")

    except Exception as e:
        print(f"Error: {e}")

submit_button.on_click(on_submit_clicked)
