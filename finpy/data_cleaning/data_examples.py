import pandas as pd


def generate_example_dataframe():
    df = pd.read_csv('./tests/test_data/test_data_two.csv')
    return df
