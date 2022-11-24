# -*- coding: utf-8 -*-
"""Top level package for pydev_test_mid."""
from pathlib import Path

__version__ = "0.1.0"


# Base path of nvs_ex module
# (to be used when accessing non .py files in pydev_test_mid/)
WORKSPACE = Path(__file__).parent.parent
ASSETS_DIR = WORKSPACE / "assets"
OUT_DIR = WORKSPACE / "out"
