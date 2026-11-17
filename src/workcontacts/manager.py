from workcontacts.models.contact import Contact


class ContactManager:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        if self.find_by_email(contact.email):
            raise ValueError("A contact with this email already exists")

        self.contacts.append(contact)

    def find_by_email(self, email: str):
        for contact in self.contacts:
            if contact.email == email:
                return contact

        return None

    def delete_by_email(self, email: str):
        for contact in self.contacts:
            if contact.email == email:
                self.contacts.remove(contact)
                return True

        return False