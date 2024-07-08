# -*- coding: utf-8 -*-

import pytest
import sys

from pytest import MonkeyPatch
from src.exceptions import PythonVersionError
from src.geodefi import check_python_version


def test_python_invalid_version_check():
    # Mock sys.version_info to return a specific version (3.6 in this case)
    with pytest.raises(PythonVersionError):
        with pytest.raises(SystemExit):
            with MonkeyPatch.context() as m:
                m.setattr(sys, "version_info", (3, 6))
                check_python_version()


def test_python_version_check():
    # Mock sys.version_info to return a version greater than 3.8 (e.g., 3.11)
    with MonkeyPatch.context() as m:
        m.setattr(sys, "version_info", (3, 11))
        check_python_version()
        assert True
