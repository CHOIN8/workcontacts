from workcontacts.utils.validators import validate_name, validate_email


def test_validate_name_with_valid_name():
    assert validate_name("Martin") is True


def test_validate_name_with_empty_name():
    assert validate_name("") is False


def test_validate_name_with_spaces():
    assert validate_name("   ") is False


def test_validate_email_with_valid_email():
    assert validate_email("martin@gmail.com") is True


def test_validate_email_without_at():
    assert validate_email("martin.com") is False
def test_validate_email_with_double_at():
    assert validate_email("martin@@gmail.com") is False


def test_validate_email_without_extension():
    assert validate_email("martin@gmail") is False

def test_validate_email_with_empty_domain():
    assert validate_email("martin@") is False

def test_validate_name_with_none():
    assert validate_name(None) is False


def test_validate_name_with_number():
    assert validate_name(123) is False
def test_validate_email_with_none():
    assert validate_email(None) is False


def test_validate_email_with_number():
    assert validate_email(123) is False