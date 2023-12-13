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