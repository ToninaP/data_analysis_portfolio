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
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Kiasma/APIexample-master/kiasma_flattened.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/smk/smk_flattened.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/Kiasma/APIexample-master/ateneum_flattened.csv",
        "/Users/CUDAN/Documents/TLU/Data analysis/data/queensland/queensland_flattened.csv",
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
        "kiasma",
        "smk",
        "ateneum",
        "queensland",
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

    return raw_data, dataset_names
