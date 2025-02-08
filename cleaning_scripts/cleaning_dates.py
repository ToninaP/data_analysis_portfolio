import pandas as pd
import re
from cleaning_scripts.extract_first_number import (
    extract_first_number,
    extract_last_number,
)


def extract_date(df, possible_columns, new_column_name):

    df[new_column_name] = pd.NA
    found_column = False

    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            df[new_column_name] = df[col].apply(extract_first_number)
            # Basic validation: years should be between 1000 and current year
            current_year = pd.Timestamp.now().year
            mask = (df[new_column_name] >= 1000) & (df[new_column_name] <= current_year)
            df.loc[~mask, new_column_name] = pd.NA

            # Calculate statistics
            count_nans = df[new_column_name].notna().sum()
            total_rows = len(df)
            coverage_percent = (count_nans / total_rows) * 100

            print(f"Data found in column: {col}")
            print(
                f"Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
            )
            print("----------------------------------")

            found_column = True
            break  # Exit loop once we find the first match
    if not found_column:
        print("Data is not found in any expected columns")

    return df


def analyze_data_quality(df, possible_columns, new_column_name):

    diagnostic_results = []

    for col in possible_columns:
        if col in df.columns:
            # Keep rows where original column has data but new_column_name is NA
            problematic_rows = df[
                (df[col].notna()) & (df[new_column_name].isna())
            ].copy()
            print(f"Data taken from column {col}")

            if not problematic_rows.empty:
                # Add column name for reference
                problematic_rows["source_column"] = col
                diagnostic_results.append(problematic_rows)

    # Combine all problematic rows into one DataFrame
    if diagnostic_results:
        diagnostic_df = pd.concat(diagnostic_results, ignore_index=True)
    else:
        diagnostic_df = pd.DataFrame()

    return diagnostic_df


def extract_date_from_other_column(
    df, new_column, column_with_main_data, column_with_more_data
):
    """
    case when we use ready function extract_first_date
    on another column
    """
    # Create mask for problematic rows
    mask = (df[column_with_main_data].notna()) & (df[new_column].isna())

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, new_column] = df.loc[mask, column_with_more_data].apply(
        extract_first_number
    )

    # mark changes
    df.loc[mask, "source_column"] = column_with_more_data
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask][new_column].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df[new_column].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"MET - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")

    return


def extract_last_date_from_other_column(
    df, new_column, column_with_main_data, column_with_more_data
):
    """
    case when we use ready function extract_last_date
    on another column
    """
    # Create mask for problematic rows
    mask = (df[column_with_main_data].notna()) & (df[new_column].isna())

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, new_column] = df.loc[mask, column_with_more_data].apply(
        extract_last_number
    )

    # mark changes
    df.loc[mask, "source_column"] = column_with_more_data
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask][new_column].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df[new_column].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"MET - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")

    return
