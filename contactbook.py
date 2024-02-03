class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, keyword):
        matching_contacts = [contact for contact in self.contacts
                              if keyword.lower() in contact.name.lower() or
                              keyword in contact.phone_number]
        if not matching_contacts:
            print("No matching contacts found.")
        else:
            for contact in matching_contacts:
                print(contact)

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[i] = new_contact
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted successfully!")
                return
        print("Contact not found.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter Name or Phone Number to search: ")
            contact_manager.search_contact(keyword)

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter New Name: ")
            new_phone_number = input("Enter New Phone Number: ")
            new_email = input("Enter New Email: ")
            new_address = input("Enter New Address: ")
            updated_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_manager.update_contact(old_name, updated_contact)

        elif choice == '5':
            name_to_delete = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name_to_delete)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()