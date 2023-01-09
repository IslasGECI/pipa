import os
import pipa as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


def test_repo_init(mocker):
    mocker.patch("os.system")
    dt.repo_init()
    os.system.assert_called_once_with("template in GitHub")
