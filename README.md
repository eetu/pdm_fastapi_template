# pdm-fastapi-template

A modern FastAPI project template using PDM for dependency management. This template provides a clean project structure with routes, models, tests, and best practices configured out of the box.

## Features

- ⚡ FastAPI web framework
- 📦 PDM for dependency management
- 🧪 pytest for testing with async support
- 🎨 Black for code formatting
- ✅ pylint for code linting
- 🔧 Pydantic Settings for environment configuration
- 🔥 Hot reload with watchfiles
- 📁 Clean modular structure with separate routes and models

## Prerequisites

- Python 3.13
- PDM (Python Development Master)
- pyenv (recommended for Python version management)

## Installation

### 1. Setup Python Environment

Install pyenv and Python 3.13:

```bash
brew install pyenv
```

Configure pyenv for your shell. For example, with Fish shell, add to `~/.config/fish/config.fish`:

```bash
pyenv init - | source
```

For Bash/Zsh, add to `~/.bashrc` or `~/.zshrc`:

```bash
eval "$(pyenv init -)"
```

Install Python and PDM:

```bash
pyenv install 3.13
pyenv global 3.13
pip install pdm
```

### 2. Install Project Dependencies

```bash
pdm install
```

### 3. Configure Environment Variables

Copy the example environment file and customize it:

```bash
cp .env.example .env
```

Edit `.env` and set your desired values:

```env
MESSAGE="Hello from my API!"
```

## Usage

### Development Server

Run the application in development mode with hot reload:

```bash
pdm run dev
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs

### Example Request

```bash
curl http://localhost:8000/
```

Response:

```json
{
  "message": "Hello from my API!"
}
```

## Development

### Run Tests

```bash
pdm run test
```

### Run Linters

```bash
pdm run lint
```

This runs both Black and pylint checks.

### Format Code

```bash
pdm run format
```

## Project Structure

```
src/
├── main.py              # FastAPI application entry point
├── settings.py          # Application settings using Pydantic
├── models/              # Pydantic models
│   ├── __init__.py
│   ├── message.py
│   └── test_message.py
├── routes/              # API route handlers
│   ├── __init__.py
│   ├── root.py
│   └── test_root.py
└── test_main.py         # Main application tests
```

## Available Commands

All commands are defined in `pyproject.toml`:

- `pdm run dev` - Start development server with hot reload
- `pdm run test` - Run all tests
- `pdm run lint` - Run linting (Black + pylint)
- `pdm run format` - Format code with Black

## License

MIT
