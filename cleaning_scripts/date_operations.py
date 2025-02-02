import pandas as pd
from extract_first_number import extract_first_number


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

    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            df["Year_acquisition"] = df[col].apply(extract_first_number)
            break  # Exit loop once we find the first match

    # print the number of nans in the new colums

    # create a new dataframe with not empty original column and empty target column
    # so I can manually check that the code did not miss a thing

    # print dates in the chronological order to find outliers

    return df
