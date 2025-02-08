import numpy as np
import pandas as pd
import os

while True:
    filename = input("Enter a valid filename: ") + ".json"
    if os.path.isfile(filename):
        print(f"File '{filename}' found!")
        break
    else:
        print("File not found. Please try again.")
df = pd.read_json(filename)

# exclude podcasts
df = df[df["episode_name"].isna()]

# sum the ms of all songs by the same track name and convert it to minutes
df_total_playtime = df.groupby("master_metadata_track_name")["ms_played"].sum().reset_index()
df_total_playtime["total_minutes_listened"] = df_total_playtime["ms_played"] / 60000

# sort by total minutes listened
df_sorted = df_total_playtime.sort_values(by="total_minutes_listened", ascending=False)

# filter all data to show only the track name and the total minutes listened
print()
print(df_sorted[["master_metadata_track_name", "total_minutes_listened"]].head(5))
print("\n\n\n")