# Smell

A static code analysis tool for detecting code smells in your codebase.

## Installation

To install `smell` globally, you need Python >= 3.13. If you have Poetry and a project repository, you can build and install the wheel:

```bash
cd /path/to/smell
python3 -m venv .venv
source .venv/bin/activate
pip install poetry
poetry build
pip install dist/smell-*.whl
deactivate
```

## Usage

Display the version:
```bash
smell -v
# or
smell --version
# or
smell version
```

Display help:
```bash
smell -h
# or
smell --help
```

Analyze a Git branch for file statistics:
```bash
smell analyze --branch main
```

## Development

### Prerequisites

- Python >= 3.13
- Poetry for dependency management
- Git for version control

### Setup

Clone the repository and set up a virtual environment:

```bash
git clone <repository-url>
cd smell
python3 -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --with dev
```

### Run Tests

Run the test suite to verify functionality:

```bash
poetry run pytest
```

### Build the Project

Build the source distribution and wheel:

```bash
poetry build
```

### Project Structure

```
smell/
├── smell/
│   ├── __init__.py
│   ├── cli.py
│   └── version.py
├── tests/
│   ├── __init__.py
│   └── test_cli.py
├── pyproject.toml
├── Poetry.lock
├── README.md
├── .gitignore
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue on the repository.

## License

MIT License