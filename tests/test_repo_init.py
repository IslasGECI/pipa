import os
import geci_pipa as pp


def test_repo_init(mocker):
    mocker.patch("os.system")
    pp.repo_init()
    os.system.assert_called_once_with("template in GitHub")


def test_modele_name_in_files(mocker):
    mocker.patch("os.system")
    pp.change_module_name_in_makefile()
    assert_called_os_system_with_file("Makefile")
    pp.change_module_name_in_pyproject()
    assert_called_os_system_with_file("pyproject.toml")
    pp.change_module_name_in_tests()
    assert_called_os_system_with_file("tests/test_transformations.py")
    pp.change_module_name_in_actions()
    assert_called_os_system_with_file(".github/workflows/develop.yml")


def assert_called_os_system_with_file(file_name):
    command = f"sed --in-place 's/dummy_transformations/pipa/' {file_name}"
    os.system.assert_called_with(command)
