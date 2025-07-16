# src/metaname_smunz/api.py

import requests
from .secrets import fetch_op_field

class MetanameClient:
    def __init__(self, item_name: str = "Metaname API Key", vault_name: str = "startmeup.nz"):
        self.account_reference = fetch_op_field(item_name, "account_reference", vault_name)
        self.api_key = fetch_op_field(item_name, "credential", vault_name)
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
