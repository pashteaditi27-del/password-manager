# Password Manager

A simple Python-based password manager that securely stores and retrieves passwords using encryption.

## Features
- Store passwords securely using encryption
- Retrieve saved passwords
- Master password protection
- Command-line interface

## Technologies Used
- Python
- cryptography (Fernet encryption)
- JSON for storage

## How to Run
1. Install dependencies:
   pip install cryptography

2. Run the program:
   python password_manager.py

## How It Works
- Passwords are encrypted before saving
- Stored in a local JSON file
- Master password is required to access data

## Note
Sensitive files like keys and stored passwords are not uploaded for security reasons.
