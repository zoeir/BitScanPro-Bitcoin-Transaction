<!-- wp:image {"sizeSlug":"large","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-large"><img src="https://raw.githubusercontent.com/zoeir/BitScanPro-Bitcoin-Transaction/refs/heads/main/image.png" alt=""/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-large"><img src="https://raw.githubusercontent.com/zoeir/BitScanPro-Bitcoin-Transaction/refs/heads/main/result.png" alt=""/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-large"><img src="https://raw.githubusercontent.com/zoeir/BitScanPro-Bitcoin-Transaction/refs/heads/main/bitscanpro.png" alt=""/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-large"><img src="https://raw.githubusercontent.com/zoeir/BitScanPro-Bitcoin-Transaction/refs/heads/main/decoding.png" alt=""/></figure>
<!-- /wp:image -->

# 💬 [BitScanPro Bitcoin Transaction Creator](https://colab.research.google.com/drive/1e93p7gxpTtfMU2L83w7I1tRDJQ1tENYa?usp=sharing)

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![Bitcoin](https://img.shields.io/badge/Bitcoin-OP__RETURN-orange.svg)](https://en.bitcoin.it/wiki/OP_RETURN)

Create Bitcoin transactions with embedded OP_RETURN messages. This tool allows you to permanently store text messages on the Bitcoin blockchain while sending BTC to any address.

## 🌟 Features

- ✅ **OP_RETURN Message Embedding** - Store up to 80 bytes of data on-chain
- ✅ **Interactive UI** - User-friendly interface in Google Colab
- ✅ **CLI Version** - Command-line interface for desktop use
- ✅ **Automatic Change Calculation** - Returns remaining funds to sender
- ✅ **Testnet & Mainnet Support** - Test safely before going live
- ✅ **Transaction Export** - Save RawTX to file for broadcasting
- ✅ **Real-time Message Length Validation** - Prevents errors before creation

## 📋 Table of Contents

- [Installation](#-installation)- [Usage](#-usage)  - [Google Colab Version](#-google-colab-version)  - [Python CLI Version](#-python-cli-version)- [Broadcasting Transaction](#-broadcasting-transaction)- [Requirements](#-requirements)- [Examples](#-examples)- [Security](#-security)- [Contributing](#-contributing)- [License](#-license)---

## 🚀 Installation

### Prerequisites

<!-- wp:code -->
<pre class="wp-block-code"><code>- Python 3.6 or higher
- Git</code></pre>
<!-- /wp:code -->


### Clone Repository
<!-- wp:code -->
<pre class="wp-block-code"><code>git clone https://github.com/zoeir/BitScanPro-Bitcoin-Transaction.git
cd BitScanPro-Bitcoin-Transaction</code></pre>
<!-- /wp:code -->

### Install Dependencies

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install ipywidgets zmq urllib3 requests pycryptodome</code></pre>
<!-- /wp:code -->


---

<h1>YouTube video tutorial for using BitScanPro</h1>

[![Watch the video](https://img.youtube.com/vi/2_d8-8-J8IQ/maxresdefault.jpg)](https://youtu.be/2_d8-8-J8IQ)

<p align="center">
  <a href="https://youtu.be/2_d8-8-J8IQ" target="_blank">Watch video on YouTube: https://youtu.be/2_d8-8-J8IQ </a>
</p>

---



## 📖 Usage

### 🌐 [Google Colab Version](https://colab.research.google.com/drive/1e93p7gxpTtfMU2L83w7I1tRDJQ1tENYa?usp=sharing)

[https://colab.research.google.com/drive/1e93p7gxpTtfMU2L83w7I1tRDJQ1tENYa](https://colab.research.google.com/drive/1e93p7gxpTtfMU2L83w7I1tRDJQ1tENYa?usp=sharing)

Perfect for users who want a graphical interface without installing anything locally.

#### Step 1: Open Google Colab

Navigate to [Google Colab](https://colab.research.google.com/)

#### Step 2: Create New Notebook

Click **File** → **New Notebook**

#### Step 3: Install Dependencies

Copy and paste this code into the first cell:

<!-- wp:code -->
<pre class="wp-block-code"><code>!pip install ipywidgets zmq urllib3 requests pycryptodome
!git clone https://github.com/zoeir/BitScanPro-Bitcoin-Transaction.git > /dev/null 2>&amp;1
%cd BitScanPro-Bitcoin-Transaction</code></pre>
<!-- /wp:code -->

Run the cell (press `Shift + Enter`)

#### Step 4: Load the Script

In a new cell, copy the entire content of [`colab.py`](colab.py) and run it.

#### Step 5: Fill the Form

An interactive form will appear with the following fields:

<!-- wp:code -->
<pre class="wp-block-code"><code>| Field | Description | Example |
|-------|-------------|---------|
| 🔑 **Private Key (WIF)** | Your Bitcoin private key in WIF format | `5J64pq77XjeacCezwmAr2V1s7snvvJkuAz8sENxw7xCkikceV6e` |
| 🆔 **UTXO TXID** | Transaction ID containing your funds | `2a29fdb4e188f827da3c3175856b3ed95819b323bb303a46b8036534e78c76db` |
| 🔢 **UTXO Index** | Output index (usually 0) | `0` |
| 💰 **UTXO Value** | Amount in satoshi | `30352330` |
| 💸 **Transaction Fee** | Network fee (500-10000 sat) | `1000` |
| 📤 **Send Amount** | Amount to send in satoshi | `600` |
| 📍 **Recipient Address** | Destination Bitcoin address | `1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC` |
| 💬 **Message** | Your text message (max 80 bytes) | `Hello Bitcoin!` |
| 🧪 **Use Testnet** | Enable for testing | ☑️ Checked |</code></pre>
<!-- /wp:code -->

#### Step 6: Create Transaction

Click **"Create Bitcoin Transaction"** button

#### Step 7: Copy RawTX

The output will display:
- ✅ Your BTC Address- ✅ Recipient Address  - ✅ Send Amount- ✅ Transaction Fee- ✅ Change Returned- ✅ OP_RETURN Message- ✅ **RawTX (Hex)** ← Copy this for broadcasting---

### 🖥️ Python CLI Version

For users who prefer command-line interface on their desktop/laptop.

#### Step 1: Navigate to Repository

<!-- wp:code -->
<pre class="wp-block-code"><code>cd BitScanPro-Bitcoin-Transaction</code></pre>
<!-- /wp:code -->

#### Step 2: Run the Script

<!-- wp:code -->
<pre class="wp-block-code"><code>python3 main.py</code></pre>
<!-- /wp:code -->

#### Step 3: Follow Interactive Prompts

The script will ask for:

<!-- wp:code -->
<pre class="wp-block-code"><code>=================================
BITSCANPRO BITCOIN TRANSACTION CREATOR
Enter your Private Key (WIF): 5J64pq77Xjeac...

--- UTXO Information ---
Enter UTXO TXID: 2a29fdb4e188f827...
Enter UTXO Index (default 0): 0
Enter UTXO Value (satoshi): 30352330

--- Transaction Details ---
Enter Recipient Address: 1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC
Enter Send Amount (satoshi): 600
Enter Transaction Fee (satoshi, default 1000): 1000

--- OP_RETURN Message ---
Enter your message (up to 80 bytes): Hello Bitcoin!

--- Network Selection ---
Use Testnet? (y/n, default y): y</code></pre>
<!-- /wp:code -->


#### Step 4: Review Output

<!-- wp:code -->
<pre class="wp-block-code"><code>============================================================
BITCOIN TRANSACTION (OP_RETURN)
Your BTC Address: 14NWDXkQwcGN1Pd9fboL8npVynD5SfyJAE
Recipient Address: 1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC
Send Amount: 600 satoshi
Transaction Fee: 1000 satoshi
Change Returned: 30350730 satoshi

OP_RETURN Message: Hello Bitcoin!

RawTX (Hex):
0100000001db768ce7346503b8463a30bb23b31958d93e6b8575313cda..
============================================================</code></pre>
<!-- /wp:code -->

✓ Transaction saved to file: RawTX_OP_RETURN.txt

---

## 📡 Broadcasting Transaction

After creating your transaction, broadcast it using any of these services:

### Mainnet Services


| Service | URL |
|---------|-----|
| 🌐 **Bitcoin Message** | [bitcoinmessage.ru](https://bitcoinmessage.ru) |

**Steps:**

1. Copy your **RawTX (Hex)** from the output
2. Visit any broadcast service above
3. Paste the RawTX into the form
4. Click "Broadcast" or "Push"
5. Wait for confirmation 

---

## 📦 Requirements

### Python Packages

- `pycryptodome` - Cryptographic library
- `ipywidgets` (Colab only) - Interactive widgets
- `IPython` (Colab only) - Display utilities

### Repository Dependencies

This tool requires modules from [BitScanPro-Bitcoin-Transaction](https://github.com/zoeir/BitScanPro-Bitcoin-Transaction):
- `secp256k1.py` - Elliptic curve operations
- `sighash.py` - Transaction signing

---

## 💡 Examples

### Example 1: Simple Message
Message: "Hello from the blockchain!"
Send Amount: 1000 satoshi
Fee: 1000 satoshi


### Example 2: Timestamp Proof



Message: "Document hash: 5d41402abc4b2a76b9719d911017c592"
Send Amount: 546 satoshi (dust limit)
Fee: 2000 satoshi


### Example 3: Identity Proof

Message: "github.com/zoeir/BitScanPro-Bitcoin-Transaction/ - Verified 2025"
Send Amount: 600 satoshi
Fee: 1500 satoshi

---

## 🔒 Security

### ⚠️ Important Security Notes

- **Never share your private key** with anyone
- **Test on Testnet first** before using real BTC
- **Double-check addresses** before broadcasting
- **Backup your private keys** securely offline
- **Use secure connections** when broadcasting transactions
- **OP_RETURN data is permanent** and cannot be deleted

### Best Practices

1. ✅ Use testnet for testing
2. ✅ Verify recipient address multiple times
3. ✅ Start with small amounts
4. ✅ Keep private keys in encrypted storage
5. ✅ Never commit private keys to Git

---




## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

<!-- wp:code -->
<pre class="wp-block-code"><code>git clone https://github.com/zoeir/BitScanPro-Bitcoin-Transaction.git
cd BitScanPro-Bitcoin-Transaction
pip install -r requirements.txt</code></pre>
<!-- /wp:code -->

### Reporting Issues

Please use the [GitHub Issues](https://github.com/zoeir/BitScanPro-Bitcoin-Transaction/issues) page to report bugs or request features.

---## 📄 LicenseThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---## 🙏 Acknowledgments- Bitcoin Core developers
- [BitScanPro-Bitcoin-Transaction](https://github.com/zoeir/BitScanPro-Bitcoin-Transaction) repository
- Python cryptography community---## 📞 Support- 🌐 Website: [bitcoinmessage.ru](https://bitcoinmessage.ru)
- 📧 Issues: [GitHub Issues](https://github.com/zoeir/BitScanPro-Bitcoin-Transaction/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/zoeir/BitScanPro-Bitcoin-Transaction/discussions)---## ⭐ Star HistoryIf you find this project useful, please consider giving it a star! ⭐---**Made with ❤️ for the Bitcoin community**---## 📸 Screenshots

### Google Colab Interface
![Colab Interface](https://via.placeholder.com/800x400?text=Google+Colab+Interface)

### CLI Version Output
![CLI Output](https://via.placeholder.com/800x400?text=CLI+Version+Output)

---


---

## 📊 Statistics

![GitHub stars](https://img.shields.io/github/stars/zoeir/BitScanPro-Bitcoin-Transaction?style=social)
![GitHub forks](https://img.shields.io/github/forks/zoeir/BitScanPro-Bitcoin-Transaction?style=social)
![GitHub issues](https://img.shields.io/github/issues/zoeir/BitScanPro-Bitcoin-Transaction)
![GitHub pull requests](https://img.shields.io/github/issues-pr/zoeir/BitScanPro-Bitcoin-Transaction)

---










