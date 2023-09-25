import pandas as pd

import inter_class
import intra_class


def get_overlap(intra_class_distance_a, intra_class_distance_b, inter_class_distance_a_b) -> float:
    return (intra_class_distance_a + intra_class_distance_b) / (2 * inter_class_distance_a_b)


def get_overlap_markdown_table(tuple_class_matrix_list: [(str, [[float]])]) -> str:
    rows = []
    for tuple_class_matrix_a in tuple_class_matrix_list:
        for tuple_class_matrix_b in tuple_class_matrix_list:
            if tuple_class_matrix_a[0] < tuple_class_matrix_b[0]:
                rows.append([
                    tuple_class_matrix_a[0],
                    tuple_class_matrix_b[0],
                    get_overlap(
                        intra_class.get_euclidean_intra_class_distance(tuple_class_matrix_a[1]),
                        intra_class.get_euclidean_intra_class_distance(tuple_class_matrix_b[1]),
                        inter_class.get_euclidean_inter_class_distance(
                            tuple_class_matrix_a[1], tuple_class_matrix_b[1])
                    ),
                    get_overlap(
                        intra_class.get_cosine_intra_class_distance(tuple_class_matrix_a[1]),
                        intra_class.get_cosine_intra_class_distance(tuple_class_matrix_b[1]),
                        inter_class.get_cosine_inter_class_distance(
                            tuple_class_matrix_a[1], tuple_class_matrix_b[1])
                    )
                ])

    df = pd.DataFrame(rows, columns=[
        'Class A',
        'Class B',
        'Euclidean overlap',
        # 'Mahalanobis overlap',
        'Cosine overlap'
    ])
    return df.to_markdown(floatfmt=".6f", colalign=("center", "center", "center", "center"), index=False)
