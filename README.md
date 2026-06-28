# 🌍 AQI Multimodal Environmental Monitoring Pipeline

An end-to-end **Data Science and Machine Learning project** for processing, validating, analyzing, and predicting Air Quality Index (AQI) using large-scale environmental sensor data. The project integrates data engineering, feature engineering, machine learning, physics-based validation, and an interactive Streamlit dashboard.

---

## 🚀 Project Highlights

- Built an end-to-end environmental data pipeline handling **2.5+ million sensor records**
- Performed comprehensive **EDA**, missing value analysis, outlier detection, and sensor drift detection
- Engineered time-based and AQI-specific features for improved model performance
- Implemented **Linear Interpolation** and **KNN Imputation** for missing data handling
- Trained a **Random Forest Regression model** for AQI prediction
- Developed **Physics-Informed Validation** rules for environmental data consistency
- Designed an interactive **Streamlit Dashboard** for visualization and AQI prediction
- Built a **Search & Retrieval System** for querying air quality records

---

# 🏗️ Project Architecture

```
Raw Dataset
      │
      ▼
Data Collection
      │
      ▼
EDA & Data Validation
      │
      ▼
Data Fusion
      │
      ▼
Feature Engineering
      │
      ▼
Missing Value Imputation
      │
      ▼
Machine Learning Model
      │
      ▼
Physics Validation
      │
      ▼
Search Module
      │
      ▼
Interactive Dashboard
```

---

# 📂 Repository Structure

```
AQI_Multimodal_Pipeline
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── random_forest_model.pkl
│
├── reports/
│   └── feature_importance.csv
│
├── src/
│   ├── data_collection.py
│   ├── data_fusion.py
│   ├── feature_engineering.py
│   ├── imputation.py
│   ├── model.py
│   ├── physics.py
│   ├── quality_score.py
│   ├── search.py
│   └── outlier_visualization.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The project uses the **Indian Air Quality Dataset** consisting of:

- Hourly air quality observations
- Air Quality Index (AQI)
- Pollutant concentrations
- Station metadata

**Files Used**

- station_hour.csv
- stations.csv

> Large datasets are excluded from GitHub due to file size limitations.

---

# ⚙️ Features

## 📌 Data Engineering

- Data ingestion
- Data cleaning
- Data fusion
- Quality score generation

---

## 📈 Data Analysis

- Exploratory Data Analysis
- Missing value analysis
- Outlier detection
- Sensor drift analysis

---

## 🧠 Feature Engineering

Generated features include

- Hour
- Day
- Month
- Year
- Day of Week
- Weekend Indicator
- AQI Category

---

## 🤖 Machine Learning

Model:

- Random Forest Regressor

Evaluation Metrics

- MAE
- RMSE
- R² Score

Generated

- Feature Importance Report
- Trained Model (.pkl)

---

## 🌍 Physics-Informed Validation

Validation Rules

- AQI ≥ 0
- PM2.5 ≤ PM10
- CO ≥ 0
- NO₂ ≥ 0
- O₃ ≥ 0

---

## 📊 Dashboard

Interactive dashboard developed using Streamlit with

- Station filtering
- Date filtering
- AQI trends
- Pollutant visualization
- Correlation heatmap
- AQI prediction
- Dataset download

---

# 💻 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Machine Learning | Scikit-Learn |
| Dashboard | Streamlit |
| Model Serialization | Joblib |
| Mapping | Folium |

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/AQI_Multimodal_Pipeline.git

cd AQI_Multimodal_Pipeline

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

# ▶️ Run

Train Model

```bash
python src/model.py
```

Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

# 📈 Future Improvements

- Real-time AQI prediction
- IoT sensor integration
- Weather API integration
- LSTM-based forecasting
- Interactive GIS maps
- Cloud deployment

---

# 👩‍💻 Author

**Samruddhi Magadum**

B.Tech Aerospace Engineering

Indian Institute of Technology Bombay

---

## Note

The trained model and processed datasets are excluded from this repository because of their large size.

To generate them:

1. Place the raw dataset in `data/raw/`.
2. Run:
   python run_pipeline.py

This will recreate the processed datasets and train the Random Forest model.
