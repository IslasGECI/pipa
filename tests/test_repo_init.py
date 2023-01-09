import os
import pipa as pp


def test_repo_init(mocker):
    mocker.patch("os.system")
    pp.repo_init()
    os.system.assert_called_once_with("template in GitHub")
