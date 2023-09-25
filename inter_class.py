import sys

import pandas as pd

import utils


# Inter class distance between "BRCA" and "KIRC".
# Dist-inter("BRCA", "KIRC") = min( dist("BRCA", "KIRC"), dist("KIRC", "BRCA) )
# dist("BRCA", "KIRC") = min( "BRCA"i, mean("KIRC") )
# dist("KIRC", "BRCA") = min( "KIRC"i, mean("BRCA") )


def get_euclidean_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]]) -> float:
    return __get_inter_class_distance(matrix_a, matrix_b, utils.get_euclidean_distance)


def get_cosine_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]]) -> float:
    return __get_inter_class_distance(matrix_a, matrix_b, utils.get_cosine_distance)


def __get_inter_class_distance(matrix_a: [[float]], matrix_b: [[float]], distance_function) -> float:
    mean_tab_a: [float] = utils.get_column_means(matrix_a)
    mean_tab_b: [float] = utils.get_column_means(matrix_b)

    dist_inter_a_b: float = sys.float_info.max
    for row in matrix_a:
        dist_inter_a_b = min(dist_inter_a_b, distance_function(row, mean_tab_b))

    dist_inter_b_a: float = sys.float_info.max
    for row in matrix_b:
        dist_inter_b_a = min(dist_inter_b_a, distance_function(row, mean_tab_a))

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
                    # get_mahalanobis_inter_class_distance(tuple_class_matrix_a[1], tuple_class_matrix_b[1]),
                    get_cosine_inter_class_distance(tuple_class_matrix_a[1], tuple_class_matrix_b[1])
                ])

    df = pd.DataFrame(rows, columns=[
        'Class A',
        'Class B',
        'Euclidean inter-class distance',
        # 'Mahalanobis inter-class distance',
        'Cosine inter-class distance',
    ])
    return df.to_markdown(floatfmt=".6f", colalign=("center", "center", "center", "center"), index=False)
