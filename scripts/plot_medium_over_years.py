import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff


def plot_medium_over_years(museum_data, museum_names, min_year=1860):
    # colors for labels (fixed global color map)
    label_color_map = {
        "architecture": "rgb(253, 127, 111)",
        "graphics": "rgb(126, 176, 213)",
        "installation": "rgb(178, 224, 97)",
        "new media": "rgb(189, 126, 190)",
        "object": "rgb(255, 181, 90)",
        "painting": "rgb(255, 238, 101)",
        "photography": "rgb(190, 185, 219)",
        "sculpture": "rgb(253, 204, 229)",
        "video art": "rgb(139, 211, 199)",
    }

    # Initialize lists for valid data
    valid_museum_data = []
    valid_museum_names = []

    # Process and validate museum data
    for i, df in enumerate(museum_data):
        df_filtered = df[df["Year_acquisition"] >= min_year].copy()
        df_filtered = df_filtered.dropna(subset=["Medium_classified"])

        if not df_filtered.empty:
            valid_museum_data.append(df_filtered)
            valid_museum_names.append(museum_names[i])

    # Get all unique categories across all museums
    all_categories = set()
    for df in valid_museum_data:
        all_categories.update(df["Medium_classified"].unique())
    all_categories = sorted(list(all_categories))

    # Create figure
    fig = make_subplots(
        rows=len(valid_museum_data),
        cols=1,
        shared_xaxes=True,
        subplot_titles=valid_museum_names,
    )

    # Create a fixed color mapping for all categories
    color_mapping = {}
    for category in all_categories:
        if category in label_color_map:
            color_mapping[category] = label_color_map[category]
        else:
            # Assign a consistent gray color for unknown categories
            color_mapping[category] = "rgb(128, 128, 128)"

    # Plot data for each museum
    for museum_idx, df in enumerate(valid_museum_data):
        # Prepare data for this museum
        yearly_data = {}

        # Initialize data structure for all years and categories
        years = df["Year_acquisition"].unique()
        for year in years:
            yearly_data[year] = {cat: 0 for cat in all_categories}

        # Calculate percentages for each category and year
        for year in years:
            year_data = df[df["Year_acquisition"] == year]
            total_items = len(year_data)

            if total_items > 0:
                category_counts = year_data["Medium_classified"].value_counts()
                for category, count in category_counts.items():
                    yearly_data[year][category] = (count / total_items) * 100

        # Plot each category
        for category in all_categories:
            x_values = sorted(years)
            y_values = [yearly_data[year][category] for year in x_values]

            fig.add_trace(
                go.Scatter(
                    x=x_values,
                    y=y_values,
                    name=category,
                    mode="none",
                    fill="tonexty" if category != all_categories[0] else "tozeroy",
                    fillcolor=color_mapping[category],
                    line=dict(color=color_mapping[category], width=0),
                    legendgroup=category,
                    showlegend=(museum_idx == 0),
                    stackgroup="one",
                    hoveron="points+fills",
                ),
                row=museum_idx + 1,
                col=1,
            )

    # Update layout
    fig.update_layout(
        template="plotly_white",
        width=900,
        height=1800,
        title="Percentage of Acquisitions by Medium Over Years",
        showlegend=True,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.0),
        hovermode="x unified",
    )

    # Update y-axes
    for i in range(len(valid_museum_data)):
        fig.update_yaxes(title_text="Percentage (%)", range=[0, 100], row=i + 1, col=1)

    return fig
