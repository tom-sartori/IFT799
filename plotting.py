###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

from os import path
import matplotlib.pyplot as plt
import seaborn as sns

def plot_conjoint_representation(data, feature1, feature2, save=False, show=True):
    """
    Plots a conjoint representation of the distribution of 2 features as histograms.
    :param data: the data to plot
    :param feature1: the first feature
    :param feature2: the second feature
    """
    plt.figure()
    plt.hist(data[feature1], bins=30, alpha=0.5, label=feature1)
    plt.hist(data[feature2], bins=30, alpha=0.5, label=feature2)
    plt.legend(loc='upper right')
    plt.title("Conjoint representation of " + feature1 + " and " + feature2)
    plt.xlabel("Intensity")
    plt.ylabel("Number of occurences")
    if save:
        name = "conjoint_representation_" + feature1 + "_" + feature2 + ".png"
        plt.savefig(path.join("rapport", "img", name), bbox_inches='tight')
    if show:
        plt.show()
