# src/metaname_smunz/secrets.py

import subprocess

class SecretFetchError(Exception):
    pass

def fetch_op_field(item: str, field: str, vault: str) -> str:
    try:
        return subprocess.check_output([
            "op", "item", "get", item,
            "--vault", vault,
            "--field", field,
            "--reveal"
        ]).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        raise SecretFetchError(f"Failed to fetch '{field}' from 1Password item '{item}': {e}")
