import pandas as pd

print("=" * 60)
print("AQI Multimodal Environmental Monitoring Pipeline")
print("=" * 60)

# Load datasets
station_hour = pd.read_csv("data/raw/station_hour.csv")
stations = pd.read_csv("data/raw/stations.csv")

print("\nDatasets loaded successfully!")

# -------------------------------
# Dataset Information
# -------------------------------
print("\n========== STATION HOUR DATASET ==========")

print("\nShape:")
print(station_hour.shape)

print("\nColumns:")
print(station_hour.columns.tolist())

print("\nData Types:")
print(station_hour.dtypes)

print("\nFirst 5 Rows:")
print(station_hour.head())

print("\nLast 5 Rows:")
print(station_hour.tail())

print("\nSummary Statistics:")
print(station_hour.describe())

# -------------------------------
# Missing Values
# -------------------------------
print("\n========== MISSING VALUES ==========")

missing = station_hour.isnull().sum()

print(missing)

print("\nMissing Percentage:")

missing_percent = (missing / len(station_hour)) * 100

print(missing_percent.round(2))

# -------------------------------
# Station Dataset
# -------------------------------
print("\n========== STATIONS DATASET ==========")

print("\nShape:")
print(stations.shape)

print("\nColumns:")
print(stations.columns.tolist())

print("\nFirst 5 Rows:")
print(stations.head())

missing_report = pd.DataFrame({
    "Missing Count": missing,
    "Missing Percentage": missing_percent.round(2)
})

missing_report.to_csv(
    "reports/missing_value_report.csv",
    index=True
)

print("\nMissing value report saved successfully!")