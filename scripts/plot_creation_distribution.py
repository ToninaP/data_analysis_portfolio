import pandas as pd
import plotly.express as px


def plot_creation_distribution(museum_data):
    """
    This function takes in a list of datasets (museum_data) and creates an interactive plot
    showing the distribution of the 'Date_creation_year' across all datasets.

    Parameters:
    museum_data (list of DataFrames): A list containing pandas DataFrames with a 'Date_creation_year' column.
    """
    museum_data_grouped = []
    for df in museum_data:

        # Check if 'Date_creation_year' exists in the DataFrame
        if "Date_creation_year" not in df.columns:
            print("Error: 'Date_creation_year' column is missing from the datasets.")
            return

        # Group by 'Date_creation_year' and count occurrences
        df_grouped = df["Date_creation_year"].value_counts().reset_index()
        df_grouped.columns = ["Date_creation_year", "Count"]
        museum_data_grouped.append(df_grouped)

    # Create an interactive bar chart using Plotly
    fig = px.bar(
        museum_data_grouped[0],
        x="Date_creation_year",
        y="Count",
        title="Distribution of Data Points by Date of Creation",
        labels={
            "Date_creation_year": "Year of Creation",
            "Count": "Number of Artifacts",
        },
    )

    return fig
