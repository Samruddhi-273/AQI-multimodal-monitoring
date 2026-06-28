import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

print("="*60)
print("AQI PREDICTION MODEL")
print("="*60)

# Load data
df = pd.read_csv("data/processed/interpolated_dataset.csv")

# Features
features = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",
    "Benzene",
    "Toluene",
    "Xylene"
]

# Keep only available columns
features = [c for c in features if c in df.columns]

# Remove rows where AQI is missing
df = df.dropna(subset=["AQI"])

# Use a sample for training
df = df.sample(n=100000, random_state=42)

X = df[features]
y = df["AQI"]

print(f"Training samples: {len(df)}")

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("\nModel Performance")
print("-------------------------")
print("MAE :", mean_absolute_error(y_test, pred))
print("RMSE:", mean_squared_error(y_test, pred) ** 0.5)
print("R2  :", r2_score(y_test, pred))

# Feature importance
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=False)

print("\nFeature Importance")
print(importance)

importance.to_csv(
    "reports/feature_importance.csv",
    index=False
)

joblib.dump(
    model,
    "models/random_forest_model.pkl"
)

print("\nModel saved successfully!")