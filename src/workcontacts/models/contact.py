
from dataclasses import dataclass
from workcontacts.utils.validators import validate_name, validate_email


@dataclass
class Contact:
    first_name: str
    last_name: str  
    email: str
    phone: str | None = None
    category: str = "personal"
    notes: str | None = None
    id: int | None = None

    def __post_init__(self):
        if not validate_name(self.first_name):
            raise ValueError("First name cannot be empty or invalid")

        if not validate_name(self.last_name):
         raise ValueError("Last name cannot be empty or invalid")

        if not validate_email(self.email):
            raise ValueError("Email address is invalid")


