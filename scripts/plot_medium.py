import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_medium(museums_data, museum_names):

    # Data transformation: count how many works with medium
    data_transformed = []
    for df in museums_data:
        df = df.groupby(["Medium_classified"]).size().reset_index(name="Count")
        data_transformed.append(df)

    # Creating subplots
    fig = make_subplots(
        rows=1,
        cols=3,
        specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
    )

    # Iterate over data_transformed and museum_names using zip
    for i, (df, name) in enumerate(zip(data_transformed, museum_names)):
        fig.add_trace(
            go.Pie(labels=df["Medium_classified"], values=df["Count"], name=name),
            1,
            i + 1,  # Adding each plot in a separate column (1st row)
        )
    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=0.4, hoverinfo="label+percent+name")
    fig.update_layout(
        title_text="Artworks media percentage",
    )
    # Create annotations dynamically using the museum_names list
    annotations = []
    for i, name in enumerate(museum_names):
        # Calculate the x position relative to the subplot
        x_position = (i * 0.3) + 0.2  # Adjust this offset to position correctly
        annotations.append(
            dict(
                text=name,  # Annotation text from museum_names
                x=x_position,  # Adjust position horizontally
                y=0.5,  # Position above the pie chart
                font_size=20,
                showarrow=False,
                xanchor="center",
            )
        )

    # Add the annotations to the figure
    fig.update_layout(annotations=annotations)
    fig.update_layout(template="plotly_white")

    return fig
