"""Module for implementing the overall logics.

This consists of extracting data, training model, using it and ranking the
results.
"""
import logging

from sklearn.cluster import KMeans

from bitcoin_heist.src.constants import N_CLUSTER
from bitcoin_heist.src.data import prepare_dataset, write_model

logger = logging.getLogger(__name__)


def main():
    """Run main logics for generating clusters."""
    training_data, testing_data = prepare_dataset()
    model = KMeans(n_clusters=N_CLUSTER, max_iter=30)
    logger.info(f"Training K-means with {N_CLUSTER} clusters.")
    result = model.fit(training_data)
    write_model(result)
