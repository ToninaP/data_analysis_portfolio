import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class PlotConfig:
    """Configuration settings for the museum plot."""

    min_year: int = 1860
    figure_width: int = 900
    figure_height: int = 2000
    color_map: Dict[str, str] = None

    def __post_init__(self):
        if self.color_map is None:
            self.color_map = {
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


def plot_medium_over_years2(
    museum_data: List[pd.DataFrame],
    museum_names: List[str],
    config: Optional[PlotConfig] = None,
) -> go.Figure:
    """
    Create a distribution plot showing medium distribution over years for multiple museums.

    Args:
        museum_data: List of DataFrames containing museum data
        museum_names: List of museum names corresponding to the DataFrames
        config: PlotConfig object containing plotting configuration

    Returns:
        go.Figure: Plotly figure object containing the visualization

    Raises:
        ValueError: If museum_data and museum_names have different lengths
    """
    if len(museum_data) != len(museum_names):
        raise ValueError("Number of museums and names must match")

    if config is None:
        config = PlotConfig()

    figures = []

    for df in museum_data:
        fig = _create_museum_distribution(df, config)
        if fig is not None:
            figures.append(fig)

    if not figures:
        return None

    return _combine_figures(figures, museum_names, config)


def _create_museum_distribution(
    df: pd.DataFrame, config: PlotConfig
) -> Optional[go.Figure]:
    """Create distribution plot for a single museum."""
    # Filter data by minimum year
    df_filtered = df[df["Date_creation_year"] >= config.min_year].copy()

    # Calculate counts by medium and acquisition year
    grouped_df = (
        df_filtered.groupby(["Medium_classified", "Year_acquisition"])
        .size()
        .reset_index(name="Count")
    )

    # Remove first acquisition year and any NaN values
    first_year = grouped_df["Year_acquisition"].min()
    filtered_df = grouped_df[grouped_df["Year_acquisition"] > first_year].dropna(
        subset=["Year_acquisition"]
    )

    # Group by medium
    grouped = filtered_df.groupby("Medium_classified")["Year_acquisition"].agg(list)
    grouped = grouped[grouped.apply(len) > 1]

    if grouped.empty:
        return None

    group_labels = grouped.index.tolist()
    colors = [config.color_map.get(label, "#000000") for label in group_labels]

    return ff.create_distplot(
        grouped.tolist(),
        group_labels,
        show_hist=False,
        colors=colors,
        show_rug=False,
        show_curve=True,
    )


def _combine_figures(
    figures: List[go.Figure], museum_names: List[str], config: PlotConfig
) -> go.Figure:
    """Combine individual museum figures into a single subplot figure."""
    fig = make_subplots(
        rows=len(figures),
        cols=1,
        subplot_titles=museum_names[: len(figures)],
        shared_xaxes=True,
        shared_yaxes=True,
    )

    for idx, fig_data in enumerate(figures, 1):
        for trace in fig_data["data"]:
            if idx > 1:
                trace.update(showlegend=False)
            fig.add_trace(trace, row=idx, col=1)

    fig.update_xaxes(range=[config.min_year, None], title="Year of Acquisition")

    fig.update_layout(
        template="plotly_white",
        width=config.figure_width,
        height=config.figure_height,
    )

    return fig


# Example usage:
if __name__ == "__main__":
    # Create custom configuration if needed
    custom_config = PlotConfig(min_year=1900, figure_width=1000, figure_height=2500)

    # Create visualization
    fig = plot_medium_over_years2(museum_data, museum_names, custom_config)
    if fig is not None:
        fig.show()
