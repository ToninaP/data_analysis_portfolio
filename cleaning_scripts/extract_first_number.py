import pandas as pd
import re


def extract_first_number(value):
    # Check if the value is NaN or not a string/number
    if pd.isna(value):
        return pd.NA

    # If it's a string or number (int/float), process it
    if isinstance(value, (str, int, float)):
        # Convert to string if it's a number
        if isinstance(value, (int, float)):
            value = str(value)

        # Find all 4-digit numbers
        years = re.findall(r"\b\d{4}\b", value)

        # If years are found, convert first one to numeric
        if years:
            year = pd.to_numeric(years[0])
            # Return year only if it's not greater than 2024
            return year if year <= 2024 else pd.NA

    # Return NA if no valid year is found
    return pd.NA


def extract_last_number(value):
    # Check if the value is NaN or not a string/number
    if pd.isna(value):
        return pd.NA

    # If it's a string or number (int/float), process it
    if isinstance(value, (str, int, float)):
        # Convert to string if it's a number
        if isinstance(value, (int, float)):
            value = str(value)

        # Initialize new_value with the original value
        new_value = value

        # Split by hyphen if present and take last part
        if "-" in value:
            new_value = value.split("-")[-1]

        # Find all 4-digit numbers
        years = re.findall(r"\b\d{4}\b", new_value)

        # If years are found, convert first one to numeric
        if years:
            year = pd.to_numeric(years[0])
            # Return year only if it's not greater than 2024
            return year if year <= 2024 else pd.NA

    # Return NA if no valid year is found
    return pd.NA
