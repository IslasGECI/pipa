import os


def repo_init() -> None:
    os.system("template in GitHub")


def change_module_name_in_makefile() -> None:
    change_module_name_in_file("Makefile")


def change_module_name_in_pyproject() -> None:
    change_module_name_in_file("pyproject.toml")


def change_module_name_in_tests() -> None:
    change_module_name_in_file("tests/test_transformations.py")


def change_module_name_in_actions() -> None:
    change_module_name_in_file(".github/workflows/develop.yml")


def change_module_name_in_file(filename: str) -> None:
    command = f"sed --in-place 's/dummy_transformations/pipa/' {filename}"
    os.system(command)
