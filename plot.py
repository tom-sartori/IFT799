import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('resources/dataTp2.csv', sep = ',')
#séparation des données en 6 tableaux différents pour chaque colonne
df1 = df.iloc[:,0]
df2 = df.iloc[:,1]
df3 = df.iloc[:,2]
df4 = df.iloc[:,3]
df5 = df.iloc[:,4]
df6 = df.iloc[:,5]
df7 = df.iloc[:,6]

def Histogramme_comparaison():
    plt.figure(0)
    plt.hist(df2, bins = 10, alpha=0.5, color = 'blue',label="valence_intensity", edgecolor = 'black')
    plt.hist(df3, bins = 10, alpha=0.5, color = 'green',label="fear_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('Valence and fear intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of valence and fear intensity')
    plt.figure(1)
    plt.hist(df2, bins = 10, alpha=0.5, color = 'blue',label="valence_intensity", edgecolor = 'black')
    plt.hist(df4, bins = 10, alpha=0.5, color = 'green',label="anger_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('Valence and anger intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of valence and anger intensity')
    plt.figure(2)
    plt.hist(df2, bins = 10, alpha=0.5, color = 'blue',label="valence_intensity", edgecolor = 'black')
    plt.hist(df5, bins = 10, alpha=0.5, color = 'green',label="happiness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('Valence and happiness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of valence and happiness intensity')
    plt.figure(3)
    plt.hist(df2, bins = 10, alpha=0.5, color = 'blue',label="valence_intensity", edgecolor = 'black')
    plt.hist(df6, bins = 10, alpha=0.5, color = 'green',label="sadness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('Valence and sadness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of valence and sadness intensity')
    
    plt.figure(4)
    plt.hist(df3, bins = 10, alpha=0.5, color = 'blue',label="fear_intensity", edgecolor = 'black')
    plt.hist(df4, bins = 10, alpha=0.5, color = 'green',label="anger_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('fear and anger intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of fear and anger intensity')
    plt.figure(5)
    plt.hist(df3, bins = 10, alpha=0.5, color = 'blue',label="fear_intensity", edgecolor = 'black')
    plt.hist(df5, bins = 10, alpha=0.5, color = 'green',label="happiness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('fear and happiness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of fear and happiness intensity')
    plt.figure(6)
    plt.hist(df3, bins = 10, alpha=0.5, color = 'blue',label="fear_intensity", edgecolor = 'black')
    plt.hist(df6, bins = 10, alpha=0.5, color = 'green',label="sadness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('fear and sadness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of fear and sadness intensity')

    plt.figure(7)
    plt.hist(df4, bins = 10, alpha=0.5, color = 'blue',label="anger_intensity", edgecolor = 'black')
    plt.hist(df5, bins = 10, alpha=0.5, color = 'green',label="happiness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('anger and happiness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of anger and happiness intensity')
    plt.figure(8)
    plt.hist(df4, bins = 10, alpha=0.5, color = 'blue',label="anger_intensity", edgecolor = 'black')
    plt.hist(df6, bins = 10, alpha=0.5, color = 'green',label="sadness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('anger and sadness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of anger and sadness intensity')

    plt.figure(9)
    plt.hist(df5, bins = 10, alpha=0.5, color = 'blue',label="happiness_intensity", edgecolor = 'black')
    plt.hist(df6, bins = 10, alpha=0.5, color = 'green',label="sadness_intensity", edgecolor = 'black')
    plt.legend(loc='upper right')
    plt.xlabel('Happiness and sadness intensity')
    plt.ylabel('Number of people')
    plt.title('Histogram of Happiness and sadness intensity')
    plt.show()
    