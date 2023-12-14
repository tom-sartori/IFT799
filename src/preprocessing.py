###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import src.data as data

from sklearn.cluster import SpectralClustering
import numpy as np


def five_closest_users(ratings):
    """
    For each (userId, movieId, rating) tuple in the dataset, find the five closest users that have rated the movie.
    Returns a dictionary with (userId, movieId, rating) tuples as keys and a list of the notes of the five closest users as values.
    Ex : {(userId, movieId, rating) : [note1, note2, note3, note4, note5]}
    """
    
    # Computing stats on the dataset
    movies_map, movie_genre_matrix = data.movies_stats()
    users_map, users_profiles, users_seen_movies = data.users_stats(ratings, movie_genre_matrix, movies_map)

    # Normalizing users_profiles
    max_ = 0
    for u in range(len(users_profiles)):
        if np.max(users_profiles[u]) > max_:
            max_ = np.max(users_profiles[u])
    users_profiles /= max_

    # Computing the affinity matrix
    clustering = SpectralClustering(n_clusters=2, assign_labels="kmeans").fit(users_profiles)
    affinity_matrix = clustering.affinity_matrix_

    # Computing the five closest users that have seen the film for each (userId, movieId) pair
    five_closest_users_dict = {}
    for user_id, i in users_map.items():
        # Computing the five closest users
        closest_users = np.argsort(affinity_matrix[i])
        for movie_id, j in movies_map.items():
            if users_seen_movies[i, j] > 0:
                five_closest_users = []
                for other_user in closest_users:
                    if len(five_closest_users) == 5:
                        break
                    if users_seen_movies[other_user, j] > 0 and other_user != i:
                        five_closest_users.append(users_seen_movies[other_user, j])
                if len(five_closest_users) == 5:
                    five_closest_users_dict[(user_id, movie_id, users_seen_movies[i, j])] = five_closest_users

    return five_closest_users_dict
