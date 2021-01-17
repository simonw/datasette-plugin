# datasette-plugin cookiecutter template

A cookiecutter template for creating new Datasette plugins. See [Writing Plugins](https://docs.datasette.io/en/stable/writing_plugins.html) in the Datasette documentation for more details.

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:

    pipx install cookiecutter

Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:simonw/datasette-plugin` and then answer the prompts. Here's an example run:

    $ cookiecutter gh:simonw/datasette-plugin
    plugin_name []: plugin template demo
    description []: Demonstrating https://github.com/simonw/datasette-plugin
    hyphenated [plugin-template-demo]: 
    underscored [plugin_template_demo]: 
    github_username []: simonw
    author_name []: Simon Willison

I strongly recommend accepting the suggested value for "hyphenated" and "underscored" by hitting enter on those prompts.

This will create a directory called `datasette-plugin-template-demo` - the plugin name you enter is converted to lowercase and uses hyphens instead of spaces.

See https://github.com/simonw/datasette-plugin-template-demo for the output of this example.

## Developing your plugin

Having created the new plugin structure from the template, here's how to start working on the plugin.

If your plugin is called `datasette-my-new-plugin`, you can start working on it like so:

    cd datasette-my-new-plugin
    # Create and activate a virtual environment:
    python3 -mvenv venv
    source venv/bin/activate
    # Install dependencies so you can edit the plugin:
    pip install -e '.[test]'
    # With zsh you have to run this again for some reason:
    source venv/bin/activate
    # Confirm your plugin is visible to Datasette:
    datasette plugins

You should see the following:

    [
        {
            "name": "datasette-my-new-plugin",
            "static": false,
            "templates": false,
            "version": "0.1",
            "hooks": []
        }
    ]

You can run the default test for your plugin like so:

    pytest

This will execute the test in `tests/test_my_new_plugin.py`, which confirms that the plugin has been installed.

Now you can open the `datasette_my_new_plugin/__init__.py` file and start adding your [plugin hooks](https://docs.datasette.io/en/stable/plugin_hooks.html).

## Creating a Git repository for your plugin

You can initialize a Git repository for your plugin like this:

    cd datasette-my-new-plugin
    git init
    git add .
    git commit -m "Initial structure from template"
    # Rename the 'master' branch to 'main':
    git branch -m master main

## Publishing your plugin to GitHub

Use https://github.com/new to create a new GitHub repository sharing the same name as your plugin, which should be something like `datasette-my-new-plugin`.

Push your `main` branch to GitHub like this:

    git remote add origin git@github.com:YOURNAME/datasette-my-new-plugin.git
    git push -u origin main

The template will have created a GitHub Action which runs your plugin's test suite against every commit.

## Publishing your plugin as a package to PyPI

The template also includes an Action for publishing packages to [PyPI](https://pypi.org/).

To use this action, you need to create a PyPI account and an API token against that account.

Once you have created your account, navigate to https://pypi.org/manage/account/token/ and create an API token. For initial publication of the package you will need to set the scope of the token to "Entire account (all projects)".

Add that token to your repository as a GitHub secret called `PYPI_TOKEN`. You can find this in the "Settings -> Secrets -> New Secret" area of the repository. The token should begin with the string `pypi-`.

Now, any time you create a new "Release" on GitHub the Action will build your package and push it to PyPI. The tag for the new release needs to match the `VERSION` string at the top of your `setup.py` file.

After the first release has gone out you can create a new PyPI API token that is scoped just to that project and use that to replace the `PYPI_TOKEN` secret in your GitHub repository settings.
