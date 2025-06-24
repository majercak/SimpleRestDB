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
```


### 🔁 Local Hatch Commands

| Command       | Description |
|---------------|-------------|
| `make dev`    | Runs the development server using Hatch (`hatch run dev`). Useful during active development. |
| `make lint`   | Runs code linting with Ruff via Hatch (`hatch run lint`). Ensures code quality and formatting standards. |
| `make format` | Formats code automatically using Ruff (`hatch run format`). Applies safe auto-fixes. |
| `make shell`  | Opens a Hatch-managed virtual environment shell. Lets you run tools manually with dependencies loaded. |

### 🐳 Docker Commands

| Command         | Description |
|------------------|-------------|
| `make build`     | Builds Docker containers using `docker-compose build`. |
| `make up`        | Starts up the application stack in the background (`docker-compose up`). |
| `make down`      | Shuts down all running Docker containers (`docker-compose down`). |
| `make logs`      | Tails the logs from all containers (`docker-compose logs -f`). |
| `make test`      | Runs the test suite inside a clean Docker container (`docker-compose run --rm test`). |
