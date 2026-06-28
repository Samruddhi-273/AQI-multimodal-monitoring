import pandas as pd

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# Load fused dataset
df = pd.read_csv("data/processed/fused_dataset.csv")

# -------------------------
# Convert Datetime
# -------------------------
df["Datetime"] = pd.to_datetime(df["Datetime"])

# -------------------------
# Time Features
# -------------------------
df["Hour"] = df["Datetime"].dt.hour
df["Day"] = df["Datetime"].dt.day
df["Month"] = df["Datetime"].dt.month
df["Year"] = df["Datetime"].dt.year
df["DayOfWeek"] = df["Datetime"].dt.day_name()

# -------------------------
# Weekend Feature
# -------------------------
df["IsWeekend"] = df["Datetime"].dt.weekday >= 5

# -------------------------
# AQI Category
# -------------------------
def categorize_aqi(aqi):
    if pd.isna(aqi):
        return "Unknown"
    elif aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

df["AQI_Category"] = df["AQI"].apply(categorize_aqi)

print("\nNew Features Created:")
print([
    "Hour",
    "Day",
    "Month",
    "Year",
    "DayOfWeek",
    "IsWeekend",
    "AQI_Category"
])

# Save
df.to_csv(
    "data/processed/feature_engineered_dataset.csv",
    index=False
)

print("\nFeature engineered dataset saved successfully!")
print("\nFinal Shape:", df.shape)