###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import itertools

import data_management as dm
import plotting as pl
import clustering as cl
import metrics as me


data = dm.get_all_users_as_df()

##############
# Question 1 #
##############

# features = ["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]
# # All possible combinations of 2 features
# combinations = list(itertools.combinations(features, 2))

# # Plots distributions of all combinations of 2 features
# for combi in combinations:
#     # pl.plot_conjoint_representation(data, combi[0], combi[1])
#     # pl.plot_conjoint_representation(data, combi[0], combi[1], save=True, show=False)
#     pl.plot_conjoint_distribution(data, combi[0], combi[1], save=True, show=False)
#     continue


##############
# Question 2 #
##############

# # Running UMAP on the data to plot it
# data_with_umap = dm.get_data_with_umap(data)

# # Running k-means clustering on the data with k = 2, 3, ..., 10
# for k in range(2, 11):
#     clustered_data_with_umap = cl.get_clustered_data_kmeans(k, data_with_umap)
#     pl.plot_clustered_data_with_umap(clustered_data_with_umap, save=True, show=False)
#     continue


##############
# Question 3 #
##############

# # Running k-means clustering on the data with k = 2, 3, ..., 10
# for k in range(2, 11):
#     clustered_data = cl.get_clustered_data_kmeans(k, data)

#     # Printing the silhouette score and the overlap for each combination of 2 clusters
#     print(f"K = {k}")
#     print(f"Silhouette score: {round(me.silhouette_score(clustered_data), 2)}\n")
#     if k > 5:
#         continue
#     for combi in list(itertools.combinations(range(k), 2)):
#         cluster1_data = clustered_data[clustered_data["cluster"] == combi[0]]
#         cluster2_data = clustered_data[clustered_data["cluster"] == combi[1]]
#         print(f"Overlap (C{combi[0]+1}, C{combi[1]+1}): {round(me.overlap(cluster1_data, cluster2_data), 2)}")
#     print()
#     print()

# # Printing precision, recall and F1-score for k = 3
# # To ensure that we get the best results,
# # we test every association of a cluster and a sentiment and keep the best one

# print("K = 3")
# clustered_data = cl.get_clustered_data_kmeans(3, data)

# # We generate all possible permutations of the clusters
# perm = list(itertools.permutations(range(3), 3))

# # Each permutation is tested with 
# # the first cluster being associated with the -1 sentiment,
# # the second cluster being associated with the 0 sentiment,
# # and the third cluster being associated with the 1 sentiment
# precisions = []
# recalls = []
# f1_scores = []
# for p in perm:
#     clustered_data_copy = clustered_data.copy()
#     clustered_data_copy["cluster"] = clustered_data_copy["cluster"].replace(p[0], -1)
#     clustered_data_copy["cluster"] = clustered_data_copy["cluster"].replace(p[1], 0)
#     clustered_data_copy["cluster"] = clustered_data_copy["cluster"].replace(p[2], 1)
    
#     print(f"Permutation: Clusters {p} = sentiment (-1, 0, 1))")
#     precisions.append(me.precision(clustered_data_copy))
#     recalls.append(me.recall(clustered_data_copy))
#     f1_scores.append(me.f1_score(clustered_data_copy))
#     print(f"Precision: {precisions[-1]}")
#     print(f"Recall: {recalls[-1]}")
#     print(f"F1-score: {f1_scores[-1]}")
#     print()

# # We keep the permutation that gives the best f1-score
# best_perm = perm[f1_scores.index(max(f1_scores))]
# print(f"Best permutation: Clusters {best_perm} = sentiment (-1, 0, 1))")
# print(f"Precision: {precisions[perm.index(best_perm)]}")
# print(f"Recall: {recalls[perm.index(best_perm)]}")
# print(f"F1-score: {f1_scores[perm.index(best_perm)]}")
# print()

##############
# Question 4 #
##############

# # Threshold = 3.63 : 10 clusters
# # Threshold = 4.5 :  9 clusters
# # Threshold = 5 :    8 clusters
# # Threshold = 6 :    7 clusters
# # Threshold = 6.2 :  6 clusters
# # Threshold = 8 :    5 clusters
# # Threshold = 9 :    4 clusters
# # Threshold = 12 :   3 clusters
# # Threshold = 18 :   2 clusters

# # Running hierarchical clustering on the data with different thresholds
# for threshold in [18, 12, 9, 8, 6.2, 6, 5, 4.5, 3.63]:
#     clustered_data = cl.get_clustred_data_hierarchical(data, threshold=threshold, print_dendrogram=False)
#     # clustered_data_with_umap = dm.get_data_with_umap(clustered_data)
#     # pl.plot_clustered_data_with_umap(clustered_data_with_umap)
#     # Printing the silhouette score and the overlap for each combination of 2 clusters
#     print(f"Threshold = {threshold}")
#     print(f"Silhouette score: {me.silhouette_score(clustered_data)}\n")
#     for combi in list(itertools.combinations(range(len(clustered_data["cluster"].unique())), 2)):
#         cluster1_data = clustered_data[clustered_data["cluster"] == combi[0]]
#         cluster2_data = clustered_data[clustered_data["cluster"] == combi[1]]
#         print(f"Overlap (C{combi[0]+1}, C{combi[1]+1}): {me.overlap(cluster1_data, cluster2_data)}")
#     print()
#     print()

##############
# Question 5 #
##############

# # Printing precision, recall and F1-score for k = 3
# # To ensure that we get the best results,
# # we test every association of a cluster and a sentiment and keep the best one

# print("K = 3")
# clustered_data = cl.get_clustred_data_hierarchical(data, k=3, print_dendrogram=False)

# # We generate all possible permutations of the clusters
# perm = list(itertools.permutations(range(3), 3))

# # Each permutation is tested with 
# # the first cluster being associated with the -1 sentiment,
# # the second cluster being associated with the 0 sentiment,
# # and the third cluster being associated with the 1 sentiment
# precisions = []
# recalls = []
# f1_scores = []
# for p in perm:
#     clustered_data_copy = clustered_data.copy()
#     clustered_data_copy["cluster"] = clustered_data_copy["cluster"].replace(p[0], -1)
#     clustered_data_copy["cluster"] = clustered_data_copy["cluster"].replace(p[1], 0)
#     clustered_data_copy["cluster"] = clustered_data_copy["cluster"].replace(p[2], 1)
    
#     print(f"Permutation: Clusters {p} = sentiment (-1, 0, 1))")
#     precisions.append(me.precision(clustered_data_copy))
#     recalls.append(me.recall(clustered_data_copy))
#     f1_scores.append(me.f1_score(clustered_data_copy))
#     print(f"Precision: {precisions[-1]}")
#     print(f"Recall: {recalls[-1]}")
#     print(f"F1-score: {f1_scores[-1]}")
#     print()

# # We keep the permutation that gives the best f1-score
# best_perm = perm[f1_scores.index(max(f1_scores))]
# print(f"Best permutation: Clusters {best_perm} = sentiment (-1, 0, 1))")
# print(f"Precision: {precisions[perm.index(best_perm)]}")
# print(f"Recall: {recalls[perm.index(best_perm)]}")
# print(f"F1-score: {f1_scores[perm.index(best_perm)]}")
# print()
