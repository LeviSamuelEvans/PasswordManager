# Basic Password Manager with Encryption

This is just a small project to build a command-line based password manager that securely stores user passwords in an encrypted file.

## Overview
A secure password manager that allows you to store, retrieve, and manage your passwords securely. It uses encryption to protect your passwords.

## Features
- Generate a new encryption key
- Add, retrieve, delete, and list passwords
- Backup and restore encryption keys
- Check password strength

## Key Management
- **Generate Key**: Creates a new encryption key. **Warning**: Generating a new key will make previously encrypted passwords inaccessible unless backed up.
- **Backup Key**: Backs up the current key to `secret.key.bak`.
- **Restore Key**: Restores the key from `secret.key.bak`.

## Usage
1. **Generate a Key**: Ensure you generate a key before adding passwords.
2. **Backup the Key**: Regularly backup your key to prevent data loss.
3. **Restore the Key**: Restore the key if you accidentally generate a new one or lose the current key.

## Running the Application
```
python3 main.py
```