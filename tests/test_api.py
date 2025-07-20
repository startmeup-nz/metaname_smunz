from metaname_smunz.api import MetanameClient
from metaname_smunz.models import ContactDetails, PhoneNumber, PostalAddress

def test_class_instantiation(monkeypatch):
    def fake_fetch_op_field(item, field, vault):
        return "fake-value"

    def fake_get(url):
        class FakeResponse:
            text = "1.2.3.4"
        return FakeResponse()

    # Patch the function as used inside api.py
    monkeypatch.setattr("metaname_smunz.api.fetch_op_field", fake_fetch_op_field)
    monkeypatch.setattr("metaname_smunz.api.requests.get", fake_get)

    client = MetanameClient()
    assert client.account_reference == "fake-value"
    assert client.api_key == "fake-value"
    assert client.source_ip == "1.2.3.4"

def test_check_domain_availability(monkeypatch):
    def fake_fetch_op_field(item, field, vault):
        return "fake-value"

    def fake_get(url):
        class FakeResponse:
            text = "1.2.3.4"
        return FakeResponse()

    def fake_post(url, json):
        assert url == "https://metaname.net/api/1.1"
        assert json["method"] == "check_availability"
        assert json["params"][2] == "example.nz"  # domain param
        class FakeResponse:
            def raise_for_status(self):
                pass
            def json(self):
                return {"result": "available"}
        return FakeResponse()

    monkeypatch.setattr("metaname_smunz.api.fetch_op_field", fake_fetch_op_field)
    monkeypatch.setattr("metaname_smunz.api.requests.get", fake_get)
    monkeypatch.setattr("metaname_smunz.api.requests.post", fake_post)

    client = MetanameClient()
    result = client.check_domain_availability("example.nz")
    assert result == {"result": "available"}


def test_register_domain(monkeypatch):
    def fake_fetch_op_field(item, field, vault):
        return "fake-value"

    def fake_get(url):
        class FakeResponse:
            text = "1.2.3.4"

        return FakeResponse()

    def fake_post(url, json):
        assert url == "https://test.metaname.net/api/1.1"
        assert json["method"] == "register_domain_name"
        assert json["params"][2] == "example.nz"
        assert json["params"][3] == 12
        class FakeResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"result": "registered"}

        return FakeResponse()

    monkeypatch.setattr("metaname_smunz.api.fetch_op_field", fake_fetch_op_field)
    monkeypatch.setattr("metaname_smunz.api.requests.get", fake_get)
    monkeypatch.setattr("metaname_smunz.api.requests.post", fake_post)

    client = MetanameClient(use_test_api=True)

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

    result = client.register_domain("example.nz", 12, contacts)
    assert result == {"result": "registered"}

