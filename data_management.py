###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import pandas as pd

def get_all_users():
    with open("data/dataTp2.csv", "r") as f:
        lines = f.readlines()
        users = []
        for line in lines[1:]:
            line = line.strip()
            if line == "":
                continue
            line = line.split(",")[1:]
            users.append({"valence_intensity": line[0], "fear_intensity": line[1], "anger_intensity": line[2], "happiness_intensity": line[3], "sadness_intensity": line[4], "sentiment": line[5]})
    return users

def get_all_users_as_df():
    df = pd.read_csv("data/dataTp2.csv")
    df = df.drop(columns=["Unnamed: 0"])
    return df

def get_one_column_as_df(column_name):
    df = pd.read_csv("data/dataTp2.csv")
    return df[column_name]

if __name__ == "__main__":
    print(get_all_users_as_df())
    print(get_one_column_as_df("valence_intensity"))