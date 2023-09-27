import Gene
import Label
import intra_class

import matplotlib.pyplot as plt

from inter_class import get_inter_class_distance_markdown_table
from overlap import get_overlap_markdown_table
from shared import get_all_genes_by_class, get_one_gene_by_class

if __name__ == '__main__':
    # Get data.
    labels: [Label] = Label.get_labels()
    genes: [Gene] = Gene.get_genes()

    # print(Label.get_distinct_classes(labels))  # ['PRAD', 'LUAD', 'BRCA', 'KIRC', 'COAD']

    tuple_class_matrix_list: [(str, [[float]])] = []
    for cls in Label.get_distinct_classes(labels):
        tuple_class_matrix_list.append((cls, get_all_genes_by_class(labels, genes, cls)))

    # Method 1:
    #print(intra_class.get_intra_class_distance_markdown_table(tuple_class_matrix_list) + "\n")
    #print(get_inter_class_distance_markdown_table(tuple_class_matrix_list) + "\n")
    #print(get_overlap_markdown_table(tuple_class_matrix_list))

    # class_a: str = "BRCA"
    # class_b: str = "KIRC"
    #
    # matrix_a: [[float]] = get_genes_by_class(labels, genes, class_a)
    # matrix_b: [[float]] = get_genes_by_class(labels, genes, class_b)
    #
    # intra_class_distance_a: float = get_euclidean_intra_class_distance(matrix_a)
    # intra_class_distance_b: float = get_euclidean_intra_class_distance(matrix_b)
    #
    # inter_class_distance_a_b: float = get_euclidean_inter_class_distance(matrix_a, matrix_b)
    #
    # overlap_a_b: float = get_overlap(intra_class_distance_a, intra_class_distance_b, inter_class_distance_a_b)
    #
    # print("intra_class_distance_a : " + str(intra_class_distance_a))
    # print("intra_class_distance_b : " + str(intra_class_distance_b))
    # print("inter_class_distance_a_b : " + str(inter_class_distance_a_b))
    # print("overlap_a_b : " + str(overlap_a_b))

    # intra_class_distance_a: 256.9586133692328
    # intra_class_distance_b: 270.1335553730265
    # inter_class_distance_a_b: 215.22326915974665
    # overlap_a_b: 1.2245241204635546
    
    # Method 2:
    # chosen_gene_1 = 3
    # chosen_gene_2 = 4
    # distinct_classes: [str] = Label.get_distinct_classes(labels)
    # chosen_gene_1_data_by_class: {str: [float]} = {}
    # chosen_gene_2_data_by_class: {str: [float]} = {}
    # for class_name in distinct_classes:
    #     samples_from_class: [str] = Label.get_samples_by_class(labels, class_name)
    #     chosen_gene_1_data_by_class[class_name] = get_one_gene_by_class(labels, genes, class_name, chosen_gene_1)
    #     chosen_gene_2_data_by_class[class_name] = get_one_gene_by_class(labels, genes, class_name, chosen_gene_2)

    # Plotting the classes' distributions for the first chosen gene as histograms.
    # fig, axs = plt.subplots(2, 3)
    # plt.subplots_adjust(wspace=0.5, hspace=0.5)
    # fig.suptitle(f'Distributions of the gene_{chosen_gene_1} for each class')
    # axs[0, 0].hist(chosen_gene_1_data_by_class[distinct_classes[0]], bins=20, rwidth=0.9, color='darkorange')
    # axs[0, 0].set_title(distinct_classes[0])
    # axs[0, 1].hist(chosen_gene_1_data_by_class[distinct_classes[1]], bins=20, rwidth=0.9, color='darkred')
    # axs[0, 1].set_title(distinct_classes[1])
    # axs[0, 2].hist(chosen_gene_1_data_by_class[distinct_classes[2]], bins=20, rwidth=0.9, color='darkgreen')
    # axs[0, 2].set_title(distinct_classes[2])
    # axs[1, 0].hist(chosen_gene_1_data_by_class[distinct_classes[3]], bins=20, rwidth=0.9, color='darkblue')
    # axs[1, 0].set_title(distinct_classes[3])
    # axs[1, 1].hist(chosen_gene_1_data_by_class[distinct_classes[4]], bins=20, rwidth=0.9, color='darkviolet')
    # axs[1, 1].set_title(distinct_classes[4])
    # axs[1, 2].axis('off')
    # plt.show()

    # Plotting the data of both chosen genes as one scatter plot.
    # plt.scatter(chosen_gene_1_data_by_class[distinct_classes[0]], chosen_gene_2_data_by_class[distinct_classes[0]], color='darkorange', marker='x')
    # plt.scatter(chosen_gene_1_data_by_class[distinct_classes[1]], chosen_gene_2_data_by_class[distinct_classes[1]], color='darkred', marker='x')
    # plt.scatter(chosen_gene_1_data_by_class[distinct_classes[2]], chosen_gene_2_data_by_class[distinct_classes[2]], color='darkgreen', marker='x')
    # plt.scatter(chosen_gene_1_data_by_class[distinct_classes[3]], chosen_gene_2_data_by_class[distinct_classes[3]], color='darkblue', marker='x')
    # plt.scatter(chosen_gene_1_data_by_class[distinct_classes[4]], chosen_gene_2_data_by_class[distinct_classes[4]], color='darkviolet', marker='x')
    # plt.xlabel(f'gene_{chosen_gene_1}')
    # plt.ylabel(f'gene_{chosen_gene_2}')
    # plt.title(f'Distributions of the gene_{chosen_gene_1} and gene_{chosen_gene_2} for each class')
    # plt.legend(distinct_classes)
    # plt.show()
