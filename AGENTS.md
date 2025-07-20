# AGENTS.md

## Purpose
This file defines tasks, responsibilities, and guidance for AI agents and contributors working on this repository.

## TODOs for Codex or other AI agents

- [x] Refactor the `MetanameClient` class:
  - Move the `use_test_api` parameter from the `register_domain()` method into the `__init__()` constructor.
  - Store the base API URL in `self.api_url`.
  - Ensure all methods (e.g. `register_domain()`, `check_domain_availability()`) use `self.api_url`.

- [ ] Add a full integration test for domain registration using the Metaname Test API:
  - Create a new test file at `tests/integration/test_register_domain.py`.
  - Load credentials securely using the existing `fetch_op_field()` utility.
  - Use the real test API (`use_test_api=True`) to register a domain (e.g. `"smutest1.nz"`).
  - Construct `ContactDetails`, `PostalAddress`, and `PhoneNumber` using the `metaname_smunz.models` module.
  - Assert that the API result is `{"result": "registered"}` or `"already_registered"`.
  - Mark the test with `@pytest.mark.integration` and consider `@pytest.mark.slow`.

## Notes

- This test **should not** run by default in CI environments. Use markers to isolate it unless explicitly included.

## Style Guidance

- Use clean, minimal method signatures.
- Keep all environment-sensitive logic (e.g. live API endpoints) in the constructor or config layer.
- Follow the existing docstring and type hinting style in `api.py` and `models.py`.
- Integration tests should be placed in `tests/integration/` to distinguish them from fast-running unit tests.
