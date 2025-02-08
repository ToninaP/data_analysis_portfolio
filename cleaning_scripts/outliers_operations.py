import pandas as pd


def find_outliers(df, col):

    # Print summary statistics for the cleaned years
    valid_years = df[col].dropna()
    if len(valid_years) > 0:
        print("\nYear statistics:")
        print(f"Earliest year: {valid_years.min()}")
        print(f"Latest year: {valid_years.max()}")

        # Flag potential outliers
        q1 = valid_years.quantile(0.25)
        q3 = valid_years.quantile(0.75)
        iqr = q3 - q1
        outliers = valid_years[
            (valid_years < (q1 - 1.5 * iqr)) | (valid_years > (q3 + 1.5 * iqr))
        ]

        if len(outliers) > 0:
            print(f"\nPotential outliers detected ({len(outliers)} values):")
            print(outliers.value_counts().head())
            print("----------------------------------")
