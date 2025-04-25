# Smell

A static code analysis tool for detecting code smells in your codebase.

## Installation

To install `smell` globally, build and install the wheel:

```bash
poetry build
pip install dist/smell-0.1.0-py3-none-any.whl
```

Ensure the Python environment's `bin/` directory is in your `PATH`. For example, if using `pyenv` with Python 3.13.3:

```bash
echo 'export PATH="$HOME/.pyenv/versions/3.13.3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
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

## Development

### Prerequisites

- Python >= 3.13
- Poetry for dependency management

### Setup

Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd smell
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
├── README.md
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue on the repository.

## License

MIT License