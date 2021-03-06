"""Module for implementing the overall logics of the data analysis."""
import logging

import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans

from bitcoin_heist.src.constants import MAX_ITER, N_CLUSTER, TARGET_ATTR
from bitcoin_heist.src.data import (
    prepare_dataset, write_confusion_matrix,
    write_model,
)

logger = logging.getLogger(__name__)


def main(n_clusters=N_CLUSTER):
    """Run main logics for generating clusters for each label.

    Get dataset, remove label from training data so it's not used in K-Means,
    generate the model with the same amount of clusters as there are labels,
    use the model to predict each sample's cluster, and then create a
    confusion matrix and evaluate the results (Rand Score).
    """
    training_data = prepare_dataset(n_clusters)
    pruned_training_data = training_data.drop(TARGET_ATTR, axis=1)
    model = KMeans(n_clusters=n_clusters, max_iter=MAX_ITER)

    logger.info(f"Training K-means with {n_clusters} clusters.")
    result = model.fit(pruned_training_data)
    write_model(result, n_clusters)

    logger.info(f"Predicting clusters for samples.")
    predicted = result.predict(pruned_training_data)
    logger.info(f"Cross-referencing cluesters and labels.")

    data_frame = pd.DataFrame({
        'Labels': training_data[TARGET_ATTR],
        'Predicted': predicted,
    })

    labels = data_frame['Labels']
    predicted = data_frame['Predicted']
    confusion_matrix = pd.crosstab(labels, predicted, dropna=False)
    logger.debug(confusion_matrix)
    write_confusion_matrix(confusion_matrix, n_clusters)

    logger.info(f"Similarity: {metrics.rand_score(labels, predicted)}")
    adjusted = metrics.adjusted_rand_score(labels, predicted)
    logger.info(f"Adjusted for chance: {adjusted}")


def binary():
    """Run main logics for generating two clusters, determining whether
    the transaction is suspicious (True) or not (False).
    """
    main(n_clusters=2)
