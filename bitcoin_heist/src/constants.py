"""Hold default values."""
import logging

LOGGING_LEVEL = logging.INFO
DATASET_ATTRS = (
    # "address",  ## Drop address
    "year",
    "day",
    "length",
    "weight",
    "count",
    "looped",
    "neighbors",
    "income",
    "label"
)
DATASET_PREDICT_ATTRS_LEN = len(DATASET_ATTRS) - 1
TARGET_ATTR = "label"
N_FOLD = 5
N_CLUSTER = 29
N_ROWS = None

ASSETS_PATH = "./assets"
DATA_PATH = f"{ASSETS_PATH}/dataset/BitcoinHeistData.csv"
RESULTS_PATH = f"{ASSETS_PATH}/results"
CHARTS_PATH = f"{RESULTS_PATH}/charts"

COLOR_1 = "teal"
COLOR_2 = "xkcd:azure"

