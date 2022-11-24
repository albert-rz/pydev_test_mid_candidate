# -*- coding: utf-8 -*-
"""Exercise 4: SlidingBacktest as a service."""
import pandas as pd
from flask import Flask
from loguru import logger
from sktime.forecasting.fbprophet import Prophet

# from .forecasting import SlidingBacktest
from .utils import load_dataset

app = Flask(__name__)


@app.route("/")
def hello_world():
    logger.info("hello_world request")
    return "Hello world"


@app.route("/backtest")
def bkt_in_back():
    logger.info("bkt_in_back request")
    # Implement the service as defined in openapi.yml
    # TODO

    return "Please delete this line"
