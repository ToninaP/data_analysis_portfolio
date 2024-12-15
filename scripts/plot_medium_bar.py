import pandas as pd
import plotly.graph_objects as go


def plot_medium_bar(museum_data, museum_names, min_year=1860):
    data_transformed = []

    for df in museum_data:
        # Filter data based on the minimum year
        df_filtered = df[df["Date_creation_year"] >= min_year]

        # Group by "Medium_classified" and count the number of occurrences
        df_grouped = (
            df_filtered.groupby(["Medium_classified"]).size().reset_index(name="Count")
        )

        data_transformed.append(df_grouped)

    for df in data_transformed:
        df["percent of media"] = 100 * df["Count"] / df["Count"].sum()

    # Create an empty list to hold the dataframes with the new column
    data_with_names = []

    # Iterate over the dataframes and add the corresponding dataset name
    for i, df in enumerate(data_transformed):
        # Add a new column 'dataset_name' with the dataset name
        df["dataset_name"] = museum_names[i]
        data_with_names.append(df)

    # Concatenate all dataframes into one
    final_dataframe = pd.concat(data_with_names, ignore_index=True)

    # Prepare for stacked bar chart
    # We need to pivot the data so that each medium will have its own column, with counts for each dataset
    pivot_df = final_dataframe.pivot_table(
        index="dataset_name",
        columns="Medium_classified",
        values="percent of media",
        aggfunc="sum",
        fill_value=0,
    )

    # Create the figure
    fig = go.Figure()

    # Add a trace for each medium
    for medium in pivot_df.columns:
        fig.add_trace(go.Bar(x=pivot_df.index, y=pivot_df[medium], name=medium))

    # Update layout for stacked bars
    fig.update_layout(
        barmode="stack",
        title="Stacked Bar Chart of Media Percentages by Dataset",
        xaxis_title="Museum Name",
        yaxis_title="Percent of Media",
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(len(museum_names))),
            ticktext=museum_names,
        ),
    )
    fig.update_layout(template="plotly_white")
    return fig
