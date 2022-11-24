# -*- coding: utf-8 -*-
"""Helper functions."""
import pandas as pd
from loguru import logger

from . import ASSETS_DIR


def load_dataset() -> pd.DataFrame:
    sources = [
        ASSETS_DIR / "BTC-2018min.csv",
        ASSETS_DIR / "BTC-2019min.csv",
    ]

    # Load dataset from sources
    # TODO

    # Sort in ascending order
    # TODO

    # Check nulls
    # TODO

    # Resample to day
    # TODO

    return pd.DataFrame()
