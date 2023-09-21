import pandas as pd


class Label:

    def __init__(self, row: pd.Series):
        self.sample: str = row.iloc[0]
        self.cls: str = row.iloc[1]
