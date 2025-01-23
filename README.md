# Google Authenticator Decoder

A tool to decode Google Authenticator export QR codes and format them for KeePassXC import.

## Setup
1. Install requirements:
```bash
pip install protobuf
```

## Usage
1. Export codes from Google Authenticator
2. Save the migration text to a file
3. Run:
```bash
python decode_auth.py "migration-text-here"
```