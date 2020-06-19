# datasette-{{ cookiecutter.hyphenated }}

[![PyPI](https://img.shields.io/pypi/v/datasette-{{ cookiecutter.hyphenated }}.svg)](https://pypi.org/project/datasette-{{ cookiecutter.hyphenated }}/)
{% if cookiecutter.github_username -%}
[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}?label=changelog)](https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/blob/master/LICENSE)

{%- endif %}

{{ cookiecutter.description }}

## Installation

Install this plugin in the same environment as Datasette.

    $ pip install datasette-{{ cookiecutter.hyphenated }}

## Development

TODO: how to pip install -e .[test] etc
