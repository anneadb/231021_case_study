"""Case study."""
import pandas as pd

DATE_COLUMN = "Datum (Anlage)"
TIMESTAMP_COLUMN = "Zeit (Anlage)"

INT_COLUMNS = [
    "Nacelle Position (avg)",
    "Feature 0",
    "Feature 34",
    "Feature 36",
    "Feature 54",
    "Feature 57",
    "Feature 61",
    "Feature 62",
]

FLOAT_COLUMNS = ["Feature 26"]

INCONSISTENT_COLUMNS = ["Wind Speed (avg)", "Active Power (avg)"]


def drop_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Drops rows that may skew data analysis.

    Args:
        df: pandas DataFrame

    Returns:
        pandas DataFrame
    """
    # days with too few data entries
    date_count = df[DATE_COLUMN].value_counts(sort=False).reset_index()
    date_list = date_count[date_count["count"] == 1][DATE_COLUMN]

    new_df = df[~df[DATE_COLUMN].isin(date_list)]

    # duplicate timestamps
    new_df = new_df.drop_duplicates(subset=[TIMESTAMP_COLUMN]).reset_index(drop=True)

    return new_df


def transform_column_types(df: pd.DataFrame) -> None:
    """Transforms the column types for columns which were not classified correctly.

    Changes to the dataframe are happening inplace.

    Args:
        df: pandas DataFrame
    """
    # datetime
    df[TIMESTAMP_COLUMN] = pd.to_datetime(
        df[DATE_COLUMN] + df[TIMESTAMP_COLUMN], format="%d.%m.%y%H:%M:%S"
    )
    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN], format="%d.%m.%y")

    for column in INT_COLUMNS:
        try:
            df[column] = df[column].astype("Int64")
        except ValueError:
            df[column] = df[column].astype(float)
            df[column] = df[column].astype("Int64")

    for column in FLOAT_COLUMNS:
        df[column] = df[column].astype(float)

    for column in INCONSISTENT_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")


def drop_columns(df: pd.DataFrame) -> None:
    """Drop columns with little or no information value.

    Changes to the dataframe are happening inplace.

    Args:
        df: pandas DataFrame
    """
    columns_to_drop = ["Unnamed: 0"]
    for column in df.columns.values:
        percentage_missing = df[column].isnull().sum() * 100 / len(df)
        if percentage_missing >= 98:
            columns_to_drop.append(column)
            continue

        unique_values = len(df[column].dropna().unique())
        if unique_values == 1:
            columns_to_drop.append(column)
            continue

        temp_df = df[column].value_counts().reset_index()
        temp_df["percentage"] = temp_df["count"] / sum(temp_df["count"])
        if temp_df["percentage"].max() >= 0.98:
            columns_to_drop.append(column)

    df.drop(columns_to_drop, axis=1, inplace=True)

    print(f"Dropped {len(columns_to_drop)} columns:", columns_to_drop)


if __name__ == "__main__":
    df = pd.read_csv("example_raw_data.csv", sep=";", decimal=",")

    drop_columns(df)
    transform_column_types(df)
    df = drop_rows(df)

    df.to_csv("output.csv", sep=";", index=False, decimal=",")
    print("Export completed.")
