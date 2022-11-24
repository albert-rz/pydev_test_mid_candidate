# -*- coding: utf-8 -*-
"""Exercise 1: Data load."""
import matplotlib.pyplot as plt
from loguru import logger

from . import OUT_DIR
from .utils import load_dataset


def _main():
    logger.info("Starting ex_1")

    # Load dataset
    y = load_dataset()

    # Plot it and save it in OUT_DIR / ex_1.png
    # TODO


if __name__ == "__main__":
    _main()
