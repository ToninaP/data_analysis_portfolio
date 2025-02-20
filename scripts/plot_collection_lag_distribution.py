import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def plot_collection_lag_distribution(collection_lag, museum_names):    
    fig, axs = plt.subplots(nrows=11, ncols=1, figsize=(10, 20), sharex=True)
    fig.suptitle('Collection lag distributions')

    for i, (df, museum) in enumerate(zip(collection_lag, museum_names)):
        # Filter data between -5 and 200
        filtered_df = df[(df['Collection_lag'] >= -5) & (df['Collection_lag'] <= 200)]
        
        # Create histogram
        axs[i].hist(filtered_df['Collection_lag'],
                    weights=filtered_df['count'],
                    density=True,
                    bins=50,
                    alpha=0.7)
        
        # Calculate KDE
        
        kde_xs = np.linspace(-5, 200, 200)
        kde = stats.gaussian_kde(np.repeat(filtered_df['Collection_lag'], filtered_df['count'].astype(int)))
        kde_density = kde(kde_xs)
        
        # Plot KDE curve
        axs[i].plot(kde_xs, kde_density, 'r-', lw=2, label='KDE')
        
        # Add title for each subplot using museum name
        axs[i].set_title(museum, pad=10)
        
        # Optional: Add grid for better readability
        axs[i].grid(True, alpha=0.3)
        
        # Add legend
        axs[i].legend()

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