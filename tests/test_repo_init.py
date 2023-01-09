import os
import pipa as pp


def test_repo_init(mocker):
    mocker.patch("os.system")
    pp.repo_init()
    os.system.assert_called_once_with("template in GitHub")


def test_modele_name_in_files(mocker):
    mocker.patch("os.system")
    pp.change_module_name_in_makefile()
    os.system.assert_called_with("sed --in-place 's/dummy_transformations/pipa/' Makefile")
    pp.change_module_name_in_pyproject()
    os.system.assert_called_with("sed --in-place 's/dummy_transformations/pipa/' pyproject.toml")
