import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_acquisition_over_time(museum_data, museum_names, min_year=1860):
    # Define a consistent color palette for the specified acquisition categories
    category_colors = {
        "museum accession": "rgb(255, 198, 93)",  # Golden yellow
        "jointly owned": "rgb(126, 141, 232)",  # Periwinkle blue
        "bequest": "rgb(130, 202, 157)",  # Sage green
        "gift": "rgb(147, 101, 184)",  # Muted purple
        "tax": "rgb(92, 124, 250)",  # Royal blue
        "loan": "rgb(255, 107, 129)",  # Coral pink
        "exchange": "rgb(83, 186, 157)",  # Turquoise
        "commissioned": "rgb(255, 170, 195)",  # Soft pink
        "assisted purchase": "rgb(255, 151, 76)",  # Warm orange
    }

    # Initialize a list to keep track of valid museums (those with data to plot)
    valid_museum_data = []
    valid_museum_names = []

    # Process each museum dataset and check if it contains valid data
    for i, df in enumerate(museum_data):
        df_filtered = df[df["Year_acquisition"] >= min_year].copy()
        df_filtered = df_filtered.dropna(subset=["Acquistion_classified"])

        if not df_filtered.empty:
            valid_museum_data.append(df_filtered)
            valid_museum_names.append(museum_names[i])

    # Get all unique categories across all museums
    all_categories = set()
    for df in valid_museum_data:
        all_categories.update(df["Acquistion_classified"].unique())
    all_categories = sorted(list(all_categories))

    # Create a subplot figure with rows corresponding to valid museums
    fig = make_subplots(
        rows=len(valid_museum_data),
        cols=1,
        shared_xaxes=True,
        subplot_titles=valid_museum_names,
    )

    # Create a fixed color mapping for all categories
    color_mapping = {}
    for category in all_categories:
        if category in category_colors:
            color_mapping[category] = category_colors[category]
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
                category_counts = year_data["Acquistion_classified"].value_counts()
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

    # Update layout for the entire figure
    fig.update_layout(
        title="Acquisition Trends Over Time",
        xaxis_title="Year",
        yaxis_title="Percentage of Acquisitions",
        showlegend=True,
        template="plotly_white",
        height=1000,
        hovermode="x unified",
    )

    # Update x-axis and y-axis titles for all subplots
    fig.update_xaxes(
        title_text="Year", row=len(valid_museum_data), col=1
    )  # Only on the last subplot
    fig.update_yaxes(
        title_text="Percentage of Acquisitions", row=len(valid_museum_data), col=1
    )  # Only on the last subplot

    return fig
