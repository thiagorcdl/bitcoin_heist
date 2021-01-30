"""Module for implementing the data preparation.

This involves dividing the known data set into Training and Testing subsets.
"""
import csv
import logging
from functools import lru_cache
from pathlib import Path

import pandas as pd

from bitcoin_heist.src.constants import (
    CHARTS_PATH, DATASET_PREDICT_ATTRS_LEN, DATA_PATH, N_FOLD,
    DATASET_ATTRS, N_ROWS, RESULTS_PATH, TARGET_ATTR,
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


def prepare_dataset() -> tuple:
    """Yield list of Training and Testing data tuples, respectively."""
    create_dirs()
    dataset = load_dataset()

    test_size = len(dataset) // N_FOLD
    training_data = dataset[:-test_size]
    training_data = training_data.drop(TARGET_ATTR, axis=1)
    testing_data = dataset[-test_size:]
    return training_data, testing_data


@lru_cache(maxsize=1)
def get_candidate_features() -> list:
    """Return list of input features to be used as predictor candidates."""
    return DATASET_ATTRS[:DATASET_PREDICT_ATTRS_LEN]


@lru_cache(maxsize=128)
def get_attr_idx(attr) -> int:
    """Return index of the column for given attribute in the data set."""
    return DATASET_ATTRS.index(attr)


def get_column(dataset, attr) -> list:
    """Return list of values for column `attr`."""
    idx = get_attr_idx(attr)
    return [row[idx] for row in dataset]


def show_rank(rank, results, name):
    """Print specific metric's rank to terminal and write CSV file."""
    logger.debug(rank)
    logger.debug(results)
    print_lines = [""]
    path = f"{RESULTS_PATH}/{name.lower()}_rank.csv"

    with open(path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Rank", "Attribute", f"Average {name}"])

        for idx, item in enumerate(rank, start=1):
            print_lines.append(f"{idx:02} - {item[0]}: {item[1]}")
            csv_writer.writerow([idx, item[0], item[1]])

        logger.info("\n".join(print_lines))


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
