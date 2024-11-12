import os
import pandas as pd


def load_data(folder_path):
    # List all files in the given folder
    all_files = os.listdir(folder_path)

    # Filter out the CSV files
    csv_files = [file for file in all_files if file.endswith(".csv")]

    # List to hold the dataframes
    dataframes = []

    # Loop through each CSV file and read the data into a dataframe
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
        dataframes.append(df)  # Add the dataframe to the list

    return dataframes
