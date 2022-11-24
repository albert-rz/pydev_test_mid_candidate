# -*- coding: utf-8 -*-
"""Exercise 3: SlidingBacktest in background."""
import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger
from sktime.forecasting.fbprophet import Prophet

from . import OUT_DIR

# from .forecasting import SlidingBacktest
from .utils import load_dataset


def _main():
    global _lock

    logger.info("Starting ex_3")

    # Load dataset
    y = load_dataset()

    # Do a backtest on the loaded dataset using SlidingBacktest in background
    # TODO

    # Combine y and y_pred into one dataframe
    res = pd.DataFrame()
    logger.info("Backtest result\n{}", res)

    # Plot result and save it in OUT_DIR / ex_3.png
    # TODO


if __name__ == "__main__":
    _main()
