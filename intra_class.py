###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import sys

import pandas as pd

import utils


def get_euclidean_intra_class_distance(matrix: [[float]]) -> float:
    print("Calculating euclidean intra-class distance.")
    return __get_intra_class_distance(matrix, utils.get_euclidean_distance)


def get_mahalanobis_intra_class_distance(matrix: [[float]]) -> float:
    print("Calculating mahalanobis intra-class distance.")
    return __get_intra_class_distance(matrix, utils.get_mahalanobis_distance, utils.get_inv_cov_matrix(matrix))


def get_cosine_intra_class_distance(matrix: [[float]]) -> float:
    print("Calculating cosine intra-class distance.")
    return __get_intra_class_distance(matrix, utils.get_cosine_distance)


def __get_intra_class_distance(matrix: [[float]], distance_function, inv_cov_for_mahalanobis: [[float]] = None) -> float:
    mean_list: [float] = utils.get_column_means(matrix)

    dist_intra: float = sys.float_info.min
    if inv_cov_for_mahalanobis is None:
        for row in matrix:
            dist_intra = max(dist_intra, distance_function(row, mean_list))
    else:
        for row in matrix:
            dist_intra = max(dist_intra, distance_function(row, mean_list, inv_cov_for_mahalanobis))

    return dist_intra


def get_intra_class_distance_markdown_table(tuple_class_matrix_list: [(str, [[float]])]) -> str:
    rows = []
    for tuple_class_matrix in tuple_class_matrix_list:
        rows.append([
            tuple_class_matrix[0],
            get_euclidean_intra_class_distance(tuple_class_matrix[1]),
            get_mahalanobis_intra_class_distance(tuple_class_matrix[1]),
            get_cosine_intra_class_distance(tuple_class_matrix[1])
        ])

    df = pd.DataFrame(rows, columns=[
        'Class',
        'Euclidean intra-class distance',
        'Mahalanobis intra-class distance',
        'Cosine intra-class distance'
    ])
    return df.to_markdown(floatfmt=".6f", colalign=("center", "center", "center", "center"), index=False)
