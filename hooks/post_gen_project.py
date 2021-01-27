import os
import shutil


include_static_directory = bool("{{ cookiecutter.include_static_directory }}")
include_templates_directory = bool("{{ cookiecutter.include_templates_directory }}")


print(os.getcwd())


if not include_static_directory:
    shutil.rmtree(
        os.path.join(
            os.getcwd(),
            "datasette_{{ cookiecutter.underscored }}",
            "static",
        )
    )


if not include_templates_directory:
    shutil.rmtree(
        os.path.join(
            os.getcwd(),
            "datasette_{{ cookiecutter.underscored }}",
            "templates",
        )
    )
