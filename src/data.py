import pandas as pd
import numpy as np


def load_movies():
    """Load all movies from CSV file into Pandas DataFrame."""
    movies = pd.read_csv("data/movies.csv")
    movies["genres"] = movies["genres"].str.split("|")
    return movies

def load_movies_with_genre():
    """Load all movies with a genre from CSV file into Pandas DataFrame."""
    movies = pd.read_csv("data/movies1.csv")
    movies["genres"] = movies["genres"].str.split("|")
    return movies

def load_ratings():
    """Load all ratings from CSV file into Pandas DataFrame."""
    ratings = pd.read_csv("data/ratings.csv")
    ratings = ratings.drop("timestamp", axis=1)
    return ratings

def load_ratings_with_genre():
    """Load all ratings of a wovie with a genre from CSV file into Pandas DataFrame."""
    ratings = pd.read_csv("data/ratings1.csv")
    ratings = ratings.drop("timestamp", axis=1)
    return ratings

def load_train_ratings():
    """Load all train ratings from CSV file into Pandas DataFrame."""
    ratings = pd.read_csv("data/ratings_train.csv")
    ratings = ratings.drop("timestamp", axis=1)
    return ratings

def load_eval_ratings():
    """Load all eval ratings from CSV file into Pandas DataFrame."""
    ratings = pd.read_csv("data/ratings_evaluation.csv")
    ratings = ratings.drop("timestamp", axis=1)
    return ratings

def load_test_ratings():
    """Load all test ratings from CSV file into Pandas DataFrame."""
    ratings = pd.read_csv("data/ratings_test.csv")
    ratings = ratings.drop("timestamp", axis=1)
    return ratings

def unique_genres():
    """Return a list of all unique genres in the dataset ('no genres listed' excluded)."""
    movies = load_movies_with_genre()
    genres = []
    for genre in movies["genres"]:
        for g in genre:
            if g not in genres:
                genres.append(g)
    return genres

def unique_userIds(ratings):
    """Return a list of all unique userIds in the dataset."""
    ids = []
    for id_ in ratings["userId"]:
        if id_ not in ids:
            ids.append(id_)
    return ids

def movies_stats():
    """
    Building a binary matrix movie_genre_matrix where :
    movie_genre_matrix[i,j] = 1 if the movie i is of genre j and movie_genre_matrix[i,j] = 0 otherwise.

    Returns a tuple (movies_map, movie_genre_matrix) where movies_map is a dictionary that maps movie id to index in movie_genre_matrix.
    """

    movies = load_movies_with_genre()

    unique_genres_ = unique_genres()

    # Maps movie id to index in movie_genre_matrix
    movies_map = {movie_id: i for i, movie_id in enumerate(movies['movieId'])}

    movie_genre_matrix = np.zeros((len(movies_map), len(unique_genres_)))

    for i, movie_genres in enumerate(movies['genres']):
        for j, genre in enumerate(unique_genres_):
            if genre in movie_genres:
                movie_genre_matrix[i, j] = 1

    return movies_map, movie_genre_matrix

def users_stats(ratings, movie_genre_matrix, movies_map):
    """
    Computing the profile vector of each user u, 
    where the k-th coordinate of the profile vector of u is the sum of the ratings given by u to the movies of genre k.
    The profiles are stored in a matrix users_profiles where the k-th row is the profile vector of the user k.

    Also computing a binary matrix users_seen_movies where :
    users_seen_movies[i,j] = 1 if the user i has seen the movie j and users_seen_movies[i,j] = 0 otherwise.

    Returns a tuple (users_map, users_profiles, users_seen_movies) where users_map is a dictionary that maps user id to index in users_profiles.
    """

    # Load the ratings dataset
    ratings = ratings.copy()
    
    users = unique_userIds(ratings)
    # Maps user id to index in users_profiles
    users_map = {user: i for i, user in enumerate(users)}

    users_profiles = np.zeros((len(users), len(unique_genres())))
    users_seens_movies = np.zeros((len(users), len(movies_map)))


    for _, rating in ratings.iterrows():
        users_profiles[users_map[rating['userId']]] += rating['rating'] * movie_genre_matrix[movies_map[rating['movieId']]]
        users_seens_movies[users_map[rating['userId']], movies_map[rating['movieId']]] = 1

    return users_map, users_profiles, users_seens_movies