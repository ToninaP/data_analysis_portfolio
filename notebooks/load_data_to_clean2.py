import pandas as pd
from flatten_json import flatten
import json
import re


def load_data_to_clean():
    # Load csv files and json files that do not require flattening or parsing
    data_paths_standard = [
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Met/MetObjects.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Reina Sofia/raw_data/reina_sofia3.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Tate/tate_raw.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Centre Pompidou/merged_file.json",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Moma/Artworks.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/whitney/whitney_data_raw.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/national gallery (DC)/national_gallery_raw.csv",
    ]
    raw_data = []
    dataset_names = [
        "met",
        "reina_sofia",
        "tate",
        "pompidou",
        "moma",
        "whitney",
        "national_gallery",
    ]
    for df, dataset_name in zip(data_paths_standard, dataset_names):
        # Step 1: Check if '.json' exists in the input
        if ".json" in df:
            data = pd.read_json(df)
        elif ".csv" in df:
            data = pd.read_csv(df, on_bad_lines="skip", low_memory=False)
        else:
            print(f"Cannot load {df}")
            continue

        raw_data.append(data)
        print(f"Loaded {dataset_name} with shape: {data.shape}")

    # Load datasets that require flattening
    data_paths_flattening = [
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Kiasma/APIexample-master/dataset.json",  # Kiasma
        "/Users/CUDAN/Documents/TLU/Data analysis/data/smk/smk_all_da.json",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Kiasma/APIexample-master/dataset.json",  # Ateneum
    ]
    flat_data = []
    dictionary_data = []
    for df in data_paths_flattening:
        with open(df, "r") as file:
            data = json.load(file)
            dictionary_data.append(data)

    for df in dictionary_data:
        flattened_data = [flatten(record) for record in df]
        data = pd.DataFrame(flattened_data)
        flat_data.append(data)
        print(f"Loaded flattened data with shape: {data.shape}")

    # Separate kiasma and ateneum
    flat_data[0] = flat_data[0][
        flat_data[0]["responsibleOrganisation"]
        == "Kansallisgalleria / Nykytaiteen museo Kiasma"
    ]
    flat_data[2] = flat_data[2][
        flat_data[2]["responsibleOrganisation"]
        == "Kansallisgalleria / Ateneumin taidemuseo"
    ]

    new_datasets = ["kiasma", "smk", "ateneum"]
    dataset_names.extend(new_datasets)
    raw_data.extend(flat_data)

    # File path to the raw JSON data
    data_path = "/Users/CUDAN/Documents/TLU/Data analysis/data/queensland/raw_data.json"

    # Load the JSON data
    with open(data_path, "r") as file:
        data = json.load(file)

    # Extract the column names from the "fields" part of the JSON
    columns = [field["id"] for field in data["fields"]]

    # Extract the records (the data)
    records = data["records"]

    # Create the DataFrame
    queensland = pd.DataFrame(records, columns=columns)
    raw_data.append(queensland)
    dataset_names.append("queensland")
    print(f"Loaded queensland with shape: {queensland.shape}")

    # Prepare queensland for analysis
    def assign_dates(row, column_name):
        text = row[column_name]

        # Use regular expressions to find patterns for years
        years = re.findall(r"\b\d{4}\b", text)  # Find all 4-digit numbers

        # If exactly one year is found, it is the birth year
        if len(years) == 1:
            row["birth_date"] = int(years[0])
            row["death_date"] = None  # No death date if only one year is found
        # If exactly two years are found, assign the first to birth_date and the second to death_date
        elif len(years) >= 2:
            row["birth_date"] = int(years[0])
            row["death_date"] = int(years[1])
        else:
            # If no years or more than two years are found, set both to None
            row["birth_date"] = None
            row["death_date"] = None

        return row

    raw_data[10]["Artist"] = raw_data[10]["Person"].str.split("\n").str.get(0)
    raw_data[10]["Nationality"] = (
        raw_data[10]["Person"].str.split("\n").str.get(-1).str.split("1").str.get(0)
    )
    raw_data[10]["birth_date"] = None
    raw_data[10]["death_date"] = None
    raw_data[10] = raw_data[10].apply(assign_dates, axis=1, column_name="Person")

    # Removing duplicate columns created with flattening json
    raw_data[7] = raw_data[7].loc[:, ~raw_data[7].columns.str.startswith("keywords")]
    raw_data[7] = raw_data[7].loc[:, ~raw_data[7].columns.str.startswith("multimedia")]
    raw_data[7]["artist_name"] = (
        raw_data[7]["people_0_firstName"] + " " + raw_data[7]["people_0_familyName"]
    )

    # Removing duplicate columns created with flattening json
    raw_data[9] = raw_data[9].loc[:, ~raw_data[9].columns.str.startswith("keywords")]
    raw_data[9] = raw_data[9].loc[:, ~raw_data[9].columns.str.startswith("multimedia")]
    raw_data[9]["artist_name"] = (
        raw_data[9]["people_0_firstName"] + " " + raw_data[9]["people_0_familyName"]
    )

    return raw_data, dataset_names
