#####
# Alexandre Theisse 23 488 180
# Louis-Vincent Capelli 23 211 533
# Tom Sartori 23 222 497
###

import numpy as np
from scipy.spatial import distance


def distinct(items: [str]) -> [str]:
    uniques: [str] = []
    [uniques.append(item) for item in items if item not in uniques]

    return uniques


def get_column_means(matrix: [[float]]) -> [float]:
    return np.mean(matrix, axis=0)


def get_inv_cov_matrix(matrix: [[float]]) -> [[float]]:
    cov_matrix = np.cov(matrix, rowvar=False)
    return np.linalg.inv(cov_matrix)


def get_euclidean_distance(u: [float], v: [float]) -> float:
    return distance.euclidean(u, v)


def get_mahalanobis_distance(u: [float], v: [float], inv_cov: [[float]]) -> float:
    return distance.mahalanobis(u, v, inv_cov)


def get_cosine_distance(u: [float], v: [float]) -> float:
    return distance.cosine(u, v)


def select_columns_for_tuple_class_matrix_list(tuple_class_matrix_list: [(str, [[float]])]) -> [str, np.ndarray]:
    selected_tuples: [str, np.ndarray] = []
    for tup in tuple_class_matrix_list:
        selected_tuples.append((tup[0], np.array(tup[1])[:, 0:2]))
    return selected_tuples
