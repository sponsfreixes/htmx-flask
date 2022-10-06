# Flask-htmx

TBD

## Install

It's just `pip install flask-htmx` and you're all set. It's a pure Python package
that only needs `flask` (for obvious reasons!).

## Usage

This is an example of how to use the library 

TBD

## How to contribute

This project uses pre-commit hooks to run black, isort, pyupgrade and flake8 on each commit. To have that running
automatically on your environment, install the project with:

```shell
pip install -e .[dev]
```

And then run once:

```shell
pre-commit install
```

From now one, every time you commit your files on this project, they will be automatically processed by the tools listed
above.

## How to run tests

You can install pytest and other required dependencies with:

```shell
pip install -e .[tests]
```

And then run the test suite with:

```shell
pytest
```

