import pandas as pd
import plotly.graph_objects as go


def plot_medium_bar(museum_data, museum_names, min_year=1860):
    fig = go.Figure()

    # Process each museum dataset and plot each as a trace
    for df, museum_name in zip(museum_data, museum_names):
        # Filter data based on the minimum year
        df_filtered = df[df["Date_creation_year"] >= min_year]

        # Group by "Medium_classified" and count the occurrences
        df_grouped = (
            df_filtered.groupby(["Medium_classified"]).size().reset_index(name="Count")
        )

        # Add the 'percent of media' column
        df_grouped["percent of media"] = (
            100 * df_grouped["Count"] / df_grouped["Count"].sum()
        )

        # Add a new column 'dataset_name' to store the name of the museum
        df_grouped["dataset_name"] = museum_name

        # Pivot the grouped dataframe for stacked bar chart compatibility
        pivot_df = df_grouped.pivot_table(
            index="dataset_name",
            columns="Medium_classified",
            values="percent of media",
            aggfunc="sum",
            fill_value=0,
        )

        # Add a trace for each medium in the current dataset
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
