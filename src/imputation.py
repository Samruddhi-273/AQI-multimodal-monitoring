import pandas as pd
from sklearn.impute import KNNImputer

print("="*60)
print("MISSING DATA IMPUTATION")
print("="*60)

df = pd.read_csv("data/processed/feature_engineered_dataset.csv")

pollutant_columns = [
    "PM2.5","PM10","NO","NO2","NOx","NH3",
    "CO","SO2","O3","Benzene","Toluene",
    "Xylene","AQI"
]

pollutant_columns = [c for c in pollutant_columns if c in df.columns]

print("Missing values before:")
print(df[pollutant_columns].isnull().sum())

# -----------------------
# Linear Interpolation
# -----------------------
linear_df = df.copy()

linear_df[pollutant_columns] = (
    linear_df[pollutant_columns]
    .interpolate(limit_direction="both")
)

linear_df.to_csv(
    "data/processed/interpolated_dataset.csv",
    index=False
)

print("\nInterpolation completed!")

# -----------------------
# KNN on sample only
# -----------------------

sample = linear_df.sample(
    n=50000,
    random_state=42
).copy()

imputer = KNNImputer(n_neighbors=5)

sample[pollutant_columns] = imputer.fit_transform(
    sample[pollutant_columns]
)

sample.to_csv(
    "data/processed/knn_sample_dataset.csv",
    index=False
)

print("\nKNN sample completed!")

print("\nAll datasets saved successfully.")