# src/metaname_smunz/api.py

import os
from typing import Dict, Optional

import requests

from .secrets import fetch_op_field
from .models import ContactDetails

class MetanameClient:
    """Simple client for interacting with the Metaname API."""

    def __init__(
        self,
        account_reference: Optional[str] = None,
        api_key: Optional[str] = None,
        item_name: str = "Metaname API Key",
        vault_name: str = "startmeup.nz",
    ) -> None:
        """Initialise the client.

        Credentials can be supplied directly, via environment variables
        ``METANAME_ACCOUNT_REFERENCE`` and ``METANAME_API_KEY``, or loaded from
        1Password using ``item_name`` and ``vault_name``.
        """

        if account_reference is None:
            account_reference = os.getenv("METANAME_ACCOUNT_REFERENCE")
        if api_key is None:
            api_key = os.getenv("METANAME_API_KEY")

        if account_reference is None or api_key is None:
            self.account_reference = fetch_op_field(
                item_name, "account_reference", vault_name
            )
            self.api_key = fetch_op_field(item_name, "credential", vault_name)
        else:
            self.account_reference = account_reference
            self.api_key = api_key

        self.source_ip = self.get_source_ip()

    def get_source_ip(self) -> str:
        try:
            return requests.get("https://icanhazip.com").text.strip()
        except Exception as e:
            raise RuntimeError(f"Failed to get source IP: {e}")

    def check_domain_availability(self, domain: str) -> dict:
        payload = {
            "jsonrpc": "2.0",
            "method": "check_availability",
            "params": [self.account_reference, self.api_key, domain, self.source_ip],
            "id": 1
        }
        try:
            response = requests.post("https://metaname.net/api/1.1", json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise RuntimeError(f"Failed to reach Metaname API or parse response: {e}")

    def register_domain(
        self,
        domain: str,
        term: int,
        contacts: Dict[str, ContactDetails],
        name_servers: Optional[Dict[str, str]] = None,
        use_test_api: bool = True,
    ) -> dict:
        """Register a domain name using the Metaname API."""

        payload = {
            "jsonrpc": "2.0",
            "method": "register_domain_name",
            "params": [
                self.account_reference,
                self.api_key,
                domain,
                term,
                {k: v.to_dict() for k, v in contacts.items()},
                name_servers,
            ],
            "id": 3,
        }

        url = (
            "https://test.metaname.net/api/1.1"
            if use_test_api
            else "https://metaname.net/api/1.1"
        )

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise RuntimeError(f"Failed to reach Metaname API or parse response: {e}")

