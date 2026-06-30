import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import folium
from streamlit_folium import st_folium

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.uncertainty import predict_with_uncertainty

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AQI Monitoring Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AQI Multimodal Environmental Monitoring Dashboard")

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/processed/interpolated_dataset.csv",
        low_memory=False
    )

    # Clean columns
    df.columns = df.columns.str.strip()

    # Clean Station IDs
    df["StationId"] = df["StationId"].astype(str).str.strip()

    # Datetime
    df["Datetime"] = pd.to_datetime(df["Datetime"])

    return df

df = load_data()

# Load trained model
model = joblib.load("models/random_forest_model.pkl")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.header("Filters")

stations = sorted(df["StationId"].dropna().unique())

selected_station = st.sidebar.selectbox(
    "Select Station",
    stations
)

# Filter station
filtered_df = df[df["StationId"] == selected_station].copy()

# ----------------------------
# Date Filter
# ----------------------------
if not filtered_df.empty:

    min_date = filtered_df["Datetime"].min().date()
    max_date = filtered_df["Datetime"].max().date()

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(selected_dates) == 2:
        start_date, end_date = selected_dates

        filtered_df = filtered_df[
            (filtered_df["Datetime"].dt.date >= start_date) &
            (filtered_df["Datetime"].dt.date <= end_date)
        ]

# ----------------------------
# Pollutant Selection
# ----------------------------
pollutants = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",
    "AQI"
]

available_pollutants = [p for p in pollutants if p in filtered_df.columns]

pollutant = st.sidebar.selectbox(
    "Select Pollutant",
    available_pollutants
)

# ----------------------------
# Dashboard
# ----------------------------
st.header(f"Station : {selected_station}")

if filtered_df.empty:

    st.error("No data available for selected station.")

else:

    # ------------------------
    # KPI Cards
    # ------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Records",
        len(filtered_df)
    )

    col2.metric(
        "Average AQI",
        round(filtered_df["AQI"].mean(),2)
    )

    col3.metric(
        "Maximum AQI",
        round(filtered_df["AQI"].max(),2)
    )

    col4.metric(
        "Minimum AQI",
        round(filtered_df["AQI"].min(),2)
    )

    st.divider()

    # ------------------------
    # Dataset Preview
    # ------------------------

    st.subheader("Dataset Preview")

    st.dataframe(filtered_df.head(20), use_container_width=True)

    st.divider()

    # ------------------------
    # Time Series
    # ------------------------

    st.subheader(f"{pollutant} Trend")

    fig = px.line(
        filtered_df,
        x="Datetime",
        y=pollutant,
        markers=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # ------------------------
    # AQI Histogram
    # ------------------------

    st.subheader("AQI Distribution")

    fig2 = px.histogram(
        filtered_df,
        x="AQI",
        nbins=40
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ------------------------
    # AQI Category Pie Chart
    # ------------------------

    if "AQI_Category" in filtered_df.columns:

        st.subheader("AQI Categories")

        fig3 = px.pie(
            filtered_df,
            names="AQI_Category"
        )

        st.plotly_chart(fig3, use_container_width=True)

    # ------------------------
    # Pollutant Correlation
    # ------------------------

    st.subheader("Pollutant Correlation")

    numeric_cols = [
        c for c in pollutants
        if c in filtered_df.columns
    ]

    corr = filtered_df[numeric_cols].corr()

    fig4 = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ------------------------
    # Download Button
    # ------------------------

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Filtered Data",
        csv,
        file_name=f"{selected_station}.csv",
        mime="text/csv"
    )

st.success("Dashboard Loaded Successfully!")

# ==========================================================
# AQI Prediction Panel
# ==========================================================

st.divider()

st.header("🤖 AQI Prediction")

st.write("Enter pollutant concentrations to predict AQI.")

col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input("PM2.5", value=50.0)
    pm10 = st.number_input("PM10", value=80.0)
    no = st.number_input("NO", value=5.0)
    no2 = st.number_input("NO2", value=20.0)

with col2:
    nox = st.number_input("NOx", value=25.0)
    nh3 = st.number_input("NH3", value=10.0)
    co = st.number_input("CO", value=1.0)
    so2 = st.number_input("SO2", value=15.0)

with col3:
    o3 = st.number_input("O3", value=40.0)
    benzene = st.number_input("Benzene", value=1.0)
    toluene = st.number_input("Toluene", value=2.0)
    xylene = st.number_input("Xylene", value=0.5)

if st.button("Predict AQI"):

    input_df = pd.DataFrame([[

        pm25,
        pm10,
        no,
        no2,
        nox,
        nh3,
        co,
        so2,
        o3,
        benzene,
        toluene,
        xylene

    ]], columns=[

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

    ])

    result = predict_with_uncertainty(input_df)
    prediction = result["prediction"]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Predicted AQI", f"{prediction:.2f}")

    with c2:
        st.metric("Uncertainty", f"±{result['std']:.2f}")

    with c3:
        st.metric(
            "95% Confidence Interval",
            f"{result['lower']:.1f} - {result['upper']:.1f}"
        )

    if result["std"] < 10:
        st.success("✅ High Confidence")
    elif result["std"] < 20:
        st.warning("🟡 Moderate Confidence")
    else:
        st.error("🔴 Low Confidence")

    # AQI Category
    if prediction <= 50:
        st.success("🟢 Good Air Quality")
    elif prediction <= 100:
        st.info("🟡 Satisfactory")
    elif prediction <= 200:
        st.warning("🟠 Moderate")
    elif prediction <= 300:
        st.warning("🔴 Poor")
    elif prediction <= 400:
        st.error("🟣 Very Poor")
    else:
        st.error("⚫ Severe")
        
st.divider()
st.header("📊 Model Comparison")

comparison = pd.read_csv("reports/model_comparison.csv")

st.dataframe(
    comparison,
    use_container_width=True
)

fig = px.bar(
    comparison,
    x="Model",
    y="R2 Score",
    color="Model",
    text="R2 Score",
    title="Model Performance (R² Score)"
)

fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")

st.plotly_chart(fig, use_container_width=True)

best_model = comparison.loc[
    comparison["R2 Score"].idxmax(),
    "Model"
]

st.success(f"🏆 Best Performing Model: {best_model}")