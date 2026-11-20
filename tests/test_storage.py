from workcontacts.storage import save_contacts, load_contacts, backup_contacts
from workcontacts.models.contact import Contact


def test_save_contacts(tmp_path):
    file_path = tmp_path / "contacts.json"

    contact = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        phone="600123456"
    )

    save_contacts([contact], file_path)

    assert file_path.exists()


def test_load_contacts(tmp_path):
    file_path = tmp_path / "contacts.json"

    contact = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        phone="600123456"
    )

    save_contacts([contact], file_path)

    contacts = load_contacts(file_path)

    assert len(contacts) == 1
    assert contacts[0].first_name == "Ana"
    assert contacts[0].email == "ana@email.com"
    assert contacts[0].phone == "600123456"


def test_load_contacts_file_does_not_exist(tmp_path):
    file_path = tmp_path / "missing.json"

    contacts = load_contacts(file_path)

    assert contacts == []


def test_backup_contacts(tmp_path):
    file_path = tmp_path / "contacts_backup.json"

    contact = Contact(
        first_name="Carlos",
        last_name="Lopez",
        email="carlos@email.com",
        phone="600987654"
    )

    backup_contacts([contact], file_path)

    assert file_path.exists()

    contacts = load_contacts(file_path)

    assert len(contacts) == 1
    assert contacts[0].first_name == "Carlos"
    assert contacts[0].email == "carlos@email.com"
    def restore_backup(file_path="contacts_backup.json"):
        return load_contacts(file_path)