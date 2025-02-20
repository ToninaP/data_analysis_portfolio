import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy import stats

def plot_collection_lag_distribution(collection_lag, museum_names):    
    fig, axs = plt.subplots(nrows=11, ncols=1, figsize=(10, 20), sharex=True)
    fig.suptitle('Collection lag distributions')

    for i, (df, museum) in enumerate(zip(collection_lag, museum_names)):
        # Filter data between -5 and 200
        filtered_df = df[(df['Collection_lag'] >= -5) & (df['Collection_lag'] <= 200)]
        
        # Create expanded array based on counts
        expanded_data = np.repeat(filtered_df['Collection_lag'], filtered_df['count'].astype(int))
        
        # Calculate statistics
        mean_val = np.mean(expanded_data)
        median_val = np.median(expanded_data)
        mode_val = stats.mode(expanded_data)[0]
        
        # Create histogram
        axs[i].hist(filtered_df['Collection_lag'],
                    weights=filtered_df['count'],
                    density=True,
                    bins=50,
                    alpha=0.7)
        
        # Calculate KDE
        kde_xs = np.linspace(-5, 200, 200)
        kde = stats.gaussian_kde(expanded_data)
        kde_density = kde(kde_xs)
        
        # Plot KDE curve
        axs[i].plot(kde_xs, kde_density, 'r-', lw=2, label='Distribution')
        
        # Add vertical lines for mean, median, and mode
        axs[i].axvline(mean_val, color='green', linestyle='--', lw=2, label=f'Mean: {mean_val:.1f}')
        axs[i].axvline(median_val, color='blue', linestyle='--', lw=2, label=f'Median: {median_val:.1f}')
        axs[i].axvline(mode_val, color='purple', linestyle='--', lw=2, label=f'Mode: {mode_val:.1f}')
        
        # Add title for each subplot using museum name
        axs[i].set_title(museum, pad=10)
        
        # Optional: Add grid for better readability
        axs[i].grid(True, alpha=0.3)
        
        # Add legend with statistics values
        axs[i].legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Set x-axis limits
    plt.xlim(-5, 200)

    # Adjust layout to prevent overlapping
    plt.tight_layout()
    fig.suptitle('Collection lag distributions', y=1.02)

    # Add common x-label
    fig.text(0.5, -0.01, 'Collection Lag (years)')

    # Add common y-label
    fig.text(0.02, 0.5, 'N of artworks', va='center', rotation='vertical')

    plt.style.use('seaborn-v0_8-pastel')