#Importation librairies
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot import Histogramme_comparaison
#lecture du fichier csv
df = pd.read_csv('resources/dataTp2.csv', sep = ',')
#séparation des données en 6 tableaux différents pour chaque colonne
df1 = df.iloc[:,0]
df2 = df.iloc[:,1]
df3 = df.iloc[:,2]
df4 = df.iloc[:,3]
df5 = df.iloc[:,4]
df6 = df.iloc[:,5]
df7 = df.iloc[:,6]



if __name__ == '__main__':
#Affichage des données en histogramme 
    Histogramme_comparaison()



