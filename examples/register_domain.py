"""Example: Register a domain using the Metaname test API."""

from metaname_smunz import (
    ContactDetails,
    MetanameClient,
    PhoneNumber,
    PostalAddress,
)

client = MetanameClient(use_test_api=True)

base_contact = ContactDetails(
    name="Meta Test",
    email_address="test@example.com",
    organisation_name=None,
    postal_address=PostalAddress(
        line1="123 Test Street",
        line2=None,
        city="Wellington",
        region=None,
        postal_code="6011",
        country_code="NZ",
    ),
    phone_number=PhoneNumber(country_code="64", area_code="21", local_number="2345678"),
)

contacts = {"registrant": base_contact, "admin": base_contact, "technical": base_contact}

result = client.register_domain("example-test.nz", 12, contacts)
print(result)

