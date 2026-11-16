
from workcontacts.models.contact import Contact


def test_contact_creation():
    contact = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com"
    )

    assert contact.first_name == "Ana"
    assert contact.last_name == "Garcia"
    assert contact.email == "ana@email.com"
    assert contact.category == "personal"
    assert contact.id is None


def test_contact_with_all_fields():
    contact = Contact(
        first_name="Carlos",
        last_name="Lopez",
        email="carlos@empresa.com",
        phone="600123456",
        category="cliente",
        notes="Cliente potencial",
        id=10
    )

    assert contact.first_name == "Carlos"
    assert contact.phone == "600123456"
    assert contact.category == "cliente"
    assert contact.notes == "Cliente potencial"
    assert contact.id == 10
