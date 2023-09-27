import Gene
import Label
import intra_class
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from utils import select_columns_for_tuple_class_matrix_list
from utils import nomtuples
import matplotlib.pyplot as plt

from inter_class import get_inter_class_distance_markdown_table
from overlap import get_overlap_markdown_table
from shared import get_genes_by_class

if __name__ == '__main__':
    # Get data.
    labels: [Label] = Label.get_labels()
    genes: [Gene] = Gene.get_genes()

    # print(Label.get_distinct_classes(labels))  # ['PRAD', 'LUAD', 'BRCA', 'KIRC', 'COAD']

    tuple_class_matrix_list: [(str, [[float]])] = []
    for cls in Label.get_distinct_classes(labels):
        tuple_class_matrix_list.append((cls, get_genes_by_class(labels, genes, cls)))

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
    data=select_columns_for_tuple_class_matrix_list(tuple_class_matrix_list)
    

    #fait moi un histogramme avec matplotlib pour chaque classe en fonction des gènes 
    #deux histogrammes par classe
  
    plt.figure(figsize=(10, 10))

    for i, (cls, matrix) in enumerate(data):
        plt.subplot(3, 2, i + 1)
        plt.title(cls)
        plt.hist(matrix, bins=100)
        
        plt.tight_layout()
    #fait moi un plot avec les nuages de points pour chaque classe en fonction des gènes
    #1 plot au total
    plt.figure(figsize=(10, 10))
    for i, (cls, matrix) in enumerate(data):
        plt.subplot(3, 2, i + 1)
        plt.scatter(matrix[:, 1], matrix[:, 0], label=cls)
        plt.tight_layout()
    plt.show()
    
    
    
   
    
    
    
    
    
    
    