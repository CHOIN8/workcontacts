
import csv
from workcontacts.models.contact import Contact


def export_contacts_to_csv(contacts, file_path="contacts.csv"):
    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        writer.writerow([
            "First Name",
            "Last Name",
            "Email",
            "Phone",
            "Category",
            "Notes"
        ])

        for contact in contacts:
            writer.writerow([
                contact.first_name,
                contact.last_name,
                contact.email,
                contact.phone or "",
                contact.category,
                contact.notes or ""
            ])



def import_contacts_from_csv(file_path="contacts.csv"):
    contacts = []
    invalid_count = 0

    with open(file_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required_headers = [
            "First Name",
            "Last Name",
            "Email",
            "Phone",
            "Category",
            "Notes"
        ]

        if reader.fieldnames != required_headers:
            raise ValueError("Invalid CSV headers")

        for row in reader:
            try:
                contact = Contact(
                    first_name=row["First Name"],
                    last_name=row["Last Name"],
                    email=row["Email"],
                    phone=row["Phone"] or None,
                    category=row["Category"] or "personal",
                    notes=row["Notes"] or None
                )

                contacts.append(contact)

            except ValueError:
                invalid_count += 1

    return contacts, invalid_count
