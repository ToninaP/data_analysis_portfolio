import pandas as pd
import numpy as np
import re
from cleaning_scripts.extract_first_number import extract_first_number


def clean_acquisition_year(df):
    """
    Clean and standardize acquisition year data from various possible column names.

    Parameters:
    df (pandas.DataFrame): Input DataFrame containing acquisition data

    Returns:
    pandas.DataFrame: DataFrame with new 'Year_acquisition' column
    """
    # List of possible column names for acquisition data
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

    # Initialize new column with NA values
    df["Year_acquisition"] = pd.NA
    found_column = False

    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            try:
                df["Year_acquisition"] = df[col].apply(extract_first_number)

                # Basic validation: years should be between 1000 and current year
                current_year = pd.Timestamp.now().year
                mask = (df["Year_acquisition"] >= 1000) & (
                    df["Year_acquisition"] <= current_year
                )
                df.loc[~mask, "Year_acquisition"] = pd.NA

                # Calculate statistics
                count_nans = df["Year_acquisition"].notna().sum()
                total_rows = len(df)
                coverage_percent = (count_nans / total_rows) * 100

                print(f"Data found in column: {col}")
                print(
                    f"Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
                )
                print("|----------------------------------|")

                found_column = True
                break

            except Exception as e:
                print(f"Error processing column {col}: {str(e)}")
                continue

    if not found_column:
        print("Data is not found in any expected columns")

    return df


