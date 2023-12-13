import pandas as pd

def load_movies():
    """Load all movies from CSV file into Pandas DataFrame."""
    movies = pd.read_csv("data/movies.csv")
    movies["genres"] = movies["genres"].str.split("|")
    movies = movies.drop("movieId", axis=1)
    return movies

def load_movies_with_genres():
    """Load all movies with a genre from CSV file into Pandas DataFrame."""
    movies = pd.read_csv("data/movies1.csv")
    movies["genres"] = movies["genres"].str.split("|")
    movies = movies.drop("movieId", axis=1)
    return movies