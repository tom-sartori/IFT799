import pandas as pd


class Gene:

    def __init__(self, row: pd.Series):
        self.sample = row.iloc[0]
        self.genes = row.iloc[1:].values
