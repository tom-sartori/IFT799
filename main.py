import Gene
import Label
import intra_class

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import umap

from inter_class import get_inter_class_distance_markdown_table
from overlap import get_overlap_markdown_table
from shared import get_all_genes_by_class, get_one_gene_by_class
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

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

    # 2.a) Plotting the classes' distributions for the first chosen gene as histograms.
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

    # 2.b) Plotting the data of both chosen genes as one scatter plot.
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

    # 2.c) Plotting joint plots of the distributions of all pairs of classes for the first chosen gene.
    # for i in range(0, len(distinct_classes)):
    #     for j in range(i + 1, len(distinct_classes)):
    #         sns.jointplot(x=chosen_gene_1_data_by_class[distinct_classes[i]], y=chosen_gene_1_data_by_class[distinct_classes[j]], kind='hist')
    #         plt.show()

    # 2.d) Plotting scatter plots with PCA, t-SNE and UMAP.

    # Read data
    # data = pd.read_csv('resources/data.csv')
    # Remove the first column
    # data_without_sample = data.iloc[:, 1:]
    # Get the class column from labels.csv
    # classes = pd.read_csv('resources/labels.csv')['Class']

    # 2.d.i) PCA
    # pca = PCA(n_components=2)
    # pca.fit(data_without_sample)
    # data_pca = pca.transform(data_without_sample)
    # data_pca_df = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
    # data_pca_df['class'] = classes
    # sns.scatterplot(data=data_pca_df, x='PC1', y='PC2', hue='class', palette='deep')
    # plt.title('PCA')
    # plt.show()

    # 2.d.ii) t-SNE
    # tsne = TSNE(n_components=2)
    # tsne.fit(data_without_sample)
    # data_tsne = tsne.fit_transform(data_without_sample)
    # data_tsne_df = pd.DataFrame(data_tsne, columns=['t-SNE1', 't-SNE2'])
    # data_tsne_df['class'] = classes
    # sns.scatterplot(data=data_tsne_df, x='t-SNE1', y='t-SNE2', hue='class', palette='deep')
    # plt.title('t-SNE')
    # plt.show()

    # 2.d.iii) UMAP
    # umap = umap.UMAP(n_components=2)
    # umap.fit(data_without_sample)
    # data_umap = umap.fit_transform(data_without_sample)
    # data_umap_df = pd.DataFrame(data_umap, columns=['UMAP1', 'UMAP2'])
    # data_umap_df['class'] = classes
    # sns.scatterplot(data=data_umap_df, x='UMAP1', y='UMAP2', hue='class', palette='deep')
    # plt.title('UMAP')
    # plt.show()



