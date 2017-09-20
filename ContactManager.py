class Contact:
    #Class to take inputs
    #Class properties: Name, phone_number and email
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:

    def __init__(self, contacts = []):
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)
        return print("Contact successfully added")

    def delete_contact(self, name):
        for cotact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact successfully deleted")
        else:
            print("Contact does not exist!")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Name: {}\nPhone Number: {}\nEmail Address:".format(contact.name, contact.phone_number))
            else:
                print("Contact does not exist!")

    def loop(self):
        while True:
            contact_manager = ContactManager()
            choice = input("Type 1 to add contact.\nType 2 to delete contact.\nType 3 to search for a contact.\nType 4 to exit.\n")

            if choice == '1':
                new_contact = Contact(name=input("Enter a name:\n"),phone_number=input("Enter phone number:\n"), email=input("Enter email address\n"))
                contact_manager.add_contact(new_contact)

            elif choice == '2':
                contact_manager.delete_contact(name = input("Enter name:\n"))

            elif choice == '3':
                contact_manager.search_contact(name = input("Enter name:\n"))

            elif choice == '4':
                break

            else:
                print("Invalid choice! Try again.")

manager = ContactManager()
manager.loop()