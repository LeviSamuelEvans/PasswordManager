import os
from cryptography.fernet import Fernet
import json
from tkinter import messagebox, simpledialog

KEY_FILE = "secret.key"
BACKUP_KEY_FILE = "secret.key.bak"
PASSWORD_FILE = "passwords.json"

# generate a key for encryption
def generate_key():
    """
    Generates a new encryption key and saves it to a file named 'secret.key'.
    """
    if os.path.exists(KEY_FILE):
        response = messagebox.askyesno("Key Exists", "A key already exists. Do you want to overwrite it?")
        if not response:
            return
        os.rename(KEY_FILE, BACKUP_KEY_FILE)
        messagebox.showinfo("Backup", f"Old key has been backed up to {BACKUP_KEY_FILE}")

    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "New encryption key generated and saved to secret.key")

def backup_key():
    if os.path.exists(KEY_FILE):
        os.rename(KEY_FILE, BACKUP_KEY_FILE)
        print(f"Old key has been backed up to {BACKUP_KEY_FILE}")

def restore_key():
    if os.path.exists(BACKUP_KEY_FILE):
        os.rename(BACKUP_KEY_FILE, KEY_FILE)
        print(f"Backup key restored from {BACKUP_KEY_FILE}")

# load the encrypted key
def load_key():
    return open(KEY_FILE, "rb").read()

# new password encryption using the key and fernet
def encrypt_password(password, key):
    """
    Encrypts the given password using the provided key.

    Parameters
    ----------
        password : str
            The password to be encrypted.
        key : bytes
            The encryption key.

    Returns
    -------
        The encrypted password : str
    """
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()


# decryption of the password using the key and fernet
def decrypt_password(encrypted_password, key):
    """
    Decrypts the given encrypted password using the provided key.

    Parameters
    ----------
        encrypted_password : str
            The encrypted password to be decrypted.
        key : bytes
            The key used for decryption.

    Returns
    -------
         The decrypted password : str
    """
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()


# load password store
def load_password_store(filename="passwords.json"):
    """
    Load the password store from a JSON file.

    Parameters
    ----------
        filename : str
            The name of the JSON file to load the password store from.
            Defaults to "passwords.json".

    Returns
    -------
            The loaded password store as a dictionary : dict

    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}


# save the store
def save_password_store(passwords, filename="passwords.json"):
    """
    Saves the passwords dictionary to a JSON file.

    Parameters
    ----------
        passwords : dict
            The dictionary containing the passwords.
        filename : str, optional
            The name of the file to save the passwords to.
            Defaults to "passwords.json".
    """
    with open(filename, "w") as file:
        json.dump(passwords, file)


# method to add a new password
def add_password(account, password):
    """
    Add a password for the specified account.

    Parameters
    ----------
    - account (str): The account for which the password is being added.
    - password (str): The password to be added.

    """
    key = load_key()
    passwords = load_password_store()
    passwords[account] = encrypt_password(password, key)
    save_password_store(passwords)


# retrieve a password
def retrieve_password(account):
    """
    Retrieves the password for the specified account.

    Parameters
    ----------
    account : str
        The name of the account.

    Returns
    -------
    str or None:
        The decrypted password if the account exists, None otherwise.
    """

    key = load_key()
    passwords = load_password_store()
    if account in passwords:
        return decrypt_password(passwords[account], key)
    return None


# delete an account from the store
def delete_account(account):
    """
    Deletes the specified account from the password store.

    Parameters
    ----------
        account : str
            The account to be deleted.

    Returns:
        bool: True if the account was successfully deleted, False otherwise.
    """
    passwords = load_password_store()
    if account in passwords:
        del passwords[account]
        save_password_store(passwords)
        return True
    return False


# method to list all accounts
def list_accounts():
    passwords = load_password_store()
    return passwords.keys()
