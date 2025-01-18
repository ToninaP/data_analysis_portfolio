import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_gender_pyramid_acquisition(museum_data, museum_names, min_year=1860):
    # prepare data
    # Initialize a list to keep track of valid museums (those with data to plot)
    valid_museum_data = []
    valid_museum_names = []

    # Process each museum dataset and check if it contains valid data
    for i, df in enumerate(museum_data):
        df_filtered = df[df["Year_acquisition"] >= min_year].copy()
        df_filtered = df_filtered.dropna(subset=["Gender_classified"])

        if not df_filtered.empty:
            valid_museum_data.append(df_filtered)
            valid_museum_names.append(museum_names[i])
    # calculate artist age at artwork creation moment
    # calculate artist age at artwork acquisition moment
    for df in valid_museum_data:
        df["Artist_age_creation"] = df["Date_creation_year"] - df["Artist_birth_year"]
        df["Artist_age_acqusition"] = df["Year_acquisition"] - df["Artist_birth_year"]

    # group by and store data in lists

    # Define the age bins and labels
    bins = [
        0,
        4,
        9,
        14,
        19,
        24,
        29,
        34,
        39,
        44,
        49,
        54,
        59,
        64,
        69,
        74,
        79,
        89,
        99,
        np.inf,
    ]
    labels = [
        "0-4",
        "5-9",
        "10-14",
        "15-19",
        "20-24",
        "25-29",
        "30-34",
        "35-39",
        "40-44",
        "45-49",
        "50-54",
        "55-59",
        "60-64",
        "65-69",
        "70-74",
        "75-79",
        "80-90",
        "90-100",
        "100+",
    ]

    data_to_plot = []
    for df in valid_museum_data:

        # Create a new column 'Age_Group' to categorize each artist into the age group
        df["Age_Group"] = pd.cut(
            df["Artist_age_acqusition"], bins=bins, labels=labels, right=True
        )

        # Group by 'Age_Group' and 'Gender_classified', then count the occurrences
        grouped = (
            df.groupby(["Age_Group", "Gender_classified"], observed=False)
            .size()
            .unstack(fill_value=0)
        )

        # For the final output, create the structure as requested
        final_data = {
            "Age": labels,
            "Male": grouped.get("male", [0] * len(labels)),
            "Female": grouped.get("female", [0] * len(labels)),
        }

        # Create the final DataFrame
        final_df = pd.DataFrame(final_data)
        # Make all "Male" values negative
        final_df["Male"] = final_df["Male"] * -1
        data_to_plot.append(final_df)

    # plot data
    fig = make_subplots(
        rows=len(data_to_plot),
        cols=1,
        subplot_titles=valid_museum_names,
    )

    # Add traces to each subplot
    for i, df in enumerate(data_to_plot):
        fig.add_trace(
            go.Bar(
                y=df["Age"],
                x=df["Male"],
                name="Male",
                orientation="h",
                marker=dict(color="lightblue"),
            ),
            row=i + 1,  # Specify row number for each dataset
            col=1,
        )
        fig.add_trace(
            go.Bar(
                y=df["Age"],
                x=df["Female"],
                name="Female",
                orientation="h",
                marker=dict(color="pink"),
            ),
            row=i + 1,  # Specify row number for each dataset
            col=1,
        )

    # Update layout for better presentation
    fig.update_layout(
        title="Gender pyramid in collections: Artists at the artwork acquisition age",
        template="plotly_white",
        showlegend=True,
        barmode="relative",
        bargap=0.0,
        height=1500,
    )

    return fig
