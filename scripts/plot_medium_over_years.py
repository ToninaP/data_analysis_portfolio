import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff


def plot_medium_over_years(museum_data, museum_names, min_year=1860):
    # Define a color map for the labels
    label_color_map = {
        "architecture": "#fd7f6f",
        "graphics": "#7eb0d5",
        "installation": "#b2e061",
        "new media": "#bd7ebe",
        "object": "#ffb55a",
        "painting": "#ffee65",
        "photography": "#beb9db",
        "sculpture": "#fdcce5",
        "video art": "#8bd3c7",
    }

    # Create an empty list to hold the figures
    figures = []

    # Loop through all dataframes in museums_data list
    for idx, df in enumerate(museum_data):
        df_filtered = df[df["Date_creation_year"] >= min_year]

        # Grouping the data by 'Medium_classified' and 'Year_acquisition' to get counts
        grouped_df = (
            df_filtered.groupby(["Medium_classified", "Year_acquisition"])
            .size()
            .reset_index(name="Count")
        )

        # Filter out the first acquisition year
        first_acquisition_year = grouped_df["Year_acquisition"].min()
        filtered_df = grouped_df[
            grouped_df["Year_acquisition"] > first_acquisition_year
        ]
        filtered_df = filtered_df.dropna(subset=["Year_acquisition"])

        # Group the data by 'Medium_classified' and collect the 'Year_acquisition' values
        grouped = filtered_df.groupby("Medium_classified")["Year_acquisition"].apply(
            list
        )

        # Only keep groups with more than one element (avoid empty or insufficient data)
        grouped = grouped[grouped.apply(len) > 1]

        # If there are still groups left after filtering
        if not grouped.empty:
            # Get the group labels
            group_labels = grouped.index.tolist()

            # Assign colors to data points based on the labels
            colors = [
                label_color_map.get(label, "#000000") for label in group_labels
            ]  # Default to black if label not found

            # Create the distplot with the grouped 'Year_acquisition' data, showing a rug plot for single data points
            fig = ff.create_distplot(
                grouped.tolist(),
                group_labels,
                show_hist=False,
                colors=colors,
                show_rug=False,
                show_curve=True,
            )

            # Add the created figure to the list of figures
            figures.append(fig)
        else:
            pass

    # Create the figure with an appropriate number of rows
    num_figures = len(figures)
    num_rows = (
        num_figures  # Assuming one figure per row, modify if you need multiple columns
    )

    # Create a subplot grid with enough rows for all figures in 'figures'
    fig = make_subplots(
        rows=num_rows,
        cols=1,
        subplot_titles=museum_names,
        shared_xaxes=True,
        shared_yaxes=True,
    )

    # Loop through the list of figures
    for idx, fig_data in enumerate(figures):
        # Loop through all traces in the current figure (fig_data)
        for trace in fig_data["data"]:
            # If it's not the first figure, disable the legend
            if idx > 0:
                trace.update(showlegend=False)

            # Add the trace to the correct subplot (row=idx+1, col=1)
            fig.add_trace(trace, row=idx + 1, col=1)

    # Set the x-axis range explicitly to start from min_year (1860)
    fig.update_xaxes(
        range=[
            min_year,
            None,
        ],  # Set the x-axis to start from min_year and let the max value be auto-calculated
        title="Year of Acquisition",
    )

    # Customize layout, including template for clean visuals
    fig.update_layout(
        template="plotly_white",
        width=900,
        height=2000,
    )

    return fig
