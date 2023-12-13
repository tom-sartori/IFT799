import pandas as pd

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