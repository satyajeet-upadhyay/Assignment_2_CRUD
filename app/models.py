from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated

# Phone number → exactly 10 digits, only numbers allowed
PhoneNumber = Annotated[str, StringConstraints(pattern=r'^\d{10}$')]

# Name → only alphabets, optional spaces allowed (e.g., "Satyajet Kumar")
NameType = Annotated[str, StringConstraints(pattern=r'^[A-Za-z ]+$')]

class User(BaseModel):
    name: NameType
    phone: PhoneNumber

    @field_validator("name")
    def validate_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Please enter a valid name.")
        return value
