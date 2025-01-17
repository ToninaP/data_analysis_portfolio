import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_medium_bar(museum_data, museum_names, min_year=1860):

    # Updated color palette with two additional colors
    colors = [
        "#636EFA",
        "#EF553B",
        "#00CC96",
        "#AB63FA",
        "#FFA15C",
        "#19D3F3",
        "#FF6692",
        "#B6E880",
        "#FF97FF",
        "#F4E1D2",
    ]

    # This will help us identify all unique media across museums
    medium_labels = set()
    medium_counts = {}  # Dictionary to store total counts across all museums

    data_transformed = []

    # Transform the data for each museum
    for df in museum_data:
        # Filter data based on the minimum year
        df_filtered = df[df["Date_creation_year"] >= min_year]

        # Group by "Medium_classified" and count the number of occurrences
        df_grouped = (
            df_filtered.groupby(["Medium_classified"]).size().reset_index(name="Count")
        )

        data_transformed.append(df_grouped)

        # Track all unique media types across all museums and accumulate the counts
        for medium, count in zip(df_grouped["Medium_classified"], df_grouped["Count"]):
            if medium in medium_counts:
                medium_counts[medium] += count
            else:
                medium_counts[medium] = count

            medium_labels.add(medium)

    # Sort mediums by total count across all museums in descending order
    medium_labels = sorted(medium_labels, key=lambda x: medium_counts[x], reverse=True)

    # Create the subplots
    fig = make_subplots(
        rows=1,
        cols=len(museum_data),
        shared_yaxes=True,  # Share y-axis so counts are comparable
        subplot_titles=museum_names,
    )

    # Add the bars for each museum (subplot)
    for i, (df_grouped, museum_name) in enumerate(zip(data_transformed, museum_names)):
        # Ensure all mediums are represented, even if they don't appear in a particular museum
        df_grouped = df_grouped.set_index("Medium_classified").reindex(
            medium_labels, fill_value=0
        )

        # Calculate the percentage of media for each medium
        df_grouped["percent of media"] = (
            100 * df_grouped["Count"] / df_grouped["Count"].sum()
        )

        # Sort by percentage in descending order
        df_grouped = df_grouped.sort_values(by="percent of media", ascending=False)

        # Create a trace for each medium (same color for the same medium across all plots)
        for j, medium in enumerate(df_grouped.index):
            fig.add_trace(
                go.Bar(
                    x=[medium],  # Single bar per medium
                    y=[
                        df_grouped.loc[medium, "percent of media"]
                    ],  # Use percentage instead of count
                    name=medium,
                    legendgroup=medium,  # Ensure the medium has the same color across all plots
                    marker=dict(color=colors[j % len(colors)]),  # Use updated colors
                    hovertext=f"{df_grouped.loc[medium, 'percent of media']:.2f}%",  # Hover info with percentage
                    hoverinfo="text",
                    showlegend=(i == 0),  # Only show legend in the first plot
                ),
                row=1,
                col=i + 1,  # Place bars in the appropriate subplot (column)
            )

    # Update layout
    fig.update_layout(
        title="Medium Distribution Across Museums",
        xaxis=dict(
            title="Medium",
            tickangle=45,
            tickmode="array",
            tickvals=medium_labels,  # Ensure x-axis has all medium labels
        ),
        yaxis=dict(
            title="Percentage (%)",
        ),
        height=500,
        width=2500,  # Adjust height of the plot
        showlegend=True,
        template="plotly_white",
    )

    fig.show()
