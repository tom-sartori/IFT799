###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import math
import sklearn.metrics as skm


def euclidean_distance(user1, user2):
    """
    Computes the euclidean distance between 2 users.
    :param user1: the first user
    :param user2: the second user
    """
    distance = 0
    for feature in ["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]:
        distance += (user1[feature] - user2[feature]) ** 2
    return distance ** 0.5

def cluster_centroid(cluster_data):
    """
    Computes the centroid of a cluster.
    :param cluster_data: the data of the cluster
    """
    centroid = {"valence_intensity": 0, "fear_intensity": 0, "anger_intensity": 0, "happiness_intensity": 0, "sadness_intensity": 0}
    for _, user in cluster_data.iterrows():
        for feature in ["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]:
            centroid[feature] += user[feature]
    return centroid

def intra_cluster_distance(cluster_data):
    """
    Computes the intra-cluster distance of a cluster using the euclidean distance.
    :param cluster_data: the data of the cluster
    """
    max_distance = -1
    centroid = cluster_centroid(cluster_data)
    for _, user in cluster_data.iterrows():
        distance = euclidean_distance(user, centroid)
        if distance > max_distance:
            max_distance = distance
    return max_distance

def inter_cluster_distance(cluster1_data, cluster2_data):
    """
    Computes the inter-cluster distance between 2 clusters using the euclidean distance.
    :param cluster1_data: the data of the first cluster
    :param cluster2_data: the data of the second cluster
    """
    min_distance = math.inf

    cluster1_centroid = cluster_centroid(cluster1_data)
    for _, user in cluster2_data.iterrows():
        distance = euclidean_distance(user, cluster1_centroid)
        if distance < min_distance:
            min_distance = distance

    cluster2_centroid = cluster_centroid(cluster2_data)
    for _, user in cluster1_data.iterrows():
        distance = euclidean_distance(user, cluster2_centroid)
        if distance < min_distance:
            min_distance = distance

    return min_distance

def overlap(cluster1_data, cluster2_data):
    """
    Computes the overlap between 2 clusters using the euclidean distance.
    :param cluster1_data: the data of the first cluster
    :param cluster2_data: the data of the second cluster
    """
    return (intra_cluster_distance(cluster1_data) + intra_cluster_distance(cluster2_data))/(2*inter_cluster_distance(cluster1_data, cluster2_data))

def are_clusters_separated(cluster1_data, cluster2_data):
    """
    Checks if 2 clusters are separated using the euclidean distance.
    :param cluster1_data: the data of the first cluster
    :param cluster2_data: the data of the second cluster
    """
    return overlap(cluster1_data, cluster2_data) < 1

def silhouette_score(clustered_data):
    """
    Computes the silhouette score of a clustering.
    :param clustered_data: the data of the clustering
    """
    features = ["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]
    return skm.silhouette_score(clustered_data[features], clustered_data["cluster"])

def precision(clustered_data):
    """
    Computes the precision of a clustering.
    :param clustered_data: the data of the clustering (with the cluster and sentiment columns having the same values)
    """
    # When evaluating a clustering, true positives are the users that are the pairs of users that are in the same cluster and have the same sentiment.
    tp = 0
    # When evaluating a clustering, false positives are the pairs of users that are in the same cluster but have different sentiments.
    fp = 0

    # Testing every pair of users (avoiding duplicates)
    for i in range(len(clustered_data)):
        print(f"{i}/{len(clustered_data)}")
        for j in range(i+1, len(clustered_data)):
            if clustered_data.iloc[i]["cluster"] == clustered_data.iloc[j]["cluster"]:
                if clustered_data.iloc[i]["sentiment"] == clustered_data.iloc[j]["sentiment"]:
                    tp += 1
                else:
                    fp += 1
    return tp/(tp+fp)

def recall(clustered_data):
    """
    Computes the recall of a clustering.
    :param clustered_data: the data of the clustering (with the cluster and sentiment columns having the same values)
    """
    # When evaluating a clustering, true positives are the users that are the pairs of users that are in the same cluster and have the same sentiment.
    tp = 0
    # When evaluating a clustering, false negatives are the pairs of users that are in different clusters but have the same sentiment.
    fn = 0
    
    # Testing every pair of users (avoiding duplicates)
    for i in range(len(clustered_data)):
        for j in range(i+1, len(clustered_data)):
            if clustered_data.iloc[i]["sentiment"] == clustered_data.iloc[j]["sentiment"]:
                if clustered_data.iloc[i]["cluster"] == clustered_data.iloc[j]["cluster"]:
                    tp += 1
                else:
                    fn += 1
    return tp/(tp+fn)

def f1_score(clustered_data):
    """
    Computes the F1-score of a clustering.
    :param clustered_data: the data of the clustering (with the cluster and sentiment columns having the same values)
    """
    r = recall(clustered_data)
    p = precision(clustered_data)
    return  2 * (p * r) / (p + r)