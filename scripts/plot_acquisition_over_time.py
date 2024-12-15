import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_acquisition_over_time(museum_data, museum_names, min_year=1860):
    # Define a consistent color palette for the specified acquisition categories
    category_colors = {
        "museum accession": "rgb(54, 162, 235)",  # Blue
        "jointly owned": "rgb(255, 159, 64)",  # Orange
        "bequest": "rgb(75, 192, 192)",  # Teal
        "gift": "rgb(153, 102, 255)",  # Purple
        "tax": "rgb(255, 205, 86)",  # Yellow
        "loan": "rgb(255, 99, 132)",  # Red
        "exchange": "rgb(255, 159, 64)",  # Orange
        "commissioned": "rgb(75, 192, 192)",  # Teal
        "assisted purchase": "rgb(255, 99, 132)",  # Red
        # Add other colors as needed
    }

    # Create a subplot figure with 1 row and 11 columns for 11 museums
    fig = make_subplots(
        rows=11,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        subplot_titles=museum_names,
    )

    # Loop through each museum's data and add traces to its corresponding subplot
    for i, df in enumerate(museum_data):
        # Filter the data by the minimum year
        df = df[df["Year_acquisition"] >= min_year]

        # Grouping the data by 'Acquistion_classified' and 'Year_acquisition' to get counts
        grouped_df = (
            df.groupby(["Acquistion_classified", "Year_acquisition"])
            .size()
            .reset_index(name="Count")
        )

        # Extract the categories of acquisition for plotting
        museum_acquisition_categories = grouped_df["Acquistion_classified"].unique()

        # Add a trace for each acquisition category in the subplot corresponding to the current museum
        for category in museum_acquisition_categories:
            category_df = grouped_df[grouped_df["Acquistion_classified"] == category]
            x = category_df["Year_acquisition"]
            y = category_df["Count"]

            # Ensure that categories without a color in the dictionary default to 'gray'
            color = category_colors.get(category, "gray")

            # Add the trace to the subplot
            fig.add_trace(
                go.Scatter(
                    x=x,
                    y=y,
                    mode="lines",
                    name=category,
                    line=dict(color=color, width=2),
                    stackgroup="one",
                    groupnorm="percent",  # Normalizes the sum of each stackgroup
                    legendgroup=category,  # Group all traces of the same category together in the legend
                ),
                row=i + 1,
                col=1,  # Place this trace in the i-th subplot (1-based index)
            )

    # Update layout for the entire figure
    fig.update_layout(
        title="Acquisition Trends Over Time",
        xaxis_title="Year",
        yaxis_title="Percentage of Acquisitions",
        showlegend=True,
        template="plotly_white",
        height=1000,  # Adjust this as needed for your screen size
    )

    # Update x-axis and y-axis titles for all subplots
    fig.update_xaxes(title_text="Year", row=11, col=1)  # Only on the last subplot
    fig.update_yaxes(
        title_text="Percentage of Acquisitions", row=11, col=1
    )  # Only on the last subplot

    return fig
