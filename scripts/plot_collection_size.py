import plotly.graph_objects as go


def plot_collection_size(museums_data, museum_names, log_scale=False):
    """This is a function to show how many artworks every museum has in their collection
    Arg:
        museums_data: a list of pandas dataframes
        museum_names: a list of strings with museum names from museum_data
        log_scale: Boolean, to add logarithmic scaling on y-axis
    Returns:
        fig: one stacked bar chart figure showing a proportion of modern and contemporary artworks vs classical artworks
    """
    # Ensure the number of museums matches the data provided
    if len(museums_data) != len(museum_names):
        raise ValueError(
            "The number of dataset sizes must match the number of dataset names."
        )

    # Initialize lists to store the count of contemporary artworks and non-contemporary artworks
    contemporary_sizes = []
    non_contemporary_sizes = []

    # Loop through each museum's data to classify artworks
    for df in museums_data:
        # Count contemporary artworks (created in or after 1860)
        contemporary_count = len(df[df["Date_creation_year"] >= 1860])
        # Count non-contemporary artworks (created before 1860)
        non_contemporary_count = len(df[df["Date_creation_year"] < 1860])

        contemporary_sizes.append(contemporary_count)
        non_contemporary_sizes.append(non_contemporary_count)

    # Sort museums based on the contemporary collection size in descending order
    sorted_data = sorted(
        zip(contemporary_sizes, non_contemporary_sizes, museum_names),
        reverse=True,
        key=lambda x: x[0],  # Sort by contemporary collection size
    )

    # Unzip the sorted data into individual lists
    contemporary_sizes_sorted, non_contemporary_sizes_sorted, museum_names_sorted = zip(
        *sorted_data
    )

    # Create the stacked bar chart
    fig = go.Figure()

    # Add bars for contemporary artworks (post-1860)
    fig.add_trace(
        go.Bar(
            x=museum_names_sorted,
            y=contemporary_sizes_sorted,
            name="Contemporary Artworks (Post-1860)",
            marker_color="skyblue",  # Light blue for contemporary artworks
            text=contemporary_sizes_sorted,  # Display the number of artworks on top of each bar
            textposition="inside",  # Place text labels inside the bars
        )
    )

    # Add bars for non-contemporary artworks (pre-1860)
    fig.add_trace(
        go.Bar(
            x=museum_names_sorted,
            y=non_contemporary_sizes_sorted,
            name="Non-Contemporary Artworks (Pre-1860)",
            marker_color="lightcoral",  # Light coral for non-contemporary artworks
            text=non_contemporary_sizes_sorted,
            textposition="inside",
        )
    )

    # Update layout for better readability and a single graph
    fig.update_layout(
        title="Museum Art Collections by Artwork Creation Date",
        # barmode="stack",  # Stack the bars to show total collection size
        xaxis_title="Museum",
        yaxis_title="Number of Artworks in Collection",
        showlegend=True,  # Show legend for the plot
    )

    # Apply logarithmic scale to the y-axis if log_scale is True
    if log_scale:
        fig.update_yaxes(type="log")

    # Set template for the plot (light theme)
    fig.update_layout(template="plotly_white")

    return fig
