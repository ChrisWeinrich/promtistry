# Promtistry

[![CI](https://github.com/your-org/promtistry/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/promtistry/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Prompt‑Builder Assistant** – iteratively design high‑quality system prompts.

Promtistry is a developer tool for building, evaluating, and iterating on system prompts for LLM-based agents. It provides a framework for defining prompt-building agents, judging their outputs, and automating the process of prompt refinement. The project is strictly typed and enforces code quality via pre-commit hooks and continuous integration.

---

## Quickstart

### 1. Install dependencies

Install all dependencies and set up the environment using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

### 2. Set up pre-commit hooks

Enable code quality checks before each commit:

```bash
poetry run pre-commit install
```

### 3. Run tests

Execute the test suite:

```bash
poetry run pytest
```

### 4. Launch the documentation server

Start a local server to preview the documentation:

```bash
poetry run mkdocs serve
```

Documentation will be available at [http://localhost:8000](http://localhost:8000).

### 5. Build the documentation

Generate static site files for the documentation:

```bash
poetry run mkdocs build
```

---

## Typing & Code Quality

- **Strict typing**: All code is type-checked with `mypy` and linted with `ruff`.
- **Pre-commit hooks**: Formatting and checks are enforced on every commit (`black`, `ruff`, `mypy`, `commitizen`).
- **CI**: All checks and tests are run automatically in GitHub Actions.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
