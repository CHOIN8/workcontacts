from workcontacts.manager import ContactManager
from workcontacts.models.contact import Contact


def test_add_contact():
    manager = ContactManager()

    contact = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com"
    )

    manager.add_contact(contact)

    assert len(manager.contacts) == 1
    assert manager.contacts[0] == contact

def test_find_contact_by_email():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    result = manager.find_by_email("ana@email.com")

    assert result == contact


def test_find_contact_by_email_not_found():
    manager = ContactManager()

    result = manager.find_by_email("missing@email.com")

    assert result is None
    def test_delete_contact_by_email():
        manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    result = manager.delete_by_email("ana@email.com")

    assert result is True
    assert len(manager.contacts) == 0


def test_delete_contact_by_email_not_found():
    manager = ContactManager()

    result = manager.delete_by_email("missing@email.com")

    assert result is False
    assert len(manager.contacts) == 0
def test_delete_contact_by_email():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    result = manager.delete_by_email("ana@email.com")

    assert result is True
    assert len(manager.contacts) == 0
def test_add_contact_with_duplicate_email():
    manager = ContactManager()

    contact1 = Contact("Ana", "Garcia", "ana@email.com")
    contact2 = Contact("Pedro", "Lopez", "ana@email.com")

    manager.add_contact(contact1)

    try:
        manager.add_contact(contact2)
        assert False, "Expected ValueError for duplicate email"
    except ValueError:
        pass

    assert len(manager.contacts) == 1