import pandas as pd

data = pd.read_csv("Earthquakes_USGS_1900-1950.csv")
total_earthquakes = len(data)

# Calculate the Average magnitude across all earthquakes
avg_magnitude = data["magnitude"].mean()

# Identify the top 5 strongest earthquakes by magnitude
top_5_strongest = data.sort_values(by="magnitude", ascending=False).head(5)

# Find earthquakes deeper than 300 km
deep_earthquakes_count = len(data[data["depth"] > 300])

# Write a summary report
filename = "earthquake_report.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Total number of earthquakes = {total_earthquakes}\n")
    f.write(f"Average Magnitude = {avg_magnitude:.2f}\n")

    f.write("Top 5 Strongest Earthquakes\n")
    for i, (index, row) in enumerate(top_5_strongest.iterrows(), start=1):
        f.write(f"   {i}. {row['date']}, {row['location']}, {row['magnitude']}\n")

    f.write(f"Total numbers of earthquakes deeper than 300 km = {deep_earthquakes_count}\n")