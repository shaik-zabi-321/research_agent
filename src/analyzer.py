
import pandas as pd


def inspect_dataset(df):
    """
    Inspect a dataset and return its basic information.
    """

    total_rows = df.shape[0]
    total_columns = df.shape[1]

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    missing_values = df.isnull().sum()

    missing_percentage = (
        missing_values / total_rows * 100
        if total_rows > 0 else missing_values
    )

    return {
        "rows": total_rows,
        "columns_count": total_columns,
        "column_names": df.columns.tolist(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns,
        "missing_values": missing_values.to_dict(),
        "missing_percentage": missing_percentage.to_dict(),
        "summary": df.describe(include="all").to_dict()
    }


def data_quality_report(df):
    """
    Identify basic data quality issues.
    """

    missing_values = df.isnull().sum()

    total_rows = df.shape[0]

    missing_percentage = (
        missing_values / total_rows * 100
        if total_rows > 0 else missing_values
    )

    duplicate_rows = int(df.duplicated().sum())

    unique_values = df.nunique()

    constant_columns = unique_values[
        unique_values == 1
    ].index.tolist()

    return {
        "missing_values": missing_values.to_dict(),
        "missing_percentage": missing_percentage.to_dict(),
        "duplicate_rows": duplicate_rows,
        "unique_values": unique_values.to_dict(),
        "constant_columns": constant_columns
    }
