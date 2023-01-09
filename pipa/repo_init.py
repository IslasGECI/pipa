import os


def repo_init() -> None:
    os.system("template in GitHub")


def change_module_name_in_makefile() -> None:
    os.system("sed --in-place 's/dummy_transformations/pipa/' Makefile")


def change_module_name_in_pyproject() -> None:
    os.system("sed --in-place 's/dummy_transformations/pipa/' pyproject.toml")
