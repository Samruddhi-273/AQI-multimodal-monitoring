import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv(
    "data/processed/feature_engineered_dataset.csv",
    low_memory=False
)

print("Dataset Loaded")
print(df.shape)

# ---------------------------------------
# Remove Missing AQI
# ---------------------------------------

df = df.dropna(subset=["AQI"])
df = df.sample(n=100000, random_state=42)

print("Sampled Dataset Shape:", df.shape)

# ---------------------------------------
# Feature Selection
# ---------------------------------------

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

X = df[features]

# Fill remaining missing values
X = X.fillna(X.mean(numeric_only=True))

y = df["AQI"]


# ---------------------------------------
# Train Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------
# Models
# ---------------------------------------

models = {

    "Linear Regression":
        LinearRegression(),

    "Decision Tree":
        DecisionTreeRegressor(
            random_state=42,
            max_depth=20
        ),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=50,
            random_state=42,
            n_jobs=-1
        ),

    "Gradient Boosting":
        GradientBoostingRegressor(
            random_state=42
        )

}

results = []

# ---------------------------------------
# Train & Evaluate
# ---------------------------------------

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    results.append([
        name,
        mae,
        rmse,
        r2
    ])

# ---------------------------------------
# Results
# ---------------------------------------

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "MAE",
        "RMSE",
        "R2 Score"
    ]
)

print(results_df)

# ---------------------------------------
# Save CSV
# ---------------------------------------

results_df.to_csv(
    "reports/model_comparison.csv",
    index=False
)

print("\nCSV Saved")

# ---------------------------------------
# Plot
# ---------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    results_df["Model"],
    results_df["R2 Score"]
)

plt.ylabel("R² Score")
plt.title("Model Comparison")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    "reports/model_comparison.png",
    dpi=300
)

plt.show()

print("\nPlot Saved")