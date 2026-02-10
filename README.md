# 🔐 Multi-Layer Secure Communication System

A sophisticated steganography and cryptography application that enables secure, covert communication by encrypting messages with AES-256 and hiding them within PNG images using LSB steganography.

## 🌟 Features

- **AES-256 Encryption**: Military-grade encryption for message confidentiality
- **SHA-256 Integrity Verification**: Ensures message hasn't been tampered with
- **LSB Steganography**: Hides encrypted data within image pixels
- **Multi-Layer Defense**: Defense-in-Depth security architecture
- **User-Friendly Interface**: Built with Streamlit for easy interaction
- **Download Capability**: Export secure images containing hidden messages
- **Integrity Validation**: Automatic verification of message authenticity

## 🛡️ Security Architecture

This system implements a Defense-in-Depth model with three security layers:

1. **Confidentiality Layer**: AES-256 encryption in CBC mode
2. **Integrity Layer**: SHA-256 hashing for tamper detection
3. **Concealment Layer**: LSB steganography for covert data transmission

## 📋 Prerequisites

- Python 3.7 or higher
- pip package manager

## 🚀 Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd crypto
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Starting the Application

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Encrypting and Hiding a Message

1. Navigate to the **"🔐 Encrypt & Hide"** tab
2. Enter your secret message in the text area
3. Upload a PNG image (carrier image)
4. Click **"🚀 Encrypt & Generate Secure Image"**
5. View encryption details and download the secure stego image

### Extracting and Decrypting a Message

1. Navigate to the **"🔓 Extract & Decrypt"** tab
2. Upload the stego image containing the hidden message
3. Click **"🔍 Extract & Decrypt"**
4. View the decrypted message and integrity verification status

## 🔧 How It Works

### Encryption Process

1. **Message Input**: User provides plaintext message
2. **Key Generation**: Random 32-byte AES key generated
3. **Hash Creation**: SHA-256 hash computed for integrity
4. **Encryption**: Message encrypted using AES-256-CBC
5. **Payload Creation**: Key, IV, hash, and ciphertext packaged as JSON
6. **Steganography**: Payload embedded in image using LSB technique
7. **Output**: Secure stego image generated

### Decryption Process

1. **Image Input**: User uploads stego image
2. **Data Extraction**: LSB steganography reverses to extract payload
3. **Decryption**: AES-256 decrypts the ciphertext
4. **Integrity Check**: SHA-256 hash comparison validates authenticity
5. **Output**: Original message displayed with integrity status

### LSB Steganography Details

- Modifies the least significant bit of RGB color channels
- Uses end marker `1111111111111110` to detect payload boundary
- Minimal visual impact on carrier image
- Capacity depends on image dimensions

## 📁 Project Structure

```
crypto/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
├── assets/
│   └── style.css          # Custom CSS styling
│
└── modules/
    ├── crypto_utils.py    # AES encryption/decryption functions
    └── stego_utils.py     # LSB steganography functions
```

## 📦 Dependencies

- **streamlit**: Web application framework
- **pycryptodome**: Cryptographic library (AES, SHA-256)
- **pillow**: Image processing library

## 🔍 Technical Details

### Cryptography Module (`crypto_utils.py`)

- **Algorithm**: AES-256 in CBC mode
- **Key Size**: 256 bits (32 bytes)
- **Padding**: PKCS#7 padding scheme
- **Hash**: SHA-256 for integrity verification
- **Encoding**: Base64 for binary data serialization

### Steganography Module (`stego_utils.py`)

- **Technique**: Least Significant Bit (LSB) substitution
- **Color Space**: RGB
- **Capacity**: ~3 bits per pixel
- **End Marker**: Custom binary sequence for payload termination
- **Format**: PNG (lossless compression required)

## ⚠️ Important Notes

- Only PNG images are supported (lossless format required)
- Image size must be sufficient to hold the encrypted payload
- Each encrypted message uses a unique random key
- Keys are embedded in the image; secure key management not implemented
- For production use, consider implementing proper key exchange mechanisms

## 🎯 Use Cases

- Secure communication in restricted environments
- Digital watermarking and copyright protection
- Covert data transmission
- Educational purposes for understanding cryptography and steganography
- Research in information security

## 🔐 Security Considerations

- Messages are encrypted with AES-256, providing strong confidentiality
- SHA-256 ensures message integrity and detects tampering
- LSB steganography provides covert communication but can be detected with steganalysis tools
- Keys are stored within the image; suitable for basic security needs
- Not recommended for high-security applications without additional key management

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## 📄 License

This project is open source and available for educational and research purposes.

## 🙏 Acknowledgments

Built using:
- Streamlit for the web interface
- PyCryptodome for cryptographic operations
- Pillow for image processing

---

**Note**: This tool is intended for educational purposes and legitimate security research. Always ensure you have proper authorization before using steganography or encryption tools.
