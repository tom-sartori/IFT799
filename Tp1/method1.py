###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import Gene
import Label
import intra_class

import pandas as pd

from overlap import get_overlap_markdown_table
from shared import get_all_genes_by_class

if __name__ == '__main__':
    print(pd.DataFrame([
        ["Alexandre Theisse", "23 488 180", "thea1804"],
        ["Louis-Vincent Capelli", "23 211 533", "capl1101"],
        ["Tom Sartori", "23 222 497", "sart0701"]
    ], columns=["Name", "Matricule", "CIP"]).to_markdown(index=False))

    print("\nDue to the size of the data, the program may take a while to run.\n")

    # Retrieve data.
    labels: [Label] = Label.get_labels()
    genes: [Gene] = Gene.get_genes()

    # Split data by class.
    tuple_class_matrix_list: [(str, [[float]])] = []
    for cls in Label.get_distinct_classes(labels):
        tuple_class_matrix_list.append((cls, get_all_genes_by_class(labels, genes, cls)))

    # Method 1:
    print("Method 1:\n")
    print(intra_class.get_intra_class_distance_markdown_table(tuple_class_matrix_list) + "\n")
    print(intra_class.get_inter_class_distance_markdown_table(tuple_class_matrix_list) + "\n")
    print(get_overlap_markdown_table(tuple_class_matrix_list) + "\n")