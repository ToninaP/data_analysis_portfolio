import os
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
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
        return country.alpha_3 if country else None
    except:
        return None


def plot_origin_countries2(museum_data, museum_names, min_year=1860):

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

        # Remove rows with invalid codes
        df = df[df["CODE"].notna()]

    # Create a single plot (choropleth) with one plot for all museums
    fig = go.Figure()

    # Create choropleth maps and markers for each museum
    choropleths = []
    markers = []

    for i, df in enumerate(valid_museum_data):
        choropleth = go.Choropleth(
            locations=df["CODE"],
            z=df["Count"],
            text=df["Country_normalized"],
            colorscale="YlGnBu",
            autocolorscale=False,
            reversescale=True,
            marker_line_color="darkgray",
            marker_line_width=0.5,
            colorbar_title="Number of Artworks in Collection",
            visible=False,  # Initially set all maps to be invisible
            name=valid_museum_names[i],  # Use museum name for dropdown
        )
        choropleths.append(choropleth)

        # Add red spot at museum location (if lat/lon are provided)
        marker = go.Scattergeo(
            lon=[longitudes[i]],
            lat=[latitudes[i]],
            mode="markers",
            marker=dict(
                color="red",
                size=10,
                symbol="circle",
            ),
            name=f"Location of {valid_museum_names[i]}",  # Label marker
            visible=False,  # Initially set all markers to be invisible
        )
        markers.append(marker)

    # Add choropleths and markers to the figure
    for choropleth, marker in zip(choropleths, markers):
        fig.add_trace(choropleth)
        fig.add_trace(marker)

    # Update layout to include the dropdown menu
    fig.update_layout(
        geo=dict(
            showframe=True,
            showcoastlines=False,
            projection_type="equirectangular",
        ),
        height=600,  # Adjust the height to fit the plot
        showlegend=False,
        title_text="Artworks in Collections by Origin Country",
        updatemenus=[
            {
                "buttons": [
                    {
                        "args": [
                            {
                                "visible": [
                                    True if idx == i else False
                                    for idx in range(len(valid_museum_data))
                                ]
                                + [
                                    True if idx == i else False
                                    for idx in range(len(valid_museum_data))
                                ]
                            },
                            {
                                "title": f"Artworks in Collections by Origin Country - {museum}"
                            },
                        ],
                        "label": museum,
                        "method": "update",
                    }
                    for i, museum in enumerate(valid_museum_names)
                ],
                "direction": "down",
                "showactive": True,
                "active": 0,  # Default to the first museum in the list
                "x": 0.17,
                "xanchor": "left",
                "y": 1.1,
                "yanchor": "top",
            }
        ],
    )

    # Make the first plot and marker visible by default
    fig.data[0].visible = True  # First choropleth
    fig.data[1].visible = True  # First marker

    return fig


"""#code that is an example for waht I want to do here
import plotly.graph_objects as px 
import numpy 


# creating random data through randomint 
# function of numpy.random 
np.random.seed(42) 

random_x = np.random.randint(1, 101, 100) 
random_y = np.random.randint(1, 101, 100) 

x = ['A', 'B', 'C', 'D'] 

plot = px.Figure(data=[go.Bar( 
	name='Data 1', 
	x=x, 
	y=[100, 200, 500, 673] 
), 
	go.Bar( 
	name='Data 2', 
	x=x, 
	y=[56, 123, 982, 213] 
) 
]) 


# Add dropdown 
plot.update_layout( 
	updatemenus=[ 
		dict( 
			active=0, 
			buttons=list([ 
				dict(label="Both", 
					method="update", 
					args=[{"visible": [True, True]}, 
						{"title": "Both"}]), 
				dict(label="Data 1", 
					method="update", 
					args=[{"visible": [True, False]}, 
						{"title": "Data 1", 
							}]), 
				dict(label="Data 2", 
					method="update", 
					args=[{"visible": [False, True]}, 
						{"title": "Data 2", 
							}]), 
			]), 
		) 
	]) 

plot.show() 
"""
