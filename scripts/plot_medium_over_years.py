import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot


pd.options.display.max_columns = None


def plot_medium_over_years(museum_data):
    # we need to work with arrays of dataframes
    museumNamesAr = ["met", "reina sofia", "tate"]

    fig = make_subplots(rows=3, cols=1)

    fig.add_trace(
        go.Scatter(
            x=museum_data[0]["Year_acquisition"], y=museum_data[0]["Medium_classified"]
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=museum_data[1]["Year_acquisition"], y=museum_data[1]["Medium_classified"]
        ),
        row=2,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=museum_data[2]["Year_acquisition"], y=museum_data[2]["Medium_classified"]
        ),
        row=2,
        col=1,
    )

    return fig
