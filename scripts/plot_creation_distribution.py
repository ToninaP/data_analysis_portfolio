import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_creation_distribution(museum_data, museum_names, min_year=1860, max_year=None):
    """
    This function takes in a list of datasets (museum_data) and creates an interactive plot
    showing the distribution of the 'Date_creation_year' across all datasets.

    Parameters:
    museum_data (list of DataFrames): A list containing pandas DataFrames with a 'Date_creation_year' column.
    museum_names (list of str): A list of names for each museum dataset, used as titles for subplots.
    min_year (int): Minimum year to filter the 'Date_creation_year' data.
    max_year (int, optional): Maximum year to filter the 'Date_creation_year' data.
    """

    museum_data_grouped = []
    current_year = pd.to_datetime("today").year

    # If max_year is not provided, use the current year
    if max_year is None:
        max_year = current_year

    for df in museum_data:
        # Check if 'Date_creation_year' exists in the DataFrame
        if "Date_creation_year" not in df.columns:
            print("Error: 'Date_creation_year' column is missing from the datasets.")
            return

        # Filter the data by the minimum and maximum year
        df = df[
            (df["Date_creation_year"] >= min_year)
            & (df["Date_creation_year"] <= max_year)
        ]

        # Remove any unrealistic or outlier years (e.g., greater than 2024)
        df = df[df["Date_creation_year"] <= current_year]

        # Group by 'Date_creation_year' and count occurrences
        df_grouped = (
            df.groupby(by=["Date_creation_year"]).size().reset_index(name="Count")
        )
        museum_data_grouped.append(df_grouped)

    # Create a subplot figure with rows corresponding to valid museums
    fig = make_subplots(
        rows=len(museum_data_grouped),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        subplot_titles=museum_names,
    )

    # Add traces to each subplot
    for i, df in enumerate(museum_data_grouped):
        fig.add_trace(
            go.Bar(
                x=df["Date_creation_year"],
                y=df["Count"],
                marker_color="rgb(55, 83, 109)",
            ),
            row=i + 1,  # i+1 because rows in Plotly are 1-based
            col=1,
        )

    # Update layout for better presentation
    fig.update_layout(
        title="Distribution of Artworks by Date of Creation",
        template="plotly_white",
        height=1500,
        showlegend=False,
    )

    return fig
