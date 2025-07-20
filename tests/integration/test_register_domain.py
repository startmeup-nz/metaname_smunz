import pytest

from metaname_smunz import MetanameClient, ContactDetails, PhoneNumber, PostalAddress
from metaname_smunz.secrets import fetch_op_field, SecretFetchError


@pytest.mark.integration
@pytest.mark.slow
def test_register_domain_integration():
    """Register a domain using the real Metaname test API."""
    try:
        account_reference = fetch_op_field("Metaname API Key", "account_reference", "startmeup.nz")
        api_key = fetch_op_field("Metaname API Key", "credential", "startmeup.nz")
    except SecretFetchError:
        pytest.skip("Unable to load Metaname credentials from 1Password")

    client = MetanameClient(
        account_reference=account_reference,
        api_key=api_key,
        use_test_api=True,
    )

    address = PostalAddress(
        line1="123 Test Street",
        line2=None,
        city="Wellington",
        region=None,
        postal_code="6011",
        country_code="NZ",
    )

    phone = PhoneNumber(country_code="64", area_code="21", local_number="2345678")

    contact = ContactDetails(
        name="Meta Test",
        email_address="test@example.com",
        organisation_name=None,
        postal_address=address,
        phone_number=phone,
    )

    contacts = {"registrant": contact, "admin": contact, "technical": contact}

    result = client.register_domain("smutest1.nz", 12, contacts)
    assert result.get("result") in {"registered", "already_registered"}
