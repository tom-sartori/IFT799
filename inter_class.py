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


# Inter class distance between "BRCA" and "KIRC".
# Dist-inter("BRCA", "KIRC") = min( dist("BRCA", "KIRC"), dist("KIRC", "BRCA) )
# dist("BRCA", "KIRC") = min( "BRCA"i, mean("KIRC") )
# dist("KIRC", "BRCA") = min( "KIRC"i, mean("BRCA") )


def get_euclidean_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]]) -> float:
    print("Calculating euclidean inter-class distance.")
    return __get_inter_class_distance(matrix_a, matrix_b, utils.get_euclidean_distance)


def get_mahalanobis_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]]) -> float:
    print("Calculating mahalanobis inter-class distance.")
    return __get_inter_class_distance(matrix_a, matrix_b, utils.get_mahalanobis_distance,
                                      utils.get_inv_cov_matrix(matrix_a), utils.get_inv_cov_matrix(matrix_b))


def get_cosine_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]]) -> float:
    print("Calculating cosine inter-class distance.")
    return __get_inter_class_distance(matrix_a, matrix_b, utils.get_cosine_distance)


def __get_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]], distance_function,
                               inv_cov_a_for_mahalanobis: [[float]] = None,
                               inv_cov_b_for_mahalanobis: [[float]] = None) -> float:
    mean_tab_a: [float] = utils.get_column_means(matrix_a)
    mean_tab_b: [float] = utils.get_column_means(matrix_b)

    if inv_cov_a_for_mahalanobis is None:
        dist_inter_a_b: float = sys.float_info.max
        for row in matrix_a:
            dist_inter_a_b = min(dist_inter_a_b, distance_function(row, mean_tab_b))

        dist_inter_b_a: float = sys.float_info.max
        for row in matrix_b:
            dist_inter_b_a = min(dist_inter_b_a, distance_function(row, mean_tab_a))
    else:
        dist_inter_a_b: float = sys.float_info.max
        for row in matrix_a:
            dist_inter_a_b = min(dist_inter_a_b, distance_function(row, mean_tab_b, inv_cov_b_for_mahalanobis))

        dist_inter_b_a: float = sys.float_info.max
        for row in matrix_b:
            dist_inter_b_a = min(dist_inter_b_a, distance_function(row, mean_tab_a, inv_cov_a_for_mahalanobis))

    return min(dist_inter_a_b, dist_inter_b_a)


def get_inter_class_distance_markdown_table(tuple_class_matrix_list: [(str, [[float]])]) -> str:
    rows = []
    for tuple_class_matrix_a in tuple_class_matrix_list:
        for tuple_class_matrix_b in tuple_class_matrix_list:
            if tuple_class_matrix_a[0] < tuple_class_matrix_b[0]:
                rows.append([
                    tuple_class_matrix_a[0],
                    tuple_class_matrix_b[0],
                    get_euclidean_inter_class_distance(tuple_class_matrix_a[1], tuple_class_matrix_b[1]),
                    get_mahalanobis_inter_class_distance(tuple_class_matrix_a[1], tuple_class_matrix_b[1]),
                    get_cosine_inter_class_distance(tuple_class_matrix_a[1], tuple_class_matrix_b[1])
                ])

    df = pd.DataFrame(rows, columns=[
        'Class A',
        'Class B',
        'Euclidean inter-class distance',
        'Mahalanobis inter-class distance',
        'Cosine inter-class distance',
    ])
    return df.to_markdown(floatfmt=".6f", colalign=("center", "center", "center", "center", "center"), index=False)
