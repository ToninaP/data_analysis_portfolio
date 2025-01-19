import os
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from shapely.geometry import Point
import pycountry


def normalize_country_name(country_name):
    try:
        country = pycountry.countries.search_fuzzy(country_name)[0]
        return country.name
    except LookupError:
        return None


# Add country code column
def add_country_code(country_name):
    try:
        country = pycountry.countries.get(name=country_name)
        return country.alpha_3
    except:
        return None


def plot_origin_countries(museum_data, museum_names, min_year=1860):

    valid_museum_data = []
    valid_museum_names = []

    # Process each museum dataset and check if it contains valid data
    for i, df in enumerate(museum_data):
        # Filter the data by the minimum year
        df = df[df["Year_acquisition"] >= min_year]

        # Remove rows where 'Country_calculated' is NaN (empty)
        df = df.dropna(subset=["Country_calculated"])

        grouped = df.groupby(["Country_calculated"]).size().reset_index(name="Count")

        # If there is valid data, add it to the list for plotting
        if not grouped.empty:
            valid_museum_data.append(grouped)
            valid_museum_names.append(museum_names[i])

    museum_locations = [
        "Copenhagen",
        "New York",
        "New York",
        "Madrid",
        "Paris",
        "Brisbane",
        "Washington, DC",
    ]
    # Corresponding latitudes and longitudes
    latitudes = [55.6761, 40.7128, 40.7128, 40.4168, 48.8566, -27.4698, 38.9072]
    longitudes = [12.5683, -74.0060, -74.0060, -3.7038, 2.3522, 153.0251, -77.0369]

    # Normalize country names and add codes
    for df in valid_museum_data:
        df["Country_normalized"] = df["Country_calculated"].apply(
            normalize_country_name
        )
        df["CODE"] = df["Country_normalized"].apply(add_country_code)

    # Create a subplot grid with geo type
    fig = make_subplots(
        rows=len(valid_museum_data),
        cols=1,
        subplot_titles=valid_museum_names,
        vertical_spacing=0.05,
        shared_xaxes=True,
        shared_yaxes=True,
        specs=[
            [{"type": "choropleth"}] for _ in range(len(valid_museum_data))
        ],  # Set geo type for each subplot
    )

    # Plot each museum's data as a separate subplot
    for i, df in enumerate(valid_museum_data):
        # Create the choropleth map
        choropleth = go.Choropleth(
            locations=df["CODE"],
            z=df["Count"],
            text=df["Country_normalized"],
            colorscale="YlGnBu",
            autocolorscale=False,
            reversescale=True,
            marker_line_color="darkgray",
            marker_line_width=0.5,
            colorbar_title="number of artworks in collection",
        )

        # Add the choropleth map to the subplot
        fig.add_trace(choropleth, row=i + 1, col=1)

        # Add red spot at museum location (if lat/lon are provided)
        fig.add_trace(
            go.Scattergeo(
                lon=[longitudes[i]],
                lat=[latitudes[i]],
                mode="markers",
                marker=dict(
                    color="red",
                    size=10,
                    symbol="circle",
                ),
                name=valid_museum_names[i],
            ),
            row=i + 1,
            col=1,
        )

    # Update layout
    fig.update_layout(
        geo=dict(
            showframe=True,
            showcoastlines=False,
            projection_type="equirectangular",
        ),
        height=300
        * len(valid_museum_data),  # Adjust height based on number of subplots
        showlegend=False,
        title_text="Artworks in Collections by Origin Country",
    )

    return fig
