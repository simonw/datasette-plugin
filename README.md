# datasette-plugin cookiecutter template

A cookiecutter template for creating new Datasette plugins.

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

This will create a directory called `datasette-plugin-template-demo` - the plugin name you enter is converted to lowercase and uses hyphens instead of spaces.

See https://github.com/simonw/datasette-plugin-template-demo for the output of this example.

## Creating a Git repository for your plugin

Having created your new plugin template, you can initialize a Git repository for it like this:

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

The template will have created GitHub Actions which run your plugin's test suite for you.
