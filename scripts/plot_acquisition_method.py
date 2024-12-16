import pandas as pd
import plotly.graph_objects as go


def plot_acquisition_method(museum_data, museum_names, min_year=1860):
    data_transformed = []

    for df in museum_data:
        # Filter data based on the minimum year
        df_filtered = df[df["Date_creation_year"] >= min_year]

        # Group by "Acquistion_classified" and count the number of occurrences
        df_grouped = (
            df_filtered.groupby(["Acquistion_classified"])
            .size()
            .reset_index(name="Count")
        )

        # If the dataset is empty, ensure it is included with zero counts
        if df_grouped.empty:
            # Add a row with zero counts for each acquisition type
            acquisition_types = df["Acquistion_classified"].unique()
            df_grouped = pd.DataFrame(
                {
                    "Acquistion_classified": acquisition_types,
                    "Count": [0] * len(acquisition_types),
                }
            )

        data_transformed.append(df_grouped)

    # Add percentage column to each dataset
    for df in data_transformed:
        df["percent of acquisition type"] = 100 * df["Count"] / df["Count"].sum()

    # Create an empty list to hold the dataframes with the new column
    data_with_names = []

    # Iterate over the dataframes and add the corresponding dataset name
    for i, df in enumerate(data_transformed):
        # Add a new column 'dataset_name' with the dataset name
        df["dataset_name"] = (
            museum_names[i] if i < len(museum_names) else f"Dataset {i+1}"
        )
        data_with_names.append(df)

    # Concatenate all dataframes into one
    final_dataframe = pd.concat(data_with_names, ignore_index=True)

    # Prepare for stacked bar chart
    pivot_df = final_dataframe.pivot_table(
        index="dataset_name",
        columns="Acquistion_classified",
        values="percent of acquisition type",
        aggfunc="sum",
        fill_value=0,
    )

    # Create the figure
    fig = go.Figure()

    # Add a trace for each acquisition type
    for medium in pivot_df.columns:
        fig.add_trace(go.Bar(x=pivot_df.index, y=pivot_df[medium], name=medium))

    # Update layout for stacked bars
    fig.update_layout(
        barmode="stack",
        title="Stacked Bar Chart of Acquisition Type Percentages by Dataset",
        xaxis_title="Museum Name",
        yaxis_title="Percent of Acquisition Type",
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(len(pivot_df.index))),
            ticktext=pivot_df.index,
        ),
    )
    fig.update_layout(template="plotly_white")

    return fig
