# Aider Coding Instructions (read‑only)

Whenever Aider generates or modifies **any** code in this repository, it **must**:

1. ✅ **Pass Ruff** according to the repository's configuration.
2. ✅ **Pass MyPy** with the project's strict settings.
3. ✅ Prefer **type annotations everywhere**. All public functions, methods, and variables **must** be fully typed.  
   *No `Any` unless absolutely unavoidable.*
4. ✅ Use **dataclasses** or **pydantic models** where appropriate, instead of bare dicts or tuples.
5. ✅ Do **not** relax linter or type checker rules globally; fix the underlying code instead.
6. ✅ Always use **Poetry** for dependency management and packaging. Use `poetry add` to add dependencies, and ensure to run `poetry lock` before any installation operations. Before every commit, run `poetry run pre-commit run --all-files`.
7. ✅ Keep code **idiomatic, minimal, and explicit** – follow Python best practices.
7. ✅ Every new public API must include **docstrings** describing inputs and outputs.

---

## 🎯 **Project Goal**

Build a **Prompt‑Builder Assistant** that helps you iteratively design high‑quality **system prompts**.

The assistant itself runs locally in **Streamlit**, is implemented using **LangChain** for LLM calls and **LangGraph** for orchestration, and saves final versions as Markdown files committed to **Git**.

---

## 🧭 **How It Works (User Workflow)**

1. **Start a chat**
   In a Streamlit UI you chat with a “Builder Agent.”

   * You tell it what kind of system prompt you want (e.g. *“I need a system prompt for a Python code reviewer.”*)
   * The agent responds with a first draft.

2. **Iterate**
   You refine the draft interactively by continuing the chat:
   *“Add more instructions about style”* → Builder updates the draft.
   *“Include examples”* → Builder updates again.

3. **Judge & Feedback**
   When you click **Evaluate**, the system sends the current draft to a **Judge Agent**.

   * The Judge scores it (e.g. 1–5) and explains what’s missing or unclear.
   * If the score is below your threshold, you go back to step 2.

4. **Save to Git**
   When the Judge score is good enough, click **Save**.

   * The current draft is written to a Markdown file (with front‑matter: title, date, score).
   * A local Git commit is created (`git add` + `git commit`).

---

## ⚙️ **Tech Stack**

| Component              | Technology                      | Purpose                                                                 |
| ---------------------- | ------------------------------- | ----------------------------------------------------------------------- |
| **Builder Agent**      | LangChain (e.g. `ChatOpenAI`)   | Generates and refines the system prompt.                                |
| **Judge Agent**        | LangChain (another model)       | Evaluates quality, returns a score and critique.                        |
| **Flow Orchestration** | LangGraph                       | Defines a simple graph: `Builder → Judge → (revise loop or save node)`. |
| **Frontend**           | Streamlit                       | Simple chat interface + preview panel + “Evaluate” and “Save” buttons.  |
| **Storage**            | Git repository (Markdown files) | Stores final versions, no DB or cache needed.                           |

---

## ✨ **Key Features**

✅ **Pure chat interface** (no database)
✅ **Builder → Judge loop** (via LangGraph)
✅ **Markdown + Git versioning**
✅ **Self‑hosted, BYO OpenAI key**
✅ **Easily extendable later** (add DB, templates, etc.)

---

### 🔮 **Future Extensions (optional)**

* Add templates for common prompt types.
* Introduce a database (Postgres, etc.) for metadata & search.
* Push commits automatically to GitHub.
* Multiple Judge nodes for different criteria (clarity, style, bias).

---

**In short:**
👉 *A local Streamlit app where you chat with a Builder agent (LangChain) orchestrated via LangGraph. A Judge agent scores your draft. Once satisfied, you save the system prompt into a Git repo as Markdown.*

