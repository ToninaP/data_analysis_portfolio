import pandas as pd
import re


def extract_first_number(value):
    # Check if the value is NaN or not a string/number
    if pd.isna(value):  # Check for NaN
        return ""  # Return empty string and 0 count for NaN values

    # If it's a string, replace symbols with spaces
    if isinstance(value, str):  # If it's a string
        years = re.findall(r"\b\d{4}\b", value)  # Find all 4-digit numbers
        if years:  # If the list is not empty
            year = years[0]
        else:  # If no years are found, set to a default value
            year = ""
    # If it's an int or float, convert to string and process
    elif isinstance(value, (int, float)):  # If it's a number (int or float)
        value = str(value)  # Convert to string
        years = re.findall(r"\b\d{4}\b", value)  # Try to find 4-digit numbers
        if years:  # If the list is not empty
            year = years[0]
        else:  # If no years are found, set to a default value
            year = ""

    return year
