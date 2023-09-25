import sys

import pandas as pd

import utils


def get_euclidean_intra_class_distance(matrix: [[float]]) -> float:
    return __get_intra_class_distance(matrix, utils.get_euclidean_distance)


def get_mahalanobis_intra_class_distance(matrix: [[float]]) -> float:
    mean_list: [float] = utils.get_column_means(matrix)

    dist_intra: float = sys.float_info.min
    for row in matrix:
        dist_intra = max(dist_intra, utils.get_mahalanobis_distance(row, mean_list, utils.get_inv_cov_matrix(matrix)))

    return dist_intra
    # return __get_intra_class_distance(matrix, utils.get_mahalanobis_distance)


def get_cosine_intra_class_distance(matrix: [[float]]) -> float:
    return __get_intra_class_distance(matrix, utils.get_cosine_distance)


def __get_intra_class_distance(matrix: [[float]], distance_function) -> float:
    mean_list: [float] = utils.get_column_means(matrix)

    dist_intra: float = sys.float_info.min
    for row in matrix:
        dist_intra = max(dist_intra, distance_function(row, mean_list))

    return dist_intra


def get_intra_class_distance_markdown_table(tuple_class_matrix_list: [(str, [[float]])]) -> str:
    rows = []
    for tuple_class_matrix in tuple_class_matrix_list:
        rows.append([
            tuple_class_matrix[0],
            get_euclidean_intra_class_distance(tuple_class_matrix[1]),
            # get_mahalanobis_intra_class_distance(tuple_class_matrix[1]),
            get_cosine_intra_class_distance(tuple_class_matrix[1])
        ])

    df = pd.DataFrame(rows, columns=[
        'Class',
        'Euclidean intra-class distance',
        # 'Mahalanobis intra-class distance',
        'Cosine intra-class distance'
    ])
    return df.to_markdown(floatfmt=".6f", colalign=("center", "center", "center"), index=False)
