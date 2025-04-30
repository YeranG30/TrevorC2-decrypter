# TrevorC2 Decryptor (Python)

A lightweight standalone decryptor for TrevorC2-style AES-CBC encrypted C2 traffic.

This script accepts `oldcss=` or `guid=` style base64-encoded beacon data and decrypts it based on AES-256-CBC with IV extraction and SHA-256 key hashing.

## Features

- Supports TrevorC2 AES-256-CBC encryption
- Extracts IV from ciphertext automatically
- Handles base64 padding issues
- Loops for multiple inputs
- Clear error handling and feedback

## Example

