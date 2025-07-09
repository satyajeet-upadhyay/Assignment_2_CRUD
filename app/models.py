from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated

PhoneNumber = Annotated[str, StringConstraints(pattern=r'^\d{10}$')]
NameType = Annotated[str, StringConstraints(pattern=r'^[A-Za-z ]+$')]

class User(BaseModel):
    name: NameType
    phone: PhoneNumber
    @field_validator("name")
    def validate_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Please enter a valid name.")
        return value
