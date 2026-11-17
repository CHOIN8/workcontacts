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


def test_update_contact_phone():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    result = manager.update_contact(
        "ana@email.com",
        phone="600123456"
    )

    assert result is True
    assert contact.phone == "600123456"


def update_contact(self, current_email: str, **kwargs):
    contact = self.find_by_email(current_email)

    if contact is None:
        return False

    for field, value in kwargs.items():
        if hasattr(contact, field):
            setattr(contact, field, value)

    return True
def test_update_contact_email():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    result = manager.update_contact(
        "ana@email.com",
        email="ana.nuevo@email.com"
    )

    assert result is True
    assert contact.email == "ana.nuevo@email.com"
    assert manager.find_by_email("ana.nuevo@email.com") == contact
        
    def test_update_contact_email_duplicate():
        manager = ContactManager()

    contact1 = Contact("Ana", "Garcia", "ana@email.com")
    contact2 = Contact("Pedro", "Lopez", "pedro@email.com")

    manager.add_contact(contact1)
    manager.add_contact(contact2)

    try:
        manager.update_contact(
            "ana@email.com",
            email="pedro@email.com"
        )
        assert False, "Expected ValueError for duplicate email"
    except ValueError:
        pass

    assert contact1.email == "ana@email.com"
