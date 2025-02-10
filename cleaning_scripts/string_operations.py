import pandas as pd
from cleaning_scripts.load_tags import (
    load_medium_tags,
    load_nationality_tags,
    load_acquisition_tags,
)


def create_artist_name_col(df):
    """
    The function creates a new column with Artist name based on the original column across several datasets

    Parameters:
        df (pandas.DataFrame): Input DataFrame containing artist information

    Returns:
        pandas.DataFrame: DataFrame with standardized Artist column
    """
    # List of possible column names for the artist name
    possible_columns = [
        "artist",
        "author",
        "artist_name",
        "Artist Display Name",
        "artist name",
        "Artist Display Name",
        "Artist",
        "artists",
        "forwarddisplayname",
        "production_0_creator",
        "display_name",
        "artist_0",
    ]

    found_artist = False

    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            df["Artist"] = df[col]
            print(f"Artist name found in column: {col}")
            found_artist = True
            break  # Exit the loop once we find the artist

    # If no artist was found in any column
    if not found_artist:
        print(f"Artist name is not found in any expected columns")

    return df


def create_artwork_title(df):
    # List of possible column names for the artist name
    possible_columns = [
        "object_title",
        "artwork_name",
        "Title",
        "url",
        "name",
        "title",
        "title_fi",
        "titles_0_title",
    ]
    found_artist = False
    # Loop over the possible column names and use the first one that exists
    for col in possible_columns:
        if col in df.columns:
            df["Title"] = df[col]
            print(f"Artwork title found in column: {col}")
            found_artist = True
            break  # Exit loop once we find the first match
    # If no artist was found in any column
    if not found_artist:
        print(f"Artwork title is not found in any expected columns")

    return df


def classify_medium(df):
    """
    Classifies artwork medium based on predefined columns and tags.

    Args:
        df (pandas.DataFrame): Input DataFrame containing artwork data

    Returns:
        pandas.DataFrame: DataFrame with added Medium_raw and Medium_classified columns
    """
    # Load medium tags
    medium_tags, medium_name = load_medium_tags()

    # iterate over columns to find medium data
    possible_columns = [
        "Medium",
        "type_artwork",
        "medium",
        "object_type",
        "Classification",
        "classification",
        "classifications_0_en",
        "object_names_1_name",
        "PhysicalCategory",
    ]

    # create Medium_raw and fill it with original data
    df["Medium_raw"] = pd.NA
    df["Medium_classified"] = pd.NA

    found_column = False
    for col in possible_columns:
        if col in df.columns:
            df["Medium_raw"] = df[col].str.lower()  # Fixed typo here
            print(f"Data found in column: {col}")
            found_column = True

            # Calculate statistics
            count_nans = df["Medium_raw"].notna().sum()
            total_rows = len(df)
            coverage_percent = (count_nans / total_rows) * 100
            print(
                f"Number of variables in the original column: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
            )
            break  # Exit loop once we find the first match

    if not found_column:
        print("Data is not found in any expected columns")
        return df

    # Only proceed with classification if we found data
    if found_column:
        # Iterate over each row in the DataFrame
        for idx, row in df.iterrows():
            medium = row["Medium_raw"]

            # Skip if the medium value is not a string
            if not isinstance(medium, str):
                continue

            # Check each tag group
            for i, tag_group in enumerate(medium_tags):
                # Check if any keyword from the tag group exists in the medium
                if any(tag.lower() in medium.lower() for tag in tag_group):
                    # Assign the corresponding medium name
                    df.at[idx, "Medium_classified"] = medium_name[i]
                    break  # Stop once we find a match

        # Calculate statistics after cleaning
        count_nans = df["Medium_classified"].notna().sum()
        total_rows = len(df)
        coverage_percent = (count_nans / total_rows) * 100
        print(
            f"Number of cleaned variables: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
        )
        print("----------------------------------")

        # Show a sample of the results
        print("\nSample of results:")
        print(df[["Medium_raw", "Medium_classified"]].head())

    return df


