###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

from sklearn.cluster import KMeans


def get_clustered_data_kmeans(k, data):
    """
    Performs a k-means clustering on the data and returns data with an additional column "cluster".
    :param k: the number of clusters
    :param data: the data to cluster
    """
    # copy only the features we want to cluster
    data_to_cluster = data[["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]].copy()
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data_to_cluster)
    data["cluster"] = kmeans.labels_
    return data