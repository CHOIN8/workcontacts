
from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    phone: str | None = None
    category: str = "personal"
    notes: str | None = None
    id: int | None = None

