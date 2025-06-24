# SimpleRestDB
A simple RESTful API in Python with input validation, persistence, and testing
Managed with [Hatch](https://hatch.pypa.io/), leveraging `hatch-requirements-txt` for managing dependencies via `requirements.txt`,
and using [`uv`](https://github.com/astral-sh/uv) for faster package installation.

## 🚀 Features

- Modern Python packaging with `hatch`
- Sync dependencies from `requirements.txt`
- Ultra-fast installs using `uv`
- Config-driven workflows (linting, testing, etc.)

---

## 📦 Installation

### 1. Install dependencies

You need:

- [Python 3.8+](https://www.python.org/downloads/)
- [`hatch`](https://hatch.pypa.io/latest/install/)
- [`uv`](https://github.com/astral-sh/uv)
- Hatch plugin: `hatch-requirements-txt`

```bash
pip install hatch uv hatch-requirements-txt 


## 🐣 Getting Started

### Enter the Hatch shell

```bash
hatch shell
```

This activates the project environment and drops you into an interactive shell with dependencies available. Use it to run tools manually:

```bash
ruff check src/
pytest
```

---

## 🛠 Common Commands

All commands below can be run from **outside the shell** using `hatch run`, or from **within `hatch shell`** directly.

| Task               | Command                                       | Notes                                |
|--------------------|-----------------------------------------------|---------------------------------------|
| Ruff check (lint)  | `hatch run ruff check`                        | Check code formatting                 |
| Ruff fix (safe)    | `hatch run ruff check --fix`                  | Apply safe automatic fixes            |
| Ruff fix (unsafe)  | `hatch run ruff check --fix --unsafe-fixes`   | Apply all fixes (including unsafe)    |
| Show Ruff version  | `hatch run ruff --version`                    | Verify Ruff installation              |
| Run tests          | `hatch run test`                              | Run your test suite (e.g. `pytest`)   |

---