def create_artist_nationality(df):
    """
    Classifies artist nationality based on predefined columns and nationality tags.

    Args:
        df (pandas.DataFrame): Input DataFrame containing artist data

    Returns:
        pandas.DataFrame: DataFrame with added nationality_raw and Country_calculated columns
    """
    # Load nationality tags
    nationality_tags, country_name = load_nationality_tags()

    # Define possible columns for nationality information
    possible_columns = [
        "Country",
        "Artist Nationality",
        "nationality_artist",
        "artist_nationality",
        "Nationality",
        "nationality",
        "production_0_creator_nationality",
    ]

    # Initialize new columns
    df["nationality_raw"] = pd.NA
    df["Country_calculated"] = pd.NA

    # Find and process the first matching column
    found_column = False
    for col in possible_columns:
        if col in df.columns:
            print(f"Nationality data found in column: {col}")

            # Process the nationality string: lowercase, remove 'the', parentheses,
            # take first word, and strip commas
            df["nationality_raw"] = (
                df[col]
                .str.lower()
                .str.strip("the")
                .str.replace("(", "")
                .str.replace(")", "")
                .str.split(" ")
                .str[0]
                .str.strip(",")
            )

            # Calculate initial statistics
            count_nans = df["nationality_raw"].notna().sum()
            total_rows = len(df)
            coverage_percent = (count_nans / total_rows) * 100
            print(
                f"Number of variables in the original column: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
            )

            found_column = True
            break

    if not found_column:
        print("Nationality data not found in any expected columns")
        return df

    # Only proceed with classification if we found data
    if found_column:
        # Counter for matches
        match_count = 0

        # Iterate over each row in the DataFrame
        for idx, row in df.iterrows():
            nationality = row["nationality_raw"]

            # Skip if the nationality value is not a string
            if not isinstance(nationality, str):
                continue

            # Check each tag group
            for i, tag_group in enumerate(nationality_tags):
                # Check if any keyword from the tag group matches the nationality
                if any(tag.lower() in nationality.lower() for tag in tag_group):
                    # Assign the corresponding country name
                    df.at[idx, "Country_calculated"] = country_name[i]
                    match_count += 1
                    break  # Stop once we find a match

        # Calculate final statistics
        count_nans = df["Country_calculated"].notna().sum()
        total_rows = len(df)
        coverage_percent = (count_nans / total_rows) * 100
        print(f"\nMatches found: {match_count}")
        print(
            f"Number of classified nationalities: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
        )

        # Show sample of results
        print("\nSample of classification results:")
        print(df[["nationality_raw", "Country_calculated"]].head())
        print("----------------------------------")

    return df


def create_acquisition_method(df):
    """
    Classifies artwork acquisition methods based on credit line information.

    Args:
        df (pandas.DataFrame): Input DataFrame containing artwork acquisition data

    Returns:
        pandas.DataFrame: DataFrame with added acquisition_raw and Acquisition_classified columns
    """
    # Load acquisition tags
    acquisition_tags, acquisition_methods = load_acquisition_tags()

    # Define possible columns for acquisition information
    possible_columns = [
        "Credit Line",
        "creditLine",
        "acquisition_type",
        "CreditLine",
        "credit_line",
        "creditline",
        "CreditLine",
    ]

    # Initialize new columns
    df["acquisition_raw"] = pd.NA
    df["Acquisition_classified"] = pd.NA  # Fixed typo in column name

    # Find and process the first matching column
    found_column = False
    for col in possible_columns:
        if col in df.columns:
            print(f"Acquisition data found in column: {col}")

            # Process the acquisition string: lowercase
            df["acquisition_raw"] = df[col].str.lower()

            # Calculate initial statistics
            count_nans = df["acquisition_raw"].notna().sum()
            total_rows = len(df)
            coverage_percent = (count_nans / total_rows) * 100
            print(
                f"Number of variables in the original column: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
            )

            found_column = True
            break

    if not found_column:
        print("Acquisition data not found in any expected columns")
        return df

    # Only proceed with classification if we found data
    if found_column:
        # Counter for matches
        match_count = 0

        # Iterate over each row in the DataFrame
        for idx, row in df.iterrows():
            acquisition = row["acquisition_raw"]

            # Skip if the acquisition value is not a string
            if not isinstance(acquisition, str):
                continue

            # Check each tag group
            for i, tag_group in enumerate(acquisition_tags):
                # Check if any keyword from the tag group matches the acquisition text
                if any(tag.lower() in acquisition.lower() for tag in tag_group):
                    # Assign the corresponding acquisition method
                    df.at[idx, "Acquisition_classified"] = acquisition_methods[i]
                    match_count += 1
                    break  # Stop once we find a match

        # Calculate final statistics
        count_nans = df["Acquisition_classified"].notna().sum()
        total_rows = len(df)
        coverage_percent = (count_nans / total_rows) * 100
        print(f"\nMatches found: {match_count}")
        print(
            f"Number of classified acquisition methods: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
        )

        # Show sample of results
        print("\nSample of classification results:")
        print(df[["acquisition_raw", "Acquisition_classified"]].head())
        print("----------------------------------")

    return df


