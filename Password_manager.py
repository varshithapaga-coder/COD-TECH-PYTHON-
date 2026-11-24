# Task 1 - Simple Password Manager
# Created by Varshitha

passwords = {}

def add_password():
    website = input("Website name: ")
    username = input("Username: ")
    password = input("Password: ")
    passwords[website] = {"username": username, "password": password}
    print("Password saved successfully!")

def view_passwords():
    if not passwords:
        print("No passwords saved yet!")
    else:
        for site, data in passwords.items():
            print(f"Website: {site} | Username: {data['username']} | Password: {data['password']}")

while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        print("Bye Varshitha!")
        break
    else:
        print("Invalid choice, try again!")
