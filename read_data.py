import pandas as pd

from Gene import Gene
from Label import Label


def get_labels() -> [Label]:
    df: pd.DataFrame = pd.read_csv('resources/labels.csv')
    return [Label(row) for index, row in df.iterrows()]


def get_genes() -> [Gene]:
    df: pd.DataFrame = pd.read_csv('resources/data.csv')
    return [Gene(row) for index, row in df.iterrows()]
