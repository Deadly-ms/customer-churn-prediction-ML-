import pandas as pd
from config import DATASET_PATH


class DataLoader:

    def __init__(self):
        self.dataset_path = DATASET_PATH

    def load_data(self):
        """
        Load the dataset from CSV.
        """

        try:
            df = pd.read_csv(self.dataset_path)

            print("=" * 50)
            print("Dataset Loaded Successfully")
            print("=" * 50)

            return df

        except FileNotFoundError:

            print("Dataset not found.")
            raise

    def dataset_shape(self, df):

        print("\nDataset Shape")
        print("-" * 30)

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

    def dataset_columns(self, df):

        print("\nColumn Names")
        print("-" * 30)

        for column in df.columns:
            print(column)

    def dataset_info(self, df):

        print("\nDataset Information")
        print("-" * 30)

        df.info()

    def first_rows(self, df):

        print("\nFirst Five Rows")
        print("-" * 30)

        print(df.head())

    def missing_values(self, df):

        print("\nMissing Values")
        print("-" * 30)

        print(df.isnull().sum())


if __name__ == "__main__":

    loader = DataLoader()

    df = loader.load_data()

    loader.dataset_shape(df)

    loader.dataset_columns(df)

    loader.dataset_info(df)

    loader.first_rows(df)

    loader.missing_values(df)