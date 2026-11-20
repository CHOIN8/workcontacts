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
def test_update_contact_cannot_change_id():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    contact.id = 1

    result = manager.update_contact(
        "ana@email.com",
        id=99
    )

    assert result is True
    assert contact.id == 1
def test_update_contact_invalid_email():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    try:
        manager.update_contact(
            "ana@email.com",
            email="esto-no-es-un-email"
        )
        assert False, "Expected ValueError for invalid email"
    except ValueError:
        pass

    assert contact.email == "ana@email.com"
def test_update_contact_invalid_first_name():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    try:
        manager.update_contact(
            "ana@email.com",
            first_name=""
        )
        assert False, "Expected ValueError for invalid first name"
    except ValueError:
        pass

    assert contact.first_name == "Ana"


def test_update_contact_invalid_last_name():
    manager = ContactManager()

    contact = Contact("Ana", "Garcia", "ana@email.com")
    manager.add_contact(contact)

    try:
        manager.update_contact(
            "ana@email.com",
            last_name=""
        )
        assert False, "Expected ValueError for invalid last name"
    except ValueError:
        pass

    assert contact.last_name == "Garcia"

def test_filter_by_category():
    manager = ContactManager()

    personal = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        category="personal"
    )

    work = Contact(
        first_name="Carlos",
        last_name="Lopez",
        email="carlos@email.com",
        category="work"
    )

    manager.add_contact(personal)
    manager.add_contact(work)

    results = manager.filter_by_category("personal")

    assert len(results) == 1
    assert results[0].first_name == "Ana"
    assert results[0].category == "personal"

def test_filter_by_category_ignores_case():
    manager = ContactManager()

    contact = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        category="personal"
    )

    manager.add_contact(contact)

    results = manager.filter_by_category("PERSONAL")

    assert len(results) == 1
    assert results[0] == contact

def test_get_statistics():
    manager = ContactManager()

    manager.add_contact(Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        category="personal",
        phone="600123456"
    ))

    manager.add_contact(Contact(
        first_name="Carlos",
        last_name="Lopez",
        email="carlos@email.com",
        category="work",
        phone="600987654"
    ))

    stats = manager.get_statistics()

    assert stats["total"] == 2
    assert stats["personal"] == 1
    assert stats["work"] == 1
    assert stats["without_phone"] == 0

def test_get_statistics_without_phone():
    manager = ContactManager()

    contact1 = Contact(
        first_name="Ana",
        last_name="Garcia",
        email="ana@email.com",
        category="personal",
        phone="600123456"
    )

    contact2 = Contact(
        first_name="Carlos",
        last_name="Lopez",
        email="carlos@email.com",
        category="work"
    )

    contact3 = Contact(
        first_name="Pedro",
        last_name="Alonso",
        email="pedro@email.com",
        category="personal"
    )

    manager.add_contact(contact1)
    manager.add_contact(contact2)
    manager.add_contact(contact3)

    stats = manager.get_statistics()

    assert stats["total"] == 3
    assert stats["without_phone"] == 2
