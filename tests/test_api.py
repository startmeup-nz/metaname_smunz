from metaname_smunz.api import MetanameClient

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
