import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/station_hour.csv")

# Convert datetime column
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Sort by time
df = df.sort_values("Datetime")

# Sensor columns to analyze
sensor_columns = [
    "PM2.5",
    "PM10",
    "NO2",
    "CO",
    "SO2",
    "O3",
    "AQI"
]

for column in sensor_columns:

    if column not in df.columns:
        continue

    temp = df[["Datetime", column]].dropna()

    # Rolling mean (window = 24 hours)
    temp["RollingMean"] = temp[column].rolling(window=24).mean()

    plt.figure(figsize=(12,5))

    plt.plot(temp["Datetime"], temp[column], alpha=0.4, label="Original")

    plt.plot(temp["Datetime"], temp["RollingMean"],
             color="red",
             linewidth=2,
             label="Rolling Mean")

    plt.title(f"Sensor Drift Detection - {column}")

    plt.xlabel("Time")

    plt.ylabel(column)

    plt.legend()

    plt.tight_layout()

    plt.savefig(f"reports/{column}_drift.png")

    plt.close()

print("Sensor drift graphs saved successfully!")