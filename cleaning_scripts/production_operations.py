import pandas as pd
import re
from cleaning_scripts.extract_first_number import extract_first_number


def artwork_creation_date(df):
    possible_columns = [
        "Object Date",
        "year_production",
        "year",
        "object_date",
        "Date",
        "display_date",
        "endyear_x",
        "yearFrom",
        "production_date_0_end",
        "DateCreated",
    ]

    df["Date_creation_year"] = pd.NA
    found_column = False

    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            df["Date_creation_year"] = df[col].apply(extract_first_number)
            # Basic validation: years should be between 1000 and current year
            current_year = pd.Timestamp.now().year
            mask = (df["Date_creation_year"] >= 1000) & (
                df["Date_creation_year"] <= current_year
            )
            df.loc[~mask, "Date_creation_year"] = pd.NA

            # Calculate statistics
            count_nans = df["Date_creation_year"].notna().sum()
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


def analyze_production_columns(df):

    diagnostic_results = []
    possible_columns = [
        "acquisition_date",
        "credit_line",
        "AccessionYear",
        "artwork_acquisition",
        "year_adquisition",
        "acquisitionYear",
        "DateAcquired",
        "accession_number",
        "accessionnum",
        "inventoryNumber",
        "acquisition_date_precision",
        "AcquiredDate",
    ]

    for col in possible_columns:
        if col in df.columns:
            # Keep rows where original column has data but Date_creation_year is NA
            problematic_rows = df[
                (df[col].notna()) & (df["Date_creation_year"].isna())
            ].copy()

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


def improve_production_met(df):
    """
    Using this function we add data from "Object End Date" column
    """
    # Create mask for problematic rows
    mask = (df["Object Date"].notna()) & (df["Date_creation_year"].isna())

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Date_creation_year"] = df.loc[mask, "Object End Date"].apply(
        extract_first_number
    )

    # mark changes
    df.loc[mask, "source_column"] = "Object End Date"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Date_creation_year"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Date_creation_year"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"MET - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_production_moma(df):
    """
    Using this function we use the same column, but change the regex pattern
    """
    # Create mask for problematic rows
    mask = (df["Date"].notna()) & (df["Date_creation_year"].isna())

    # Function to extract year using regex
    def extract_moma_prod(text):
        if pd.isna(text):
            return pd.NA
        # Look for pattern
        match = re.findall(r"(1[89]\d{2}).*", str(text))
        if match:
            return int(match[0])
        return pd.NA

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Date_creation_year"] = df.loc[mask, "Date"].apply(extract_moma_prod)

    # mark changes
    df.loc[mask, "source_column"] = "Date"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Date_creation_year"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Date_creation_year"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"MOMA - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_production_whitney(df):
    """
    Using this function we use the same column, but change the regex pattern
    """
    # Create mask for problematic rows
    mask = (df["display_date"].notna()) & (df["Date_creation_year"].isna())

    # Function to extract year using regex
    def extract_moma_prod(text):
        if pd.isna(text):
            return pd.NA
        # Look for pattern
        match = re.findall(r"(1[89]\d{2}).*", str(text))
        if match:
            return int(match[0])
        return pd.NA

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Date_creation_year"] = df.loc[mask, "display_date"].apply(
        extract_moma_prod
    )

    # mark changes
    df.loc[mask, "source_column"] = "display_date"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Date_creation_year"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Date_creation_year"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"whitney - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_production_nga(df):
    """
    use regex formula on another column
    """
    # Create mask for problematic rows
    mask = (df["endyear_x"].notna()) & (df["Date_creation_year"].isna())

    # Function to extract year using regex
    def extract_moma_prod(text):
        if pd.isna(text):
            return pd.NA
        # Look for pattern
        match = re.findall(r"(1[89]\d{2}).*", str(text))
        if match:
            return int(match[0])
        return pd.NA

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Date_creation_year"] = df.loc[mask, "displaydate_x"].apply(
        extract_moma_prod
    )

    # mark changes
    df.loc[mask, "source_column"] = "displaydate_x"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Date_creation_year"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Date_creation_year"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"NGA - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_production_queensland(df):
    """
    use another regex formula on original column
    """
    # Create mask for problematic rows
    mask = (df["DateCreated"].notna()) & (df["Date_creation_year"].isna())

    # Function to extract year using regex
    def extract_moma_prod(text):
        if pd.isna(text):
            return pd.NA
        # Look for pattern
        match = re.findall(r"(1[89]\d{2}).*", str(text))
        if match:
            return int(match[0])
        return pd.NA

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Date_creation_year"] = df.loc[mask, "DateCreated"].apply(
        extract_moma_prod
    )

    # mark changes
    df.loc[mask, "source_column"] = "DateCreated"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Date_creation_year"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Date_creation_year"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"Queensland - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df
