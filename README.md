# Encryption-Decryption-Software-CLI

A simple command-line application written in Python that securely stores text in encrypted form and allows users to read, append, or delete the stored data. Designed as a lightweight local encryption utility and learning project.

## Features

- Encrypts text before storing it in a file
- Decrypts and displays stored text on demand
- Appends new encrypted content without overwriting existing data
- Permanently deletes all stored data
- User-specific storage with no hard-coded paths
- Fully terminal-based interface
- Lightweight with zero external dependencies

## How It Works

The software applies a character-shift encryption algorithm to printable ASCII characters. All data remains encrypted on disk and is decrypted only when displayed through the program.

## Available Operations

`1` — Read Encrypted Text  
Displays all previously stored content in readable form without modifying the file.

`2` — Encrypt New Text (Append Mode)  
Adds new encrypted content to the existing stored data while preserving previous entries.

`3` — Delete Stored Data  
Permanently removes all encrypted content from storage. This action cannot be undone.

## Special Commands

`UM` — Show User Manual  
`q`  — Quit Program  

## Data Entry Guidelines

- Text can be entered line-by-line
- Press `Enter` on a blank line to finish input
- Supports letters, numbers, symbols, and spaces
- Avoid terminating the program during operations

## Storage Location

The encrypted file is stored in the user’s standard application data directory.

**Windows:**
```
%APPDATA%\EncryptionSoftware\Encryption.txt
```

**Linux:**
```
~/.local/share/EncryptionSoftware/Encryption.txt
```

**macOS:**
```
~/Library/Application Support/EncryptionSoftware/Encryption.txt
```

This approach ensures user-specific storage without requiring administrator privileges and avoids hard-coded usernames.

## Getting Started

**Requirements:**  
`Python 3.x`

**Run the program:**

```
Encryption.py
```

## Safety Notes

- Deleted data cannot be recovered
- The program stores data locally only
- Maintain backups of important information
- Not intended for high-security applications

## Intended Use

- Learning basic encryption concepts
- Understanding file handling in Python
- Demonstrating CLI application design
- Educational and personal use

## Disclaimer

This software uses a simple encryption technique and should not be used for protecting highly sensitive or confidential information.

## Author

Sushant Kumar Kushwaha  
Senior Secondary Student  
Technology Enthusiast and Aspiring Developer  

## Creation Date

July 22, 2025

## License

Released for educational and personal use.
