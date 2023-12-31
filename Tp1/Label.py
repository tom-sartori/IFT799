###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import pandas as pd

from utils import distinct


class Label:

    def __init__(self, row: pd.Series):
        self.sample: str = row.iloc[0]
        self.cls: str = row.iloc[1]


def get_labels() -> [Label]:
    df: pd.DataFrame = pd.read_csv('resources/labels.csv')
    return [Label(row) for index, row in df.iterrows()]


def get_distinct_classes(labels: [Label]) -> [str]:
    return distinct([label.cls for label in labels])


def get_samples_by_class(labels: [Label], cls: str) -> [str]:
    return [label.sample for label in labels if label.cls == cls]
