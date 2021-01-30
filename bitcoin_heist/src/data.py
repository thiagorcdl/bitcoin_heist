"""Module for implementing the data preparation.

This involves dividing the known data set into Training and Testing subsets.
"""
import csv
import logging
import re
from functools import lru_cache
from pathlib import Path

import pandas as pd

from bitcoin_heist.src.constants import (
    CHARTS_PATH, DATASET_PREDICT_ATTRS_LEN, DATA_PATH, N_CLUSTER,
    DATASET_ATTRS, N_ROWS, RESULTS_PATH,
)

logger = logging.getLogger(__name__)


def create_dirs() -> None:
    """Ensure necessary paths are valid."""
    for dir_path in [RESULTS_PATH, CHARTS_PATH]:
        Path(dir_path).mkdir(parents=True, exist_ok=True)


def load_dataset(file_path=DATA_PATH, n_rows=N_ROWS) -> pd.DataFrame:
    """Open dataset file and load its contents."""
    logger.info(f"Loading dataset from {file_path}.")
    return pd.read_csv(file_path, nrows=n_rows, usecols=DATASET_ATTRS)


def prepare_dataset():
    """Yield list of Training and Testing data tuples, respectively."""
    create_dirs()
    return load_dataset()


@lru_cache(maxsize=1)
def get_candidate_features() -> list:
    """Return list of input features to be used as predictor candidates."""
    return DATASET_ATTRS[:DATASET_PREDICT_ATTRS_LEN]


def write_model(result):
    """Write k-means results (centroids) in CSV file.

    Build headers from amount of folds resent in attribute results.
    """

    csv_headers = get_candidate_features()
    path = f"{RESULTS_PATH}/centroids.csv"

    with open(path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_headers)
        for centroid in result.cluster_centers_:
            csv_writer.writerow(centroid)


def write_confusion_matrix(confusion_matrix):
    """Write results of confusion_matrix.

    Ignore first 2 lines
    """

    csv_headers = ["Labels\Predicted"] + list(range(N_CLUSTER))
    path = f"{RESULTS_PATH}/confusion_matrix.csv"

    with open(path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_headers)
        for matrix_row in str(confusion_matrix).split("\n")[2:]:
            csv_row = re.sub(r"\s+", " ", matrix_row).split()
            csv_writer.writerow(csv_row)
