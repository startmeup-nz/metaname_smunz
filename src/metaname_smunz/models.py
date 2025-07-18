from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class PostalAddress:
    line1: str
    line2: Optional[str]
    city: str
    region: Optional[str]
    postal_code: str
    country_code: str


@dataclass
class PhoneNumber:
    country_code: str
    area_code: str
    local_number: str


@dataclass
class ContactDetails:
    name: str
    email_address: str
    organisation_name: Optional[str]
    postal_address: PostalAddress
    phone_number: PhoneNumber
    fax_number: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email_address": self.email_address,
            "organisation_name": self.organisation_name,
            "postal_address": asdict(self.postal_address),
            "phone_number": asdict(self.phone_number),
            "fax_number": self.fax_number,
        }

