# -*- coding: utf-8 -*-

import sys
from geodefi.exceptions import PythonVersionError


def check_python_version() -> None:
    """Checks that the python version running is sufficient and exits if not."""

    if sys.version_info <= (3, 8) and sys.version_info >= (3, 12):
        raise PythonVersionError(
            f"Python version is not supported.Please consider using 3.8-3.12"
        )
