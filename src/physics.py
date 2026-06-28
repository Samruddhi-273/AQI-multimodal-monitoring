import pandas as pd
import numpy as np

print("=" * 60)
print("PHYSICS INFORMED AQI VALIDATION")
print("=" * 60)

# Load processed dataset
df = pd.read_csv("data/processed/interpolated_dataset.csv")

# -------------------------------------------------------
# Rule 1 : AQI should never be negative
# -------------------------------------------------------

df["Physics_AQI_Positive"] = df["AQI"] >= 0

# -------------------------------------------------------
# Rule 2 : PM2.5 should not exceed PM10
# -------------------------------------------------------

if "PM2.5" in df.columns and "PM10" in df.columns:

    df["Physics_PM_Check"] = df["PM2.5"] <= df["PM10"]

else:

    df["Physics_PM_Check"] = np.nan

# -------------------------------------------------------
# Rule 3 : CO concentration should be non-negative
# -------------------------------------------------------

if "CO" in df.columns:

    df["Physics_CO_Check"] = df["CO"] >= 0

else:

    df["Physics_CO_Check"] = np.nan

# -------------------------------------------------------
# Rule 4 : NO2 concentration should be non-negative
# -------------------------------------------------------

if "NO2" in df.columns:

    df["Physics_NO2_Check"] = df["NO2"] >= 0

else:

    df["Physics_NO2_Check"] = np.nan

# -------------------------------------------------------
# Rule 5 : O3 concentration should be non-negative
# -------------------------------------------------------

if "O3" in df.columns:

    df["Physics_O3_Check"] = df["O3"] >= 0

else:

    df["Physics_O3_Check"] = np.nan

# -------------------------------------------------------
# Overall Physics Score
# -------------------------------------------------------

physics_columns = [
    "Physics_AQI_Positive",
    "Physics_PM_Check",
    "Physics_CO_Check",
    "Physics_NO2_Check",
    "Physics_O3_Check"
]

df["Physics_Score"] = (
    df[physics_columns]
    .sum(axis=1)
    / len(physics_columns)
) * 100

print("\nAverage Physics Score:")

print(round(df["Physics_Score"].mean(),2))

print("\nPhysics Rule Summary")

for col in physics_columns:

    print(f"{col}: {df[col].sum()} Valid Records")

# Save

df.to_csv(
    "data/processed/physics_validated_dataset.csv",
    index=False
)

print("\nPhysics validated dataset saved successfully!")