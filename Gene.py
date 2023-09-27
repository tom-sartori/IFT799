#####
# Alexandre Theisse 23 488 180
# Louis-Vincent Capelli 23 211 533
# Tom Sartori 23 222 497
###

import pandas as pd


class Gene:

    def __init__(self, row: pd.Series):
        self.sample: str = row.iloc[0]
        self.genes: [float] = row.iloc[1:].values.tolist()


def get_genes() -> [Gene]:
    df: pd.DataFrame = pd.read_csv('resources/data.csv')
    return [Gene(row) for index, row in df.iterrows()]


def get_genes_by_samples(genes: [Gene], samples: [str]) -> [[float]]:
    return [gene.genes for gene in genes if gene.sample in samples]
