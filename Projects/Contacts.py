contacts = []

def add_contacts():
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("E-Mail: ")

    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)


def view_contacts():
    if not contacts:    
        print("No contacts yet!")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def search_contact():
    search_name = input("Enter name to search: ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
        print("No contact found.")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        add_contacts()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        print("Exited successfully")
        break
    else:
        print("Invalid input. Try again.1")