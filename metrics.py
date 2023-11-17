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

if __name__ == "__main__":
    # 5 positive users
    # 2631,0.5329999999999999,0.3929999999999999,0.423,0.367,0.397,1
    # 785,0.544,0.354,0.391,0.295,0.405,1
    # 2302,0.627,0.377,0.385,0.525,0.332,1
    # 218,0.5215714285714286,0.3914285714285714,0.3845714285714285,0.3608571428571428,0.3737142857142857,1
    # 110,0.609,0.3565,0.3349999999999999,0.4674999999999999,0.343,1
    user1 = {"valence_intensity": 0.5329999999999999, "fear_intensity": 0.3929999999999999, "anger_intensity": 0.423, "happiness_intensity": 0.367, "sadness_intensity": 0.397}
    user2 = {"valence_intensity": 0.544, "fear_intensity": 0.354, "anger_intensity": 0.391, "happiness_intensity": 0.295, "sadness_intensity": 0.405}
    user3 = {"valence_intensity": 0.627, "fear_intensity": 0.377, "anger_intensity": 0.385, "happiness_intensity": 0.525, "sadness_intensity": 0.332}
    user4 = {"valence_intensity": 0.5215714285714286, "fear_intensity": 0.3914285714285714, "anger_intensity": 0.3845714285714285, "happiness_intensity": 0.3608571428571428, "sadness_intensity": 0.3737142857142857}
    user5 = {"valence_intensity": 0.609, "fear_intensity": 0.3565, "anger_intensity": 0.3349999999999999, "happiness_intensity": 0.4674999999999999, "sadness_intensity": 0.343}

    # 5 negative users
    # 0,0.462,0.42,0.418,0.423,0.345,-1
    # 3081,0.304,0.621,0.627,0.135,0.5379999999999999,-1
    # 234,0.423,0.455,0.504,0.237,0.4529999999999999,-1
    # 1491,0.348,0.53,0.5870000000000001,0.241,0.486,-1
    # 1450,0.4429999999999999,0.449,0.421,0.306,0.391,-1
    user6 = {"valence_intensity": 0.462, "fear_intensity": 0.42, "anger_intensity": 0.418, "happiness_intensity": 0.423, "sadness_intensity": 0.345}
    user7 = {"valence_intensity": 0.304, "fear_intensity": 0.621, "anger_intensity": 0.627, "happiness_intensity": 0.135, "sadness_intensity": 0.5379999999999999}
    user8 = {"valence_intensity": 0.423, "fear_intensity": 0.455, "anger_intensity": 0.504, "happiness_intensity": 0.237, "sadness_intensity": 0.4529999999999999}
    user9 = {"valence_intensity": 0.348, "fear_intensity": 0.53, "anger_intensity": 0.5870000000000001, "happiness_intensity": 0.241, "sadness_intensity": 0.486}
    user10 = {"valence_intensity": 0.4429999999999999, "fear_intensity": 0.449, "anger_intensity": 0.421, "happiness_intensity": 0.306, "sadness_intensity": 0.391}

    # 5 neutral users
    # 844,0.4835,0.52125,0.3785,0.34675,0.374,0
    # 893,0.505,0.415,0.427,0.325,0.389,0
    # 1529,0.4755,0.412,0.427,0.3225,0.3505,0
    # 2070,0.496,0.445,0.462,0.307,0.385,0
    # 1691,0.508,0.505,0.435,0.363,0.494,0
    user11 = {"valence_intensity": 0.4835, "fear_intensity": 0.52125, "anger_intensity": 0.3785, "happiness_intensity": 0.34675, "sadness_intensity": 0.374}
    user12 = {"valence_intensity": 0.505, "fear_intensity": 0.415, "anger_intensity": 0.427, "happiness_intensity": 0.325, "sadness_intensity": 0.389}
    user13 = {"valence_intensity": 0.4755, "fear_intensity": 0.412, "anger_intensity": 0.427, "happiness_intensity": 0.3225, "sadness_intensity": 0.3505}
    user14 = {"valence_intensity": 0.496, "fear_intensity": 0.445, "anger_intensity": 0.462, "happiness_intensity": 0.307, "sadness_intensity": 0.385}
    user15 = {"valence_intensity": 0.508, "fear_intensity": 0.505, "anger_intensity": 0.435, "happiness_intensity": 0.363, "sadness_intensity": 0.494}

    import itertools

    # Testing distance on users with the same sentiment
    print("Same sentiment: positive")
    avg_distance = 0
    for combi in itertools.combinations([user1, user2, user3, user4, user5], 2):
        avg_distance += euclidean_distance(combi[0], combi[1])
    avg_distance /= 10
    print(f"Average distance: {avg_distance}")
    print()

    print("Same sentiment: negative")
    avg_distance = 0
    for combi in itertools.combinations([user6, user7, user8, user9, user10], 2):
        avg_distance += euclidean_distance(combi[0], combi[1])
    avg_distance /= 10
    print(f"Average distance: {avg_distance}")
    print()

    print("Same sentiment: neutral")
    avg_distance = 0
    for combi in itertools.combinations([user11, user12, user13, user14, user15], 2):
        avg_distance += euclidean_distance(combi[0], combi[1])
    avg_distance /= 10
    print(f"Average distance: {avg_distance}")

    # Testing distance on users with different sentiment
    print()
    print("Different sentiment: positive and negative")
    avg_distance = 0
    for combi in itertools.product([user1, user2, user3, user4, user5], [user6, user7, user8, user9, user10]):
        avg_distance += euclidean_distance(combi[0], combi[1])
    avg_distance /= 25
    print(f"Average distance: {avg_distance}")
    print()
