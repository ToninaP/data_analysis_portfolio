import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff


def plot_medium_over_years(museum_data):
    data_transformed = []
    figures = []

    for df in museum_data:
        # Group by 'Medium_classified' and 'Year_acquisition' and count the occurrences
        df = (
            df.groupby(["Medium_classified", "Year_acquisition"])
            .size()
            .reset_index(name="Count")
        )

        # Filter out the first acquisition year and drop NaNs
        first_acquisition_year = df["Year_acquisition"].min()
        filtered_df = df[df["Year_acquisition"] > first_acquisition_year]
        filtered_df = filtered_df.dropna(subset=["Year_acquisition"])

        # Group the data by 'Medium_classified' and collect the 'Year_acquisition' values
        grouped = (
            filtered_df.groupby("Medium_classified")["Year_acquisition"]
            .apply(list)
            .tolist()
        )

        # Filter out groups with fewer than 2 acquisition years
        grouped = [group for group in grouped if len(group) > 1]

        if not grouped:
            continue  # Skip if no valid groups to plot

        # Get the corresponding labels for the groups
        group_labels = (
            filtered_df["Medium_classified"].unique().tolist()[: len(grouped)]
        )

        # Set custom colors for each group
        colors = [
            "#fd7f6f",
            "#7eb0d5",
            "#b2e061",
            "#bd7ebe",
            "#ffb55a",
            "#ffee65",
            "#beb9db",
            "#fdcce5",
            "#8bd3c7",
        ][: len(group_labels)]

        # Create the distplot with the grouped 'Year_acquisition' data
        fig = ff.create_distplot(
            grouped,
            group_labels,
            show_hist=False,
            colors=colors,
            show_rug=False,
            show_curve=True,
        )
        figures.append(fig)

    if figures:
        # Combine the individual figures into one
        fig2 = go.Figure()
        for fig in figures:
            fig2.add_traces(fig.data)

        return fig2
    else:
        print("No valid data to plot.")
        return None
