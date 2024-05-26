import tkinter as tk
from tkinter import messagebox, simpledialog
from core import generate_key, add_password, retrieve_password, delete_account, list_accounts
from security import check_password_strength

def gui_generate_key():
    generate_key()
    messagebox.showinfo("Success", "Encryption key generated and saved to secret.key")

def gui_add_password():
    account = simpledialog.askstring("Input", "Enter account name:")
    password = simpledialog.askstring("Input", "Enter password:", show='*')
    if account and password:
        strength = check_password_strength(password)
        if strength == "Weak":
            messagebox.showwarning("Weak Password", "Password is weak. Please choose a stronger password.")
        else:
            add_password(account, password)
            messagebox.showinfo("Success", f"Password for {account} added.")

def gui_retrieve_password():
    account = simpledialog.askstring("Input", "Enter account name:")
    if account:
        password = retrieve_password(account)
        if password:
            messagebox.showinfo("Password", f"Password for {account} is {password}")
        else:
            messagebox.showwarning("Error", f"Account {account} not found.")

def gui_delete_account():
    account = simpledialog.askstring("Input", "Enter account name:")
    if account:
        if delete_account(account):
            messagebox.showinfo("Success", f"Account {account} deleted.")
        else:
            messagebox.showwarning("Error", f"Account {account} not found.")

def gui_list_accounts():
    accounts = list_accounts()
    if accounts:
        account_list = "\n".join(accounts)
        messagebox.showinfo("Stored Accounts", f"Stored accounts:\n{account_list}")
    else:
        messagebox.showinfo("Stored Accounts", "No accounts stored.")

def main():
    root = tk.Tk()
    root.title("Password Manager")

    btn_generate_key = tk.Button(root, text="Generate Key", command=gui_generate_key)
    btn_generate_key.pack(pady=5)

    btn_add_password = tk.Button(root, text="Add Password", command=gui_add_password)
    btn_add_password.pack(pady=5)

    btn_retrieve_password = tk.Button(root, text="Retrieve Password", command=gui_retrieve_password)
    btn_retrieve_password.pack(pady=5)

    btn_delete_account = tk.Button(root, text="Delete Account", command=gui_delete_account)
    btn_delete_account.pack(pady=5)

    btn_list_accounts = tk.Button(root, text="List Accounts", command=gui_list_accounts)
    btn_list_accounts.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
