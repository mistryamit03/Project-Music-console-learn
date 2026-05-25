# Importing pandas and exploratory analysis

import pandas as pd 


file_path = "data/raw/universal_top_spotify_songs.csv"


df = pd.read_csv(file_path)


print(df.shape)

print(df.columns)

print(df.head())


# Task 2: Select only the columns needed for first staging practice.

selected_columns = [
    "spotify_id",
    "name",
    "artists",
    "daily_rank",
    "country",
    "snapshot_date"
]

df_selected = df[selected_columns]

print(df_selected.head())


# Task 3: Inspect selected columns for missing values and data types: Basic data profiling before cleaning.


print(df_selected.isna().sum())
print(df_selected.info())


# Task 4: Create a clean working DataFrame before cleaning: Creating a safe working copy before modifying selected data.

df_clean = df_selected.copy()


print(df_clean.head())