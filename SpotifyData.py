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

df = df[df["episode_name"].isna()]
df_total_playtime = df.groupby("master_metadata_track_name")["ms_played"].sum().reset_index()
df_total_playtime["total_minutes_listened"] = df_total_playtime["ms_played"] / 60000
df_sorted = df_total_playtime.sort_values(by="total_minutes_listened", ascending=False)

print()
print(df_sorted[["master_metadata_track_name", "total_minutes_listened"]].head(5))
print("\n\n\n")