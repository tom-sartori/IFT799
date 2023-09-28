# Rapport TP1
## Groupe de travail
- Alexandre Theisse 23 488 180
- Louis-Vincent Capelli 23 211 533
- Tom Sartori 23 222 497

## Méthode 1 (sans visualisation des données)

## Méthode 2 (avec visualisation des données)
Nous avons choisi d'étudier les variables "gene_3" et "gene_4", qui ont une distribution assez similaire aux autres et ne possèdent pas trop de 0 contrairement à "gene_0" par exemple.

### Distribution des différentes classes (1D)
Nous avons donc créé 5 histogrammes pour chacune de ces variables, en affichant dans chaque histogramme les données correspondant à la classe correspondante. 

Le code utilisé pour générer ces histogrammes récupère les classes distinctes depuis le fichier *labels.csv* afin qu'il fonctionne peu importe le nombre de classes présentes dans le fichier.

![gene_3_hist](img/gene_3_hist.png)
![gene_4_hist](img/gene_4_hist.png)

On constate que l'allure des histogrammes est assez similaire pour les deux variables, avec une distribution qui semble gaussienne.

### Distribution des différentes classes (2D)
Nous avons donc créé 1 graphique en nuage de points qui permet d'afficher les valeurs de ces deux variables pour chacune des 5 classes.

![gene_3_4_scatter](img/genes_3_4_scatter.png)

Le graphique est assez difficile à interpréter du fait du manque de lisibilité. En effet, hormis la classe "COAD" qui semble est assez bien séparée des autres, les autres classes se superposent beaucoup trop pour pouvoir être distinguées.

On observe ce genre de graphiques pour la plupart des paires de variables que nous avons testées, ce qui appuie l'intérêt de méthode comme l'ACP, t-SNE ou UMAP qui permettent de réduire la dimensionnalité des données afin de mettre en évidence des tendances qui ne sont pas visibles en choisissant deux variables au hasard.

### Distribution des paires de classes (1D)
Parmi les 120 paires de classes possibles, nous avons choisi d'étudier les paires suivantes :
- "BRCA" et "COAD"
- "KIRC" et "COAD"
- "BRCA" et "KIRC"
En effet, ces paires de classes sont celles qui sont les plus facilement distinguables sur le graphique en nuage de points précédent et nous permettront donc de mieux visualiser les différences entre les classes.

Nous avons donc créé 1 histogramme pour chacune de ces 3 paires de classes, en affichant dans chaque histogramme les données correspondant aux 2 classes correspondantes et ce pour chacune des 2 variables. (Pour des raisons de lisibilité, nous avons choisi de ne joindre au rapport que les histogrammes pour la variable "gene_3")

![BRCA_COAD_hist](img/gene_3_BRCA_COAD.png)
![KIRC_COAD_hist](img/gene_3_KIRC_COAD.png)
![BRCA_KIRC_hist](img/gene_3_BRCA_KIRC.png)

On remarque en effet que les classes sont bien séparées sur les 2 premiers histogrammes, ce qui confirme l'intérêt de la méthode avec visualisation des données. 

Également on constate que la classe "BRCA" est sur-représentée par rapport aux autres classes ce qui peut avoir des implications lors d'analyses statistiques ou d'entrainement de modèles de machine learning.



### Distribution des paires de classes (2D)
De la même manière que pour les histogrammes, nous avons créé des graphiques en nuage de points qui permettent d'afficher les valeurs de ces deux variables pour chacune des 3 paires de classes mentionnées précédemment (BRCA/COAD, KIRC/COAD et BRCA/KIRC).

![BRCA_COAD_scatter](img/genes_3_4_BRCA_COAD.png)
![KIRC_COAD_scatter](img/genes_3_4_KIRC_COAD.png)
![BRCA_KIRC_scatter](img/genes_3_4_BRCA_KIRC.png)

Ces graphiques ne présentent aucune information supplémentaire par rapport au nuage de points contenant toutes les classes. Ils ont en revanche l'avantage d'être plus lisibles et donc plus facilement interprétables.

On retrouve sur les bords des *jointplot* (et notamment au-dessus pour la variable "gene_3") les tendances illustrées par les histogrammes des classes correspondantes, joints dans la partie précédente. 

### Distribution des données après transformation

#### ACP
L'ACP permet de réduire la dimensionnalité des données en les projetant sur un espace de dimension inférieure. Dans notre cas, nous avons choisi de projeter les données sur un espace de dimension 2 afin de pouvoir les afficher sur un graphique en nuage de points.

L'algorithme utilisé pour l'ACP est celui de la librairie *scikit-learn*.

![ACP](img/ACP.png)

Le fait de condenser les informations contenues dans l'ensemble des variables en 2 dimensions permet de mettre en évidence des tendances qui ne sont pas visibles en choisissant deux variables au hasard.

Les résultats montrent des classes qui sont mieux séparées que sur les graphiques en nuage de points précédents. On constate notamment que une classe "KIRC" bien distincte. 

#### t-SNE
De la même manière, nous avons utilisé l'algorithme de t-SNE de la librairie *scikit-learn* afin de projeter les données sur un espace de dimension 2.

![t-SNE](img/t-SNE.png)

Cette fois-ci, les classes sont encore mieux séparées que sur le graphique de l'ACP avec un seul outlier pour la classe "LUAD".

#### UMA
Le dernier algorithme que nous avons utilisé est celui de UMAP, issu de la librairie *umap-learn*.

Les données sont projetées sur un espace de dimension 2.

![UMAP](img/UMAP.png)

Les résultats sont similaires à ceux de t-SNE avec une meilleure séparation des classes malgré à nouveau au moins un outlier pour la classe "LUAD".

## Sources et références
- https://matplotlib.org/stable/api/figure_api.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
- https://stackoverflow.com/questions/10035446/how-can-i-make-a-blank-subplot-in-matplotlib
- https://seaborn.pydata.org/generated/seaborn.jointplot.html
- https://umap-learn.readthedocs.io/en/latest/