# AGENTS.md

## Purpose
This file defines tasks, responsibilities, and guidance for AI agents and contributors working on this repository.

## TODOs for Codex or other AI agents

- [ ] Refactor the `MetanameClient` class:
  - Move the `use_test_api` parameter from the `register_domain()` method into the `__init__()` constructor.
  - Store the base API URL in `self.api_url`.
  - Ensure all methods (e.g. `register_domain()`, `check_domain_availability()`) use `self.api_url`.

## Notes

- The current branch implementing domain registration is `codex/add-test-domain-registration-feature`.
- The test `test_register_domain_with_real_api()` should remain compatible and use `use_test_api=True` during client initialization.
- See the GitHub PR comment for additional context and rationale for this change.

## Style Guidance
- Keep method signatures clean — avoid repeating config flags if they apply globally.
- Follow existing docstring style in `api.py`.
