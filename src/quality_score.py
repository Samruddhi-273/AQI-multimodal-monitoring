import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/station_hour.csv")

print("=" * 60)
print("DATA QUALITY SCORE")
print("=" * 60)

# Total missing values per row
missing_count = df.isnull().sum(axis=1)

# Missing percentage per row
missing_percentage = (missing_count / len(df.columns)) * 100

# Quality Score (100 = perfect)
quality_score = 100 - missing_percentage

quality_score = quality_score.clip(lower=0)

df["Quality_Score"] = quality_score.round(2)

print(df[["Quality_Score"]].head())

# Save processed dataset
df.to_csv(
    "data/processed/station_hour_quality.csv",
    index=False
)

print("\nQuality scores generated successfully!")

print("\nAverage Quality Score:")
print(df["Quality_Score"].mean().round(2))