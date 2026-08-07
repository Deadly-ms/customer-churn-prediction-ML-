import pandas as pd

from config import CLEAN_DATASET_PATH
from data_loader import DataLoader


class DataPreprocessor:

    def __init__(self):
        pass

    def remove_customer_id(self, df):
        """
        Remove customerID column.
        """

        print("\nRemoving customerID column...")

        df = df.drop("customerID", axis=1)

        return df

    def convert_total_charges(self, df):
        """
        Convert TotalCharges to numeric.
        """

        print("Converting TotalCharges to numeric...")

        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

        return df

    def remove_missing_values(self, df):
        """
        Remove rows containing missing values.
        """

        print("Removing missing values...")

        before = len(df)

        df = df.dropna()

        after = len(df)

        print(f"Removed {before-after} rows.")

        return df

    def check_duplicates(self, df):
        """
        Display duplicate rows.
        """

        duplicates = df.duplicated().sum()

        print(f"Duplicate Rows : {duplicates}")

        return df

    def dataset_summary(self, df):
        """
        Display dataset summary.
        """

        print("\nDataset Shape")
        print(df.shape)

        print("\nData Types")
        print(df.dtypes)

        return df

    def save_dataset(self, df):
        """
        Save cleaned dataset.
        """

        df.to_csv(
            CLEAN_DATASET_PATH,
            index=False
        )

        print("\nClean dataset saved successfully!")

        print(CLEAN_DATASET_PATH)


if __name__ == "__main__":

    loader = DataLoader()

    df = loader.load_data()

    preprocessor = DataPreprocessor()

    df = preprocessor.remove_customer_id(df)

    df = preprocessor.convert_total_charges(df)

    df = preprocessor.remove_missing_values(df)

    df = preprocessor.check_duplicates(df)

    preprocessor.dataset_summary(df)

    preprocessor.save_dataset(df)

    print("\nData preprocessing completed successfully.")