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
df_selected.info()


# Task 4: Create a clean working DataFrame before cleaning: Creating a safe working copy before modifying selected data.

df_clean = df_selected.copy()


print(df_clean.head())
df_clean.shape

# Task 5: Clean text columns: Cleaning text fields in a DataFrame. For this task, clean only these columns inside df_clean


df_clean["spotify_id"] = df_clean["spotify_id"].str.strip()
df_clean["name"] = df_clean["name"].str.strip()
df_clean["artists"] = df_clean["artists"].str.strip()
df_clean["country"] = df_clean["country"].str.strip()
df_clean["country"] = df_clean["country"].str.upper()


print(df_clean.tail(5))

# Task 6: Handle missing values using critical-field logic: Deciding which missing values actually break the ingestion pipeline.
# Missing country? Bad for market analysis.
# Missing snapshot_date? Bad for time analysis.
# Missing spotify_id? Bad for track identity.
# Missing daily_rank? Bad for ranking/chart logic.
# Missing name? Annoying, but not always fatal.



# subset = Only check missing values in these specific columns.


before_rows = df_clean.shape[0]

critical_columns = ["spotify_id", "daily_rank", "country", "snapshot_date"]

df_clean = df_clean.dropna(subset=critical_columns)

after_rows = df_clean.shape[0]

removed_rows = before_rows - after_rows



print("Rows before cleaning", before_rows)
print("Rows after cleaning", after_rows)
print("Removed Rows", removed_rows)
print((df_clean.isna()).sum())


# Task 7: Convert snapshot_date into a real date: Date parsing in pandas.


print("snaphot_date dtype before conversion:")
print(df_clean["snapshot_date"].dtype)


df_clean["snapshot_date"] = pd.to_datetime(df_clean["snapshot_date"],errors="coerce")


print("snapshot_date dtype after conversion:")
print(df_clean["snapshot_date"].dtype)


print("Missing/invalid snapshot_date values after conversion:")
print(df_clean[["spotify_id", "country", "snapshot_date"]].isna().sum())