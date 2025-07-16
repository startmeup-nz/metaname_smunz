# metaname_smunz

DNS as Code Python Module

## Usage Example

```python
from metaname_smunz.api import MetanameClient

client = MetanameClient()
result = client.check_domain_availability("startmeup.nz")
print(result)
```

## Development

Install dev tools:

```
pip install -r requirements-dev.txt
```

Run tests: 

```
pytest
```

Lint code: 

```
ruff check src/ tests/ examples/
```
