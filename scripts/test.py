import os
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
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

    # Create figure
    fig = go.Figure()

    # Add the choropleth maps and locations for each dataset
    for i, df in enumerate(valid_museum_data):
        # Add the choropleth map
        fig.add_trace(
            go.Choropleth(
                locations=df["CODE"],
                z=df["Count"],
                text=df["Country_normalized"],
                colorscale="YlGnBu",
                autocolorscale=False,
                reversescale=True,
                marker_line_color="darkgray",
                marker_line_width=0.5,
                colorbar_title="number of artworks in collection",
                name=valid_museum_names[i],
                visible=False,  # Initially set to invisible
            )
        )

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
                name=f"Location of {valid_museum_names[i]}",
                visible=False,  # Initially set to invisible
            )
        )

    # Create dropdown menu to toggle datasets
    fig.update_layout(
        geo=dict(
            showframe=True, showcoastlines=False, projection_type="equirectangular"
        ),
        updatemenus=[
            {
                "buttons": [
                    {
                        "args": [
                            [museum_name],
                            {
                                "visible": [
                                    True if name == museum_name else False
                                    for name in valid_museum_names
                                ]
                            },
                        ],
                        "label": museum_name,
                        "method": "restyle",
                    }
                    for museum_name in valid_museum_names
                ],
                "direction": "down",
                "pad": {"r": 10, "t": 87},
                "showactive": True,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "left",
                "y": 1.15,
                "yanchor": "top",
            }
        ],
    )

    # Show the first dataset by default
    fig.data[0].visible = True
    fig.data[1].visible = True  # Ensure the first museum's location is visible as well

    return fig
