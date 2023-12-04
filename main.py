#import 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    #lecture du fichier movies.csv et stockage dans une variable
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
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
    for i in movies.index:
        if movies.loc[i, 'genres'] == '(no genres listed)':
            id= movies.loc[i, 'movieId']
            ratings.drop(ratings[ratings['movieId'] == id].index, inplace = True)
            movies.drop(i, inplace = True)
    
    #changements des notes par des notes entieres
    ratings['rating'] = ratings['rating'].apply(np.floor)
    
    
    movies.to_csv('movies1.csv', index=False)
    ratings.to_csv('ratings1.csv', index=False)
    movies1 = pd.read_csv('movies1.csv')
    #initialisation d'une matrice de 0 de taille nombre de films dans movies1 * nombre de genres
    matrice = np.zeros((len(movies1), len(genres_count[1:])))
    #parcours des films
    for i in movies1.index:
        #parcours des genres
        for j in genres_count[1:].index:
            #si le film a le genre j
            if j in movies1.loc[i, 'genres']:
                #on met 1 dans la matrice
                matrice[i][j] = 1
    #affichage de la matrice
    print(matrice)
    
    
    #affichage du diagramme
    plt.show()
    
    
