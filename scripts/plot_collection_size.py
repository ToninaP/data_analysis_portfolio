import pandas as pd
import plotly.graph_objects as go


def plot_collection_size(museums_data, museum_names):

    if len(museums_data) != len(museum_names):
        raise ValueError(
            "The number of dataset sizes must match the number of dataset names."
        )
    collection_sizes = [len(df) for df in museums_data]

    collection_sizes = [
        max(size, 1) for size in collection_sizes
    ]  # Replacing zeros with 1
    # Create a bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                x=museum_names,
                y=collection_sizes,
                marker_color="skyblue",
                text=collection_sizes,
                textposition="auto",
            )
        ]
    )

    # Add labels and title
    fig.update_layout(
        title="Collection Sizes",
        xaxis_title="Museum",
        yaxis_title="N of artworks in collection",
    )
    fig.update_yaxes(type="log", range=[0, 5])

    return fig
