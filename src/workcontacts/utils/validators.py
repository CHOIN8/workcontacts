import re
def validate_name(name: str) -> bool:
    if not isinstance(name, str):
        return False

    if not name.strip():
        return False

    return True


def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.fullmatch(pattern, email) is not None

    if "@" not in email:
        return False

    if "." not in email.split("@")[-1]:
        return False

    return True