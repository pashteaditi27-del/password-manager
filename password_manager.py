from cryptography.fernet import Fernet
import json
import os
import getpass

def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
fer = Fernet(key)
def encrypt_password(password):
    return fer.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fer.decrypt(encrypted_password.encode()).decode()

def save_password(site, username, password):
    encrypted = encrypt_password(password)

    data = {}

    # load existing data if file exists
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            data = json.load(file)

    # add new entry
    data[site] = {
        "username": username,
        "password": encrypted
    }

    # save back to file
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

def view_password(site):
    if not os.path.exists("passwords.json"):
        print("No data found.")
        return

    with open("passwords.json", "r") as file:
        data = json.load(file)

    if site in data:
        username = data[site]["username"]
        encrypted = data[site]["password"]
        password = decrypt_password(encrypted)

        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print("No entry found for this site.")

# ❌ Delete password
def delete_password(site):
    if not os.path.exists("passwords.json"):
        print("No data found.")
        return

    with open("passwords.json", "r") as file:
        data = json.load(file)

    if site in data:
        del data[site]
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Deleted successfully.")
    else:
        print("No entry found.")

def set_master_password():
    password = input("Set master password: ")
    encrypted = encrypt_password(password)

    with open("master.key", "w") as file:
        file.write(encrypted)

# 🔐 Check master password
def check_master_password():
    if not os.path.exists("master.key"):
        print("No master password found. Set one now.")
        set_master_password()
        return True

    password = getpass.getpass("Enter master password: ")

    with open("master.key", "r") as file:
        saved_password = file.read()

    if decrypt_password(saved_password) == password:
        return True
    else:
        print("Wrong password!")
        return False
def main():
    if not check_master_password():
        return
    while True:
        print("\n1. Add Password")
        print("2. View Password")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(site, username, password)

        elif choice == "2":
            site = input("Enter site: ")
            view_password(site)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()