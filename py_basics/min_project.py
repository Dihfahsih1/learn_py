# Contact Book Mini-Project

# Initialize an empty dictionary to store contacts
contact_book = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("Contacts in the Contact Book:")
    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 20)

def search_contact():
    name = input("Enter the name to search for: ")
    if name in contact_book:
        details = contact_book[name]
        print(f"Contact found:")
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"Contact '{name}' not found in the Contact Book.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()