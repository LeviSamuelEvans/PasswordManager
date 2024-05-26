## Basic Password Manager with Encryption

This is just a small project to build a command-line based password manager that securely stores user passwords in an encrypted file.


### Features:
1. **Add a new password**: Users can add a new account and its password.
2. **Retrieve a password**: Users can retrieve the password for an account.
3. **Delete an account**: Users can delete an account and its password.
4. **List all accounts**: Users can list all stored accounts.
5. **Encrypt passwords**: All passwords will be encrypted before storing them in a file.
6. **Decrypt passwords**: Passwords will be decrypted when retrieved.

### Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/password-manager.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

### Usage

- Generate encryption key (run this once before using the manager):

```
python3 main.py --generate-key
```

- Add a new password:

```
python3 main.py --add <account> <password>
```

- Retrieve a password

```
python3 main.py --retrieve <account>
```

- Delete an account

```
python3 main.py --delete <account>
```

- List all accounts

```
python main.py --list
```


## Future features

- A hacker module
- More efficient database for storage
- A proper GUI