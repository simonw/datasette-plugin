# datasette-{{ cookiecutter.hyphenated }}

[![PyPI](https://img.shields.io/pypi/v/datasette-{{ cookiecutter.hyphenated }}.svg)](https://pypi.org/project/datasette-{{ cookiecutter.hyphenated }}/){% if cookiecutter.github_username %}
[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/releases)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/blob/main/LICENSE){% endif %}

{{ cookiecutter.description or "" }}

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-{{ cookiecutter.hyphenated }}
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-{{ cookiecutter.hyphenated }}
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
