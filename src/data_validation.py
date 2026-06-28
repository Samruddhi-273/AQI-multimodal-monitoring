import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/station_hour.csv")

print("=" * 60)
print("OUTLIER DETECTION")
print("=" * 60)

# Numerical columns to check
numeric_columns = [
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
    "Xylene",
    "AQI"
]

outlier_summary = []

for column in numeric_columns:

    if column not in df.columns:
        continue

    data = df[column].dropna()

    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = data[(data < lower) | (data > upper)]

    outlier_summary.append({
        "Column": column,
        "Outliers": len(outliers),
        "Lower Limit": round(lower, 2),
        "Upper Limit": round(upper, 2)
    })

result = pd.DataFrame(outlier_summary)

print(result)

result.to_csv("reports/outlier_report.csv", index=False)

print("\nOutlier report saved successfully!")