def create_artist_gender(df):
    """
    Classifies artist gender based on predefined columns and gender mapping.

    Args:
        df (pandas.DataFrame): Input DataFrame containing artist data

    Returns:
        pandas.DataFrame: DataFrame with added Gender_raw and Gender_classified columns
    """
    # Define possible columns for gender information
    possible_columns = [
        "Artist Gender",
        "gender",
        "artist_gender",
        "Gender",
        "production_0_creator_gender",
    ]

    # Define gender mapping dictionary
    gender_dict = {"female": ["female", "woman"], "male": ["male", "man"]}

    # Initialize new columns
    df["Gender_raw"] = pd.NA
    df["Gender_classified"] = pd.NA

    # Find and process the first matching column
    found_column = False
    for col in possible_columns:
        if col in df.columns:
            print(f"Gender data found in column: {col}")

            # Store raw data
            df["Gender_raw"] = df[col]

            # Calculate initial statistics
            count_nans = df["Gender_raw"].notna().sum()
            total_rows = len(df)
            coverage_percent = (count_nans / total_rows) * 100
            print(
                f"Number of variables in the original column: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
            )

            found_column = True
            break

    if not found_column:
        print("Gender data not found in any expected columns")
        return df

    # Only proceed with classification if we found data
    if found_column:
        # Clean and process the gender data
        df["Gender_classified"] = (
            df["Gender_raw"]
            .str.replace(
                r"[^a-zA-Z\s]", "", regex=True
            )  # Remove non-alphabetic characters
            .str.split()
            .str[0]  # Take first word
            .str.lower()
        )  # Convert to lowercase

        # Apply gender mapping
        df["Gender_classified"] = df["Gender_classified"].replace(
            {"man": "male", "woman": "female"}
        )

        # Final classification using safe check
        def classify_gender(x):
            if not isinstance(x, str):
                return x
            if any(term in x for term in gender_dict["female"]):
                return "female"
            if any(term in x for term in gender_dict["male"]):
                return "male"
            return x

        df["Gender_classified"] = df["Gender_classified"].apply(classify_gender)

        # Calculate final statistics
        count_nans = df["Gender_classified"].notna().sum()
        total_rows = len(df)
        coverage_percent = (count_nans / total_rows) * 100

        # Count specific gender classifications
        female_count = (df["Gender_classified"] == "female").sum()
        male_count = (df["Gender_classified"] == "male").sum()
        other_count = count_nans - female_count - male_count

        print(f"\nClassification results:")
        print(f"Female artists: {female_count}")
        print(f"Male artists: {male_count}")
        print(f"Other/Unclassified: {other_count}")
        print(
            f"Total classified entries: {count_nans} out of {total_rows} ({coverage_percent:.1f}%)"
        )

        # Show sample of results
        print("\nSample of classification results:")
        print(df[["Gender_raw", "Gender_classified"]].head())
        print("----------------------------------")

    return df
