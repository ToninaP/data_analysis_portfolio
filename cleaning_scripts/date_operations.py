import pandas as pd
from cleaning_scripts.extract_first_number import extract_first_number


def clean_acquisition_year(df):
    # List of possible column names for the artist name
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
    df["Year_acquisition"] = pd.NA
    # print a message when found a column
    found_column = False
    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            df["Year_acquisition"] = df[col].apply(extract_first_number)
            print(f"Artist name found in column: {col}")
            found_column = True
            # print the number of nans in the new colums
            count_nans = df["Year_acquisition"].isna().sum()
            print(f"Number of cleaned variables: {count_nans} out of {len(df)}")
            break  # Exit loop once we find the first match
        # If no artist was found in any column
        if not found_column:
            print(f"Artist name is not found in any expected columns")

    # create a new dataframe with not empty original column and empty target column
    # so I can manually check that the code did not miss a thing

    # print dates in the chronological order to find outliers

    return df
