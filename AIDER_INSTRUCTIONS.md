# Aider Coding Instructions (read‑only)

Whenever Aider generates or modifies **any** code in this repository, it **must**:

1. ✅ **Pass Ruff** according to the repository's configuration.
2. ✅ **Pass MyPy** with the project's strict settings.
3. ✅ Prefer **type annotations everywhere**. All public functions, methods, and variables **must** be fully typed.  
   *No `Any` unless absolutely unavoidable.*
4. ✅ Use **dataclasses** or **pydantic models** where appropriate, instead of bare dicts or tuples.
5. ✅ Do **not** relax linter or type checker rules globally; fix the underlying code instead.
6. ✅ Keep code **idiomatic, minimal, and explicit** – follow Python best practices.
7. ✅ Every new public API must include **docstrings** describing inputs and outputs.

---

**Remember:**  
Every commit from Aider should already **pass all checks** (`ruff`, `mypy`, `pytest`, `pre-commit`) before finishing.
