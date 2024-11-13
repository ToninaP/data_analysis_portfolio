import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px


def plot_medium_over_years(museum_data, museum_names):

    df = museum_data[0]

    grouped_df = (
        df.groupby(["Medium_classified", "Year_acquisition"])
        .size()
        .reset_index(name="Count")
    )

    first_acquisition_year = grouped_df["Year_acquisition"].min()
    filtered_df = grouped_df[grouped_df["Year_acquisition"] > first_acquisition_year]
    filtered_df = filtered_df.dropna(subset=["Year_acquisition"])

    fig = px.area(
        filtered_df, x="Year_acquisition", y="Count", color="Medium_classified"
    )
    return fig
