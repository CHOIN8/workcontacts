import json
from pathlib import Path
from workcontacts.models.contact import Contact
def save_contacts(contacts, file_path):
    data = []

    for contact in contacts:
        data.append({
            "first_name": contact.first_name,
            "last_name": contact.last_name,
            "email": contact.email,
            "phone": contact.phone,
            "category": contact.category,
            "notes": contact.notes,
            "id": contact.id
        })

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
def load_contacts(file_path):
    if not Path(file_path).exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        contacts = []

    for item in data:
        contact = Contact(
            first_name=item["first_name"],
            last_name=item["last_name"],
            email=item["email"],
            phone=item["phone"],
            category=item["category"],
            notes=item["notes"],
            id=item["id"]
        )

        contacts.append(contact)

    return contacts

def backup_contacts(contacts, file_path="contacts_backup.json"):
    save_contacts(contacts, file_path) 
def restore_backup(file_path="contacts_backup.json"):
    return load_contacts(file_path)    