#import 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    #lecture du fichier movies.csv et stockage dans une variable
    movies = pd.read_csv('movies.csv')
    #récupération des genres
    genres = movies['genres'].str.split('|', expand=True)
    #affichage des genres
    
    print(genres)
    #création d'un diagramme en baton pour afficher le nombre de films par genre
    genres_count = genres.apply(pd.Series.value_counts).sum(axis=1)
    print(genres_count[1:])
    genres_count[1:].plot.bar()
    plt.title('Nombre de films par genre')
    plt.xlabel('Genre')
    plt.ylabel('Nombre de films')
  
    #Creation d'un nouveau csv supprimant les colonnes des films sans genres
    movies.drop(movies[movies['genres'] == '(no genres listed)'].index, inplace = True)
    movies.to_csv('movies1.csv', index=False)
    
    #affichage du diagramme
    plt.show()
    
    