def analyze_acquisition_columns(df):

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
            # Keep rows where original column has data but Year_acquisition is NA
            problematic_rows = df[
                (df[col].notna()) & (df["Year_acquisition"].isna())
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


def improve_acquisition_pompidou(df):
    """
    Using this function we assume that inventory number contains acquisition year.
    For rows that do not have data about acquisition we will insert value from inventory number.
    """

    # Function to extract year using regex
    def extract_pompidou_year(text):
        if pd.isna(text):
            return pd.NA
        # Look for pattern 'AM YYYY-' where YYYY is between 1800 and 2024
        match = re.findall(r"AM (1[89]\d{2}|20[01]\d|202[01234])-.*", str(text))
        if match:
            return int(match[0])
        return pd.NA

    # Create mask for problematic rows
    mask = (df["acquisition_date"].notna()) & (df["Year_acquisition"].isna())

    # Apply the extraction directly to the main DataFrame
    df.loc[mask, "Year_acquisition"] = df.loc[mask, "object_inventory"].apply(
        extract_pompidou_year
    )

    # mark changes
    df.loc[mask, "source_column"] = "object_inventory"

    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Year_acquisition"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Year_acquisition"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"Pompidou - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_acquisition_whitney(df):
    """
    Using this function we assume that accession_number contains acquisition year.
    Another assumption is that in all cells with "93.81a-aa" data the first number is the year 19XX
    For rows that do not have data about acquisition we will insert value from accession_number number.
    """

    # create a tailored function for this dataset
    def extract_whitney_year(text):
        if pd.isna(text):
            return pd.NA

        # Strip 'P.' from the start or end of the string, and get the part before the first '.'
        result = (
            text.lower().strip("p.").strip("sc.").strip("c.").strip("x").split(".")[0]
        )

        # Check if result is numeric (this ensures we're dealing with a year-like string)
        if result.isdigit():
            # Data before 2000 (2-digit year)
            if len(result) == 2:
                date = "19" + result
                return int(date)
            # Data after 2000 (4-digit year)
            elif len(result) == 4:
                return int(result)

        return pd.NA

    # Create mask for problematic rows
    mask = (df["credit_line"].notna()) & (df["Year_acquisition"].isna())

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Year_acquisition"] = df.loc[mask, "accession_number"].apply(
        extract_whitney_year
    )

    # mark changes

    df.loc[mask, "source_column"] = "accession_number"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Year_acquisition"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Year_acquisition"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"Whitney - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_acquisition_nga(df):
    """
    Using this function we use data in locationid
    data example: 'Lila Oliver Asher; gift to NGA, 2000.'
    """
    # Create mask for problematic rows
    mask = (df["accessionnum"].notna()) & (df["Year_acquisition"].isna())

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Year_acquisition"] = df.loc[mask, "locationid"].apply(
        extract_first_number
    )

    # mark changes
    df.loc[mask, "source_column"] = "locationid"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Year_acquisition"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Year_acquisition"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"Natonal Gallery - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_acquisition_kiasma(df):
    """
    Using this function we add data from acquisition?

    """
    # Create mask for problematic rows
    mask = (df["inventoryNumber"].notna()) & (df["Year_acquisition"].isna())

    # Apply the date extraction directly to the main DataFrame
    df.loc[mask, "Year_acquisition"] = df.loc[mask, "acquisition?"].apply(
        extract_first_number
    )

    # mark changes
    df.loc[mask, "source_column"] = "acquisition?"
    # Print summary of improvements
    total_fixed = mask.sum() - df[mask]["Year_acquisition"].isna().sum()
    print(f"Fixed {total_fixed} out of {mask.sum()} problematic rows")
    count_nans = df["Year_acquisition"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100

    print(
        f"Kiasma - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df


def improve_acquisition_ateneum(df):
    """
    Extract years from inventoryNumber field to fill missing Year_acquisition values.
    """

    def extract_ateneum_year(text):
        if pd.isna(text):
            return pd.NA

        text = str(text).strip()
        patterns = [
            r"A-?((?:19|20)\d{2})-\d+",  # A-2016-130
            r"N-?((?:19|20)\d{2})-\d+",  # N-2010-68
            r"TN-?((?:19|20)\d{2})-\d+",  # TN-1994-161
            r"[A-Z] [IVX]+ (\d{4})",  # C V 1893
            r"[A-Z][- ][IVX]+[- ](\d{4})",  # With hyphens
            r"N-?((?:19|20)\d{2})-\d+:[A-F]+",  # N-1998-44:A-F
            r"A[- ]III[- ](19\d{2}):\d+",  # A III 1924:78
            r"(?:^|\s)((?:18|19|20)\d{2})(?:\s|$|[:-])",  # Generic year
        ]

        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return int(match.group(1) if match.groups() else match.group())
        return pd.NA

    mask = df["inventoryNumber"].notna()
    update_mask = mask & (df["Year_acquisition"].isna())
    df.loc[update_mask, "Year_acquisition"] = df.loc[mask, "inventoryNumber"].apply(
        extract_ateneum_year
    )
    df.loc[update_mask, "source_column"] = "inventoryNumber"

    count_nans = df["Year_acquisition"].notna().sum()
    total_rows = len(df)
    coverage_percent = (count_nans / total_rows) * 100
    # Print summary of improvements
    total_fixed = update_mask.sum() - df[update_mask]["Year_acquisition"].isna().sum()
    print(f"Fixed {total_fixed} out of {update_mask.sum()} problematic rows")
    print(
        f"Ateneum - Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
    )
    print("---------------------------------------")
    return df.copy()


def find_outliers(df):
    # Print summary statistics for the cleaned years
    valid_years = df["Year_acquisition"].dropna()
    if len(valid_years) > 0:
        print("\nYear statistics:")
        print(f"Earliest year: {valid_years.min()}")
        print(f"Latest year: {valid_years.max()}")
        print(f"Median year: {valid_years.median()}")

        # Flag potential outliers
        q1 = valid_years.quantile(0.25)
        q3 = valid_years.quantile(0.75)
        iqr = q3 - q1
        outliers = valid_years[
            (valid_years < (q1 - 1.5 * iqr)) | (valid_years > (q3 + 1.5 * iqr))
        ]
        if len(outliers) > 0:
            print(f"\nPotential outliers detected ({len(outliers)} values):")
            print(outliers.value_counts().head())
            print("|----------------------------------|")
