import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/station_hour.csv")

# Columns to visualize
columns = [
    "PM2.5",
    "PM10",
    "NO2",
    "CO",
    "SO2",
    "O3",
    "AQI"
]

for column in columns:

    if column not in df.columns:
        continue

    plt.figure(figsize=(8,4))

    plt.boxplot(df[column].dropna())

    plt.title(f"Boxplot of {column}")

    plt.ylabel(column)

    plt.grid(True)

    plt.savefig(f"reports/{column}_boxplot.png")

    plt.close()

print("All boxplots saved successfully!")