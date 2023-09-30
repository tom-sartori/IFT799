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
import matplotlib.pyplot as plt
import seaborn as sns
import umap

from inter_class import get_inter_class_distance_markdown_table
from overlap import get_overlap_markdown_table
from shared import get_all_genes_by_class, get_one_gene_by_class
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

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
    print(get_inter_class_distance_markdown_table(tuple_class_matrix_list) + "\n")
    print(get_overlap_markdown_table(tuple_class_matrix_list) + "\n")

    # Method 2:
    print("Method 2:\n")
    chosen_gene_1 = 3
    chosen_gene_2 = 4
    distinct_classes: [str] = Label.get_distinct_classes(labels)
    chosen_gene_1_data_by_class: {str: [float]} = {}
    chosen_gene_2_data_by_class: {str: [float]} = {}
    for class_name in distinct_classes:
        samples_from_class: [str] = Label.get_samples_by_class(labels, class_name)
        chosen_gene_1_data_by_class[class_name] = get_one_gene_by_class(labels, genes, class_name, chosen_gene_1)
        chosen_gene_2_data_by_class[class_name] = get_one_gene_by_class(labels, genes, class_name, chosen_gene_2)

    # 2.a) Plotting the classes' distributions for the first chosen gene as histograms.
    fig, axs = plt.subplots(2, 3)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    fig.suptitle(f'Distributions of the gene_{chosen_gene_1} for each class')
    axs[0, 0].hist(chosen_gene_1_data_by_class[distinct_classes[0]], bins=20, rwidth=0.9, color='darkorange')
    axs[0, 0].set_title(distinct_classes[0])
    axs[0, 1].hist(chosen_gene_1_data_by_class[distinct_classes[1]], bins=20, rwidth=0.9, color='darkred')
    axs[0, 1].set_title(distinct_classes[1])
    axs[0, 2].hist(chosen_gene_1_data_by_class[distinct_classes[2]], bins=20, rwidth=0.9, color='darkgreen')
    axs[0, 2].set_title(distinct_classes[2])
    axs[1, 0].hist(chosen_gene_1_data_by_class[distinct_classes[3]], bins=20, rwidth=0.9, color='darkblue')
    axs[1, 0].set_title(distinct_classes[3])
    axs[1, 1].hist(chosen_gene_1_data_by_class[distinct_classes[4]], bins=20, rwidth=0.9, color='darkviolet')
    axs[1, 1].set_title(distinct_classes[4])
    axs[1, 2].axis('off')
    plt.show()

    # 2.b) Plotting the data of both chosen genes as one scatter plot.
    plt.scatter(chosen_gene_1_data_by_class[distinct_classes[0]], chosen_gene_2_data_by_class[distinct_classes[0]],
                color='darkorange', marker='x')
    plt.scatter(chosen_gene_1_data_by_class[distinct_classes[1]], chosen_gene_2_data_by_class[distinct_classes[1]],
                color='darkred', marker='x')
    plt.scatter(chosen_gene_1_data_by_class[distinct_classes[2]], chosen_gene_2_data_by_class[distinct_classes[2]],
                color='darkgreen', marker='x')
    plt.scatter(chosen_gene_1_data_by_class[distinct_classes[3]], chosen_gene_2_data_by_class[distinct_classes[3]],
                color='darkblue', marker='x')
    plt.scatter(chosen_gene_1_data_by_class[distinct_classes[4]], chosen_gene_2_data_by_class[distinct_classes[4]],
                color='darkviolet', marker='x')
    plt.xlabel(f'gene_{chosen_gene_1}')
    plt.ylabel(f'gene_{chosen_gene_2}')
    plt.title(f'Distributions of the gene_{chosen_gene_1} and gene_{chosen_gene_2} for each class')
    plt.legend(distinct_classes)
    plt.show()

    # 2.c) Plotting the distributions of pairs of classes.
    chosen_class_1 = 2
    chosen_class_2 = 3

    # 2.c.i) Plotting the distributions of the first chosen gene for the two chosen classes as one histogram.
    plt.hist(chosen_gene_1_data_by_class[distinct_classes[chosen_class_1]], bins=20, rwidth=0.9, color='darkorange',
             alpha=0.5)
    plt.hist(chosen_gene_1_data_by_class[distinct_classes[chosen_class_2]], bins=20, rwidth=0.9, color='darkblue',
             alpha=0.5)
    plt.xlabel(f'gene_{chosen_gene_1}')
    plt.ylabel('Frequency')
    plt.title(
        f'Distributions of the gene_{chosen_gene_1} for the classes {distinct_classes[chosen_class_1]} and {distinct_classes[chosen_class_2]}')
    plt.legend([distinct_classes[chosen_class_1], distinct_classes[chosen_class_2]])
    plt.show()

    # 2.c.ii) Plotting the distributions of both chosen genes for the two chosen classes as one joint plot.
    # Combining data of the two chosen classes in one dataframe.
    gene_1_data_with_class = pd.DataFrame([[chosen_gene_1_data_by_class[distinct_classes[chosen_class_1]][i],
                                            chosen_gene_2_data_by_class[distinct_classes[chosen_class_1]][i],
                                            distinct_classes[chosen_class_1]] for i in
                                           range(len(chosen_gene_1_data_by_class[distinct_classes[chosen_class_1]]))],
                                          columns=[f'gene_{chosen_gene_1}', f'gene_{chosen_gene_2}', 'class'])
    gene_2_data_with_class = pd.DataFrame([[chosen_gene_1_data_by_class[distinct_classes[chosen_class_2]][i],
                                            chosen_gene_2_data_by_class[distinct_classes[chosen_class_2]][i],
                                            distinct_classes[chosen_class_2]] for i in
                                           range(len(chosen_gene_1_data_by_class[distinct_classes[chosen_class_2]]))],
                                          columns=[f'gene_{chosen_gene_1}', f'gene_{chosen_gene_2}', 'class'])
    gene_1_and_2_data_with_class = pd.concat([gene_1_data_with_class, gene_2_data_with_class], ignore_index=True)

    # Plotting the joint plot.
    sns.jointplot(data=gene_1_and_2_data_with_class, x=f'gene_{chosen_gene_1}', y=f'gene_{chosen_gene_2}', hue='class',
                  palette='deep')
    plt.title(
        f'Distributions of the gene_{chosen_gene_1} and gene_{chosen_gene_2} for the classes {distinct_classes[chosen_class_1]} and {distinct_classes[chosen_class_2]}')
    plt.show()

    # 2.d) Plotting scatter plots with PCA, t-SNE and UMAP.
    # Read data
    data = pd.read_csv('resources/data.csv')
    # Remove the first column
    data_without_sample = data.iloc[:, 1:]
    # Get the class column from labels.csv
    classes = pd.read_csv('resources/labels.csv')['Class']

    # 2.d.i) PCA
    pca = PCA(n_components=2)
    pca.fit(data_without_sample)
    data_pca = pca.transform(data_without_sample)
    data_pca_df = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
    data_pca_df['class'] = classes
    sns.scatterplot(data=data_pca_df, x='PC1', y='PC2', hue='class', palette='deep')
    plt.title('PCA')
    plt.show()

    # 2.d.ii) t-SNE
    tsne = TSNE(n_components=2)
    tsne.fit(data_without_sample)
    data_tsne = tsne.fit_transform(data_without_sample)
    data_tsne_df = pd.DataFrame(data_tsne, columns=['t-SNE1', 't-SNE2'])
    data_tsne_df['class'] = classes
    sns.scatterplot(data=data_tsne_df, x='t-SNE1', y='t-SNE2', hue='class', palette='deep')
    plt.title('t-SNE')
    plt.show()

    # 2.d.iii) UMAP
    umap = umap.UMAP(n_components=2)
    umap.fit(data_without_sample)
    data_umap = umap.fit_transform(data_without_sample)
    data_umap_df = pd.DataFrame(data_umap, columns=['UMAP1', 'UMAP2'])
    data_umap_df['class'] = classes
    sns.scatterplot(data=data_umap_df, x='UMAP1', y='UMAP2', hue='class', palette='deep')
    plt.title('UMAP')
    plt.show()
