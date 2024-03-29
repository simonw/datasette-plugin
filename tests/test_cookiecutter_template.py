from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_static_and_templates(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "foo",
            "description": "blah",
            "include_templates_directory": "y",
            "include_static_directory": "y",
        },
    )
    assert paths(tmpdir) == {
        "datasette-foo",
        "datasette-foo/.github",
        "datasette-foo/.github/workflows",
        "datasette-foo/.github/workflows/publish.yml",
        "datasette-foo/.github/workflows/test.yml",
        "datasette-foo/.gitignore",
        "datasette-foo/datasette_foo",
        "datasette-foo/datasette_foo/__init__.py",
        "datasette-foo/datasette_foo/static",
        "datasette-foo/datasette_foo/templates",
        "datasette-foo/README.md",
        "datasette-foo/LICENSE",
        "datasette-foo/pyproject.toml",
        "datasette-foo/tests",
        "datasette-foo/tests/test_foo.py",
    }
    assert (
        "[tool.setuptools.package-data]\n" 'datasette_foo = ["static/*", "templates/*"]'
    ) in read_pyproject_toml(tmpdir)


def test_no_static_or_templates(tmpdir):
    generate(tmpdir, {"plugin_name": "foo", "description": "blah"})
    assert "datasette-foo/datasette_foo/static" not in paths(tmpdir)
    assert "datasette-foo/datasette_foo/templates" not in paths(tmpdir)
    assert "[tools.setuptools.package-data]" not in read_pyproject_toml(tmpdir)


def test_static_but_no_templates(tmpdir):
    generate(
        tmpdir,
        {"plugin_name": "foo", "description": "blah", "include_static_directory": "y"},
    )
    assert "datasette-foo/datasette_foo/static" in paths(tmpdir)
    assert "datasette-foo/datasette_foo/templates" not in paths(tmpdir)
    assert (
        "[tool.setuptools.package-data]\n" 'datasette_foo = ["static/*"]'
    ) in read_pyproject_toml(tmpdir)


def test_templates_but_no_static(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "foo",
            "description": "blah",
            "include_templates_directory": "y",
        },
    )
    assert "datasette-foo/datasette_foo/static" not in paths(tmpdir)
    assert "datasette-foo/datasette_foo/templates" in paths(tmpdir)
    assert (
        "[tool.setuptools.package-data]\n" 'datasette_foo = ["templates/*"]'
    ) in read_pyproject_toml(tmpdir)


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def read_pyproject_toml(tmpdir):
    return (tmpdir / "datasette-foo" / "pyproject.toml").read_text("utf-8")


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
