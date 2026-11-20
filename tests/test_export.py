
import csv
import pytest

from workcontacts.export import export_contacts_to_csv
from workcontacts.models.contact import Contact
from workcontacts.export import import_contacts_from_csv


def test_export_contacts_to_csv(tmp_path):
    file_path = tmp_path / "contacts.csv"

    contact = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        phone="600123456",
        category="personal",
        notes="Test note"
    )

    export_contacts_to_csv([contact], file_path)

    assert file_path.exists()

    with open(file_path, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.reader(file))

    assert rows[0] == [
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Category",
        "Notes"
    ]

    assert rows[1] == [
        "Ana",
        "Garcia",
        "ana@email.com",
        "600123456",
        "personal",
        "Test note"
    ]

def test_export_contacts_without_optional_fields(tmp_path):
    file_path = tmp_path / "contacts.csv"

    contact = Contact(
        first_name="Luis",
        last_name="Perez",
        email="luis@email.com"
    )

    export_contacts_to_csv([contact], file_path)

    with open(file_path, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.reader(file))

    assert rows[1] == [
        "Luis",
        "Perez",
        "luis@email.com",
        "",
        "personal",
        ""
    ]

def test_import_contacts_from_csv(tmp_path):
    file_path = tmp_path / "contacts.csv"

    file_path.write_text(
        "First Name,Last Name,Email,Phone,Category,Notes\n"
        "Ana,Garcia,ana@email.com,600123456,personal,Test note\n",
        encoding="utf-8-sig"
    )

    contacts, invalid_count = import_contacts_from_csv(file_path)

    assert invalid_count == 0
    assert len(contacts) == 1
    assert contacts[0].first_name == "Ana"
    assert contacts[0].last_name == "Garcia"
    assert contacts[0].email == "ana@email.com"
    assert contacts[0].phone == "600123456"
    assert contacts[0].category == "personal"
    assert contacts[0].notes == "Test note"

def test_import_contacts_without_optional_fields(tmp_path):
    file_path = tmp_path / "contacts.csv"

    file_path.write_text(
        "First Name,Last Name,Email,Phone,Category,Notes\n"
        "Luis,Perez,luis@email.com,,,\n",
        encoding="utf-8-sig"
    )

    contacts, invalid_count = import_contacts_from_csv(file_path)

    assert invalid_count == 0
    assert len(contacts) == 1
    assert contacts[0].phone is None
    assert contacts[0].category == "personal"
    assert contacts[0].notes is None


def test_import_contacts_with_invalid_headers(tmp_path):
    file_path = tmp_path / "contacts.csv"

    file_path.write_text(
        "Name,Email\n"
        "Ana,ana@email.com\n",
        encoding="utf-8-sig"
    )

    with pytest.raises(ValueError, match="Invalid CSV headers"):
        import_contacts_from_csv(file_path)


def test_import_contacts_skips_invalid_email(tmp_path):
    file_path = tmp_path / "contacts.csv"

    file_path.write_text(
        "First Name,Last Name,Email,Phone,Category,Notes\n"
        "Ana,Garcia,ana@email.com,600123456,personal,Valid\n"
        "Luis,Perez,email-invalido,600123457,personal,Invalid\n"
        "Carlos,Lopez,carlos@email.com,600123458,work,Valid\n",
        encoding="utf-8-sig"
    )
        
    contacts, _ = import_contacts_from_csv(file_path)

    assert len(contacts) == 2
    assert contacts[0].first_name == "Ana"
    assert contacts[1].first_name == "Carlos"

def test_import_contacts_returns_invalid_count(tmp_path):
    file_path = tmp_path / "contacts.csv"

    file_path.write_text(
        "First Name,Last Name,Email,Phone,Category,Notes\n"
        "Ana,Garcia,ana@email.com,600123456,personal,Valid\n"
        "Luis,Perez,email-invalido,600123457,personal,Invalid\n",
        encoding="utf-8-sig"
    )

    contacts, invalid_count = import_contacts_from_csv(file_path)

    assert len(contacts) == 1
    assert invalid_count == 1


