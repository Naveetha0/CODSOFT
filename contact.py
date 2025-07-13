contacts = []

def add_contact():
    name = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} | {contact['phone']}")

def search_contact():
    keyword = input("Search by name or phone: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"\nFound:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            found = True
            break
    if not found:
        print("No contact found.\n")

def update_contact():
    name = input("Enter the store name to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input("Enter new phone: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the store name to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            print("Contact deleted.\n")
            return
    print("Contact not found.\n")

def main_menu():
    while True:
        print("\n📞 Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the program
main_menu()
