import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math  # Import math for ceiling function


def plot_medium_pie(museums_data, museum_names, min_year=1860):
    """
    Plot pie charts for different museums based on the medium of artworks,
    filtering for artworks created after a specific year.

    Parameters:
    museums_data (list of DataFrame): List of DataFrames containing museum data.
    museum_names (list of str): List of museum names corresponding to the data.
    min_year (int): The minimum year for filtering artworks (default is 1860).

    Returns:
    fig: A Plotly figure object.
    """

    # Data transformation: count how many works with medium, filtered by the minimum year
    data_transformed = []
    for df in museums_data:
        # Filter data based on the minimum year
        df_filtered = df[df["Date_creation_year"] >= min_year]

        # Group by "Medium_classified" and count the number of occurrences
        df_grouped = (
            df_filtered.groupby(["Medium_classified"]).size().reset_index(name="Count")
        )

        data_transformed.append(df_grouped)

    number = len(museum_names)

    # Determine the number of rows and columns for the subplot layout
    rows = 3
    cols = math.ceil(number / rows)  # Ensure integer number of columns

    # Creating subplots
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=museum_names,
        specs=[
            [{"type": "domain"}] * cols for _ in range(rows)
        ],  # Automatically create a domain-type subplot grid
    )

    # Iterate over data_transformed and museum_names using zip
    for i, (df, name) in enumerate(zip(data_transformed, museum_names)):
        row = i // cols + 1  # Determine the row index
        col = i % cols + 1  # Determine the column index

        fig.add_trace(
            go.Pie(labels=df["Medium_classified"], values=df["Count"], name=name),
            row=row,
            col=col,  # Adding each plot in the appropriate subplot grid
        )

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=0.4, hoverinfo="label+percent+name")
    fig.update_layout(
        title_text="Artworks Media Percentage (Filtered by Date Creation >= 1860)",
        width=1200,
        height=900,
    )

    fig.update_layout(template="plotly_white")

    return fig
