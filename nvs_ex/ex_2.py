# -*- coding: utf-8 -*-
"""Exercise 2: SlidingBacktest in parallel."""
import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger
from sktime.forecasting.fbprophet import Prophet

from . import OUT_DIR

# from .forecasting import SlidingBacktest
from .utils import load_dataset


def _main():
    logger.info("Starting ex_2")

    # Load dataset
    y = load_dataset()

    # Do a backtest on the loaded dataset using SlidingBacktest
    # TODO: once implemented the class, uncomment the lines below
    # logger.info("Starting SlidingBacktest")
    # bkt = SlidingBacktest(forecaster=Prophet(), fh=[1], window_length=100, n_jobs=10)
    # y_pred = bkt.backtest(y)

    # Combine y and y_pred into one dataframe
    res = pd.DataFrame()
    logger.info("Backtest result\n{}", res)

    # Plot result and save it in OUT_DIR / ex_2.png
    # TODO


if __name__ == "__main__":
    _main()
