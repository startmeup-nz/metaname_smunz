# examples/check_domain.py

"""
Example: Check domain availability with Metaname API.
"""

from metaname_smunz.api import MetanameClient

client = MetanameClient()
result = client.check_domain_availability("startmeup.nz")
print(result)
