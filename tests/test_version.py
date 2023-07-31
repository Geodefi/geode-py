
import pytest
import sys

from pytest import MonkeyPatch
from geode.exceptions import PythonVersionException
from geode.Geode import check_python_version


def test_python_invalid_version_check():
    # Mock sys.version_info to return a specific version (3.6 in this case)
    with pytest.raises(PythonVersionException):
        with pytest.raises(SystemExit):
            with MonkeyPatch.context() as m:
                m.setattr(sys, 'version_info', (3, 6))
                check_python_version()


def test_python_version_check():
    # Mock sys.version_info to return a version greater than 3.7 (e.g., 3.8)
    with MonkeyPatch.context() as m:
        m.setattr(sys, 'version_info', (3, 8))
        check_python_version()
        assert True
