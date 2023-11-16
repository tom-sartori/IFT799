###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
import os.path


def get_clustered_data_kmeans(k, data):
    """
    Performs a k-means clustering on the data and returns data with an additional column "cluster".
    :param k: the number of clusters
    :param data: the data to cluster
    """
    # Copy only the features we want to cluster
    data_to_cluster = data[["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]].copy()
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data_to_cluster)
    data["cluster"] = kmeans.labels_
    return data

def get_clustred_data_hierarchical(data, k=None, threshold=None, print_dendrogram=True, save_dendrogram=False):
    """
    Performs a hierarchical clustering on the data and returns data with an additional column "cluster".
    :param k: the number of clusters
    :param data: the data to cluster
    """
    if k is None and threshold is None:
        raise ValueError("Either k or threshold must be specified")
    # Copy only the features we want to cluster
    data_to_cluster = data[["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]].copy()

    # Perform hierarchical clustering
    Z = linkage(data_to_cluster, method="ward", metric="euclidean")
    if k is not None:
        clusters = fcluster(Z, k, criterion="maxclust")
        name = f"_with_{k}_clusters"
    else:
        clusters = fcluster(Z, threshold, criterion="distance")
        name = f"_with_threshold_{threshold}_{max(clusters)}_clusters"
    data["cluster"] = clusters

    # Save dendrogram
    if save_dendrogram:
        plt.figure(figsize=(25, 10))
        plt.title("Hierarchical Clustering Dendrogram"+name.replace("_", " "))
        plt.xlabel("sample index")
        plt.ylabel("distance")
        dendrogram(Z, truncate_mode="level", p=5, color_threshold=threshold)
        plt.savefig(os.path.join("rapport", "img", f"dendrogram" + name + ".png"))

    # Print dendrogram
    if print_dendrogram:
        plt.figure(figsize=(25, 10))
        plt.title("Hierarchical Clustering Dendrogram"+name.replace("_", " "))
        plt.xlabel("sample index")
        plt.ylabel("distance")
        dendrogram(Z, truncate_mode="level", p=5, color_threshold=threshold)
        plt.show()

    return data

