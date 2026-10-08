# password_manager.py

def add_password(site, username, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{site},{username},{password}\n")
    print("✅ Password saved!")

def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No passwords saved yet.")
            else:
                for line in lines:
                    site, username, password = line.strip().split(",")
                    print(f"Site: {site} | User: {username} | Pass: {password}")
    except FileNotFoundError:
        print("No password file found yet.")

def delete_password(site):
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        with open("passwords.txt", "w") as f:
            for line in lines:
                if not line.startswith(site + ","):
                    f.write(line)
        print(f"🗑️ Deleted password for {site}")
    except FileNotFoundError:
        print("No password file found yet.")

while True:
    print("\n--- Password Manager ---")
    print("1. Add password")
    print("2. View passwords")
    print("3. Delete password")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        site = input("Enter site: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        add_password(site, username, password)
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        site = input("Enter site to delete: ")
        delete_password(site)
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
