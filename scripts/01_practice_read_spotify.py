import pandas as pd 


file_path = "data/raw/universal_top_spotify_songs.csv"


df = pd.read_csv(file_path)


print(df.shape)

print(df.columns)

print(df.head())

import pandas as pd


