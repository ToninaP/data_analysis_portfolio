import os
import pandas as pd


def load_data(folder_path, filter_data=False):
    # List all files in the given folder
    all_files = os.listdir(folder_path)

    # Filter out the CSV files
    csv_files = [file for file in all_files if file.endswith(".csv")]

    dataframes = []
    museum_names = []

    # Loop through each CSV file and read the data into a dataframe
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame

        # Apply filter if filter_data is True
        if filter_data:
            df = df[df["Date_creation_year"] >= 1860]

        dataframes.append(df)  # Add the dataframe to the list
        museum_names.append(os.path.splitext(csv_file)[0])

    return dataframes, museum_names
