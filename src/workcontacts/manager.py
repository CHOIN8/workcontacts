from workcontacts.models.contact import Contact
from workcontacts.utils.validators import validate_email,validate_name

class ContactManager:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        if self.find_by_email(contact.email):
            raise ValueError("A contact with this email already exists")

        self.contacts.append(contact)

    def filter_by_category(self, category: str):
        return [
            contact for contact in self.contacts
            if contact.category.lower() == category.lower()
        ]

    def find_by_email(self, email: str):
        for contact in self.contacts:
            if contact.email == email:
                return contact
            
    def get_statistics(self):
        return {
            "total": len(self.contacts),
            "personal": sum(
                1 for contact in self.contacts
                if contact.category.lower() == "personal"
            ),
            "work": sum(
                1 for contact in self.contacts
                if contact.category.lower() == "work"
            ),
            "without_phone": sum(
                1 for contact in self.contacts
                if not contact.phone
            )
        }


        return None
    ALLOWED_UPDATE_FIELDS = {
        "first_name",
        "last_name",
        "email",
        "phone",
        "category",
        "notes"
    }
    def delete_by_email(self, email: str):
        for contact in self.contacts:
            if contact.email == email:
                self.contacts.remove(contact)
                return True
        return False
            
    def update_contact(self, current_email: str, **kwargs):
        contact = self.find_by_email(current_email)

        if contact is None:
            return False
        if "first_name" in kwargs:
            if not validate_name(kwargs["first_name"]):
                raise ValueError("First name cannot be empty or invalid")

        if "last_name" in kwargs:
            if not validate_name(kwargs["last_name"]):
                raise ValueError("Last name cannot be empty or invalid")

        if "email" in kwargs:
            if not validate_email(kwargs["email"]):
                raise ValueError("Email address is invalid")

            existing_contact = self.find_by_email(kwargs["email"])

            if existing_contact is not None and existing_contact is not contact:
                raise ValueError("A contact with this email already exists")

        for field, value in kwargs.items():
            if field in self.ALLOWED_UPDATE_FIELDS:
                setattr(contact, field, value)

        return True