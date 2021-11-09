from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


{% set package_datas = [] -%}
{% if cookiecutter.include_static_directory %}{{ package_datas.append('"static/*"') or "" }}{% endif -%}
{% if cookiecutter.include_templates_directory %}{{ package_datas.append('"templates/*"') or "" }}{% endif -%}

setup(
    name="datasette-{{ cookiecutter.hyphenated }}",
    description="{{ cookiecutter.description or "" }}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",{% if cookiecutter.author_name %}
    author="{{ cookiecutter.author_name }}",{% endif %}{% if cookiecutter.github_username %}
    url="https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}",
    project_urls={
        "Issues": "https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/issues",
        "CI": "https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/actions",
        "Changelog": "https://github.com/{{ cookiecutter.github_username }}/datasette-{{ cookiecutter.hyphenated }}/releases",
    },{% endif %}
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_{{ cookiecutter.underscored }}"],
    entry_points={"datasette": ["{{ cookiecutter.underscored }} = datasette_{{ cookiecutter.underscored }}"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},{% if cookiecutter.include_static_directory or cookiecutter.include_templates_directory %}
    package_data={
        "datasette_{{ cookiecutter.underscored }}": [{{ ", ".join(package_datas) }}]
    },{% endif %}
    python_requires=">=3.6",
)
