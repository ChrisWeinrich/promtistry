# Promtistry

[![CI](https://github.com/your-org/promtistry/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/promtistry/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Prompt‑Builder Assistant** – A comprehensive tool for designing and refining high‑quality system prompts for language model-based agents.

Promtistry is a powerful developer tool designed to streamline the process of creating, evaluating, and iterating on system prompts for language model-based agents. It offers a robust framework for defining prompt-building agents, assessing their outputs, and automating prompt refinement. The project emphasizes code quality and maintainability through strict typing, pre-commit hooks, and continuous integration.

### Key Features
- **Prompt Building**: Define and refine prompts for language model-based agents.
- **Automated Evaluation**: Use built-in judge agents to assess prompt quality.
- **Iterative Design**: Continuously improve prompts through automated feedback loops.
- **Code Quality**: Enforced through strict typing, linting, and pre-commit hooks.
- **Comprehensive Documentation**: Easily accessible and well-documented codebase.

---

## Architecture

The Promtistry project is structured to facilitate the development and evaluation of system prompts for language model-based agents. Below is an overview of the main components:

- **Agents**: The core of the system, consisting of `ChatAgent` instances that interact with language models. These agents are responsible for generating and evaluating prompts.
  
- **Flow**: Managed by `StateGraph`, the flow defines the sequence of operations, including the invocation of agents and handling of user inputs. The flow is designed to be flexible and extensible, allowing for easy integration of new nodes and logic.

- **State Management**: Utilizes the `ChatState` dataclass to maintain the state of interactions. This state is immutable and updated through defined methods, ensuring consistency and reliability.

- **UI**: Built with Streamlit, the user interface provides an interactive platform for users to engage with the agents. It displays conversation history and allows users to input messages and receive responses.

- **Configuration**: Managed by `ConfigService`, which loads settings from environment variables and prompt files. This service ensures that all components have access to the necessary configuration data.

- **Documentation**: Comprehensive documentation is generated using MkDocs, providing users with detailed information on setup, usage, and development.

This architecture is designed to be modular and scalable, supporting the addition of new features and components as needed.

## Quickstart

### Quickstart

#### 1. Install Dependencies

Set up your environment and install all necessary dependencies using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

#### 2. Set Up Pre-commit Hooks

Enable automatic code quality checks before each commit to maintain high standards:

```bash
poetry run pre-commit install
```

#### 3. Run Tests

Execute the comprehensive test suite to ensure everything is working correctly:

```bash
poetry run pytest
```

#### 4. Launch the Documentation Server

Start a local server to preview the project's documentation:

```bash
poetry run mkdocs serve
```

Documentation will be available at [http://localhost:8000](http://localhost:8000).

#### 5. Build the Documentation

Generate static site files for the documentation to share or deploy:

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
