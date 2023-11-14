###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import itertools

import data_management as dm
import plotting as pl


# Question 1

features = ["valence_intensity", "fear_intensity", "anger_intensity", "happiness_intensity", "sadness_intensity"]
# All possible combinations of 2 features
combinations = list(itertools.combinations(features, 2))

# Plots distributions of all combinations of 2 features
data = dm.get_all_users_as_df()
for combi in combinations:
    pl.plot_conjoint_representation(data, combi[0], combi[1])
    # pl.plot_conjoint_representation(data, combi[0], combi[1], save=True, show=False)
