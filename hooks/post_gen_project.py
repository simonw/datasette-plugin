import os
import shutil


include_static_directory = bool("{{ cookiecutter.include_static_directory }}")
include_templates_directory = bool("{{ cookiecutter.include_templates_directory }}")


if include_static_directory:
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "datasette_{{ cookiecutter.underscored }}",
            "static",
        )
    )


if include_templates_directory:
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "datasette_{{ cookiecutter.underscored }}",
            "templates",
        )
    )
