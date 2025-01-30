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
