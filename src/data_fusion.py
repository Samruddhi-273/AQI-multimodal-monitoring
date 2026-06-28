import pandas as pd

print("=" * 60)
print("DATA FUSION PIPELINE")
print("=" * 60)

# Load datasets
sensor_data = pd.read_csv("data/raw/station_hour.csv")
station_info = pd.read_csv("data/raw/stations.csv")

print("\nSensor Data Shape:", sensor_data.shape)
print("Station Info Shape:", station_info.shape)

# Display columns
print("\nSensor Data Columns:")
print(sensor_data.columns.tolist())

print("\nStation Info Columns:")
print(station_info.columns.tolist())

# Merge datasets
merged_data = pd.merge(
    sensor_data,
    station_info,
    on="StationId",
    how="left"
)

print("\nMerged Dataset Shape:", merged_data.shape)

print("\nFirst 5 Rows:")
print(merged_data.head())

# Save merged dataset
merged_data.to_csv(
    "data/processed/fused_dataset.csv",
    index=False
)

print("\nFused dataset saved successfully!")