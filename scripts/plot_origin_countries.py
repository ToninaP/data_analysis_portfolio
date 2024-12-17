import os
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from shapely.geometry import Point


def plot_origin_countries(museum_data, museum_names, min_year=1860):
    valid_museum_data = []
    valid_museum_names = []

    # Process each museum dataset and check if it contains valid data
    for i, df in enumerate(museum_data):
        # Filter the data by the minimum year
        df = df[df["Year_acquisition"] >= min_year]

        # Remove rows where 'Country_calculated' is NaN (empty)
        df = df.dropna(subset=["Country_calculated"])

        # If the dataframe is empty after filtering, skip this museum
        if df.empty:
            continue

        # If there is valid data, add it to the list for plotting
        valid_museum_data.append(df)
        valid_museum_names.append(museum_names[i])

    # Path to the downloaded shapefile
    shapefile_path = "/Users/antoninalightfoot/Library/Mobile Documents/com~apple~CloudDocs/Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"

    # Load the world map shapefile
    world = gpd.read_file(shapefile_path)

    # Assuming the correct column is 'NAME' (it could also be 'NAME_LONG' or 'country')
    country_column = "NAME"

    # Create a subplot grid (one for each museum)
    num_subplots = len(valid_museum_names)
    rows = (num_subplots + 1) // 2  # 2 columns per row, adjust rows accordingly
    cols = 2

    # Create the subplot figure with geo maps
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=valid_museum_names,
        specs=[[{"type": "choropleth"}] * cols]
        * rows,  # Define subplots to be choropleth maps
        vertical_spacing=0.05,  # Reduce vertical space between rows
        horizontal_spacing=0.05,
    )

    # Custom colorscale that colors 0 mentions as gray, and the rest using the "Viridis" scale
    colorscale = [
        [0, "gray"],  # Color for 0 mentions
        [0.01, "gray"],  # Ensure 0 is gray
        [0.01, "purple"],  # Starting point of "Viridis"
        [1, "yellow"],  # Ending point of "Viridis"
    ]

    # Iterate through each dataset in valid_museum_data and plot the locations
    for i, (data, name) in enumerate(zip(valid_museum_data, valid_museum_names)):
        # Combine all museum data and count the mentions of each country
        country_mentions = data["Country_calculated"].value_counts().reset_index()
        country_mentions.columns = ["Country", "Mentions"]

        # Debugging: Check the country_mentions DataFrame
        # print(f"Country mentions for {name}:")
        # print(country_mentions.head())

        # Merge the country mentions with the shapefile data
        world_merged = world.merge(
            country_mentions, left_on=country_column, right_on="Country", how="left"
        )

        # Debugging: Check the result of the merge
        # print(f"Merged world data for {name}:")
        # print(world_merged[["Country", "Mentions"]].head())

        # Fill NaN values in 'Mentions' with 0 (countries that have no mentions)
        world_merged["Mentions"] = world_merged["Mentions"].fillna(0)

        # Debugging: Check if 'Mentions' column exists after fillna
        # print(f"Final merged data for {name} (with filled NaNs):")
        # print(world_merged[["Country", "Mentions"]].head())

        # Create a choropleth map for the current museum dataset
        choropleth_trace = go.Choropleth(
            locations=world_merged[country_column],
            locationmode="country names",
            z=world_merged["Mentions"],
            hoverinfo="location+z",
            colorscale=colorscale,  # Custom colorscale
            colorbar=dict(title="Number of Mentions"),
        )

        # Calculate subplot position (row and col for subplot)
        row = (i // cols) + 1
        col = (i % cols) + 1

        # Add the choropleth trace to the subplot
        fig.add_trace(choropleth_trace, row=row, col=col)

    # Define the layout for the plot
    fig.update_layout(
        title="Museums' Acquisition Origins by Country",
        geo=dict(
            projection_type="natural earth",
            showland=True,
            landcolor="lightgray",
            countrycolor="white",
            coastlinecolor="black",
            lakecolor="white",
        ),
        height=1500,
        width=1500,
        template="plotly_dark",
    )

    return fig
