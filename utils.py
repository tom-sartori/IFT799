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
