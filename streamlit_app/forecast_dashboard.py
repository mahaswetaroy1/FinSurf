import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

# --------- Utility Function ---------
def load_data(actual_path, forecast_path):
    try:
        df_actual = pd.read_csv(actual_path)
        df_forecast = pd.read_csv(forecast_path)

        # Rename for consistency
        df_actual.rename(columns={"ds": "Month", "y": "Actual"}, inplace=True)
        df_forecast.rename(columns={"ds": "Month", "yhat": "Forecast", "yhat_lower": "Lower", "yhat_upper": "Upper"}, inplace=True)

        # Ensure datetime
        df_actual["Month"] = pd.to_datetime(df_actual["Month"])
        df_forecast["Month"] = pd.to_datetime(df_forecast["Month"])

        return df_actual, df_forecast
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

def plot_forecast(df_actual, df_forecast, title):
    df_merged = pd.merge(df_actual, df_forecast, on="Month", how="outer")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_merged["Month"], df_merged["Actual"], label="Actual", marker='o')
    ax.plot(df_merged["Month"], df_merged["Forecast"], label="Forecast", marker='x')

    if "Lower" in df_merged.columns and "Upper" in df_merged.columns:
        ax.fill_between(df_merged["Month"], df_merged["Lower"], df_merged["Upper"], alpha=0.3, color='orange', label="Confidence Interval")

    ax.set_title(title)
    ax.set_xlabel("Month")
    ax.set_ylabel("Value")
    ax.legend()
    st.pyplot(fig)

# --------- Main App ---------
st.set_page_config(page_title="Forecast Overlay Dashboard", layout="wide")
st.title("📊 Forecast Overlay Dashboard")
st.caption("Compare actuals vs forecast (Prophet + SARIMA) for repayment, churn, and segment performance.")

view = st.sidebar.selectbox("🔍 Select Dashboard View", [
    "Total Repayment",
    "Churn Risk Forecast",
    "Segment-Level Forecasts",
    "Recommendations"
])

# --------- Total Repayment ---------
if view == "Total Repayment":
    st.header("Total Repayment Forecast")
    df_actual, df_forecast = load_data(
        "../actuals/actual_total_repayment.csv",
        "../forecasts/prophet_total_repayment.csv"
    )
    if df_actual is not None and df_forecast is not None:
        plot_forecast(df_actual, df_forecast, title="Total Repayment: Actual vs Forecast")

# --------- Churn Forecast ---------
elif view == "Churn Risk Forecast":
    st.header("Churn Risk Forecast")
    df_actual, df_forecast = load_data(
        "../actuals/actual_churn_rate.csv",
        "../forecasts/prophet_churn_forecast.csv"
    )
    if df_actual is not None and df_forecast is not None:
        plot_forecast(df_actual, df_forecast, title="Churn Risk: Actual vs Forecast")

# --------- Segment Forecasts ---------
elif view == "Segment-Level Forecasts":
    st.header("Segment-Level Loan Volume Forecasts")

    segment_options = [
        "At-Risk Value Drainers",
        "Budget Loyalists",
        "High-Value Champions",
        "Long-term Sleepers"
    ]

    segment = st.selectbox("Select Segment", segment_options)

    # Filename formatting
    clean_segment = segment.replace(" ", "_")
    actual_file = f"../actuals/actual_segment_{clean_segment}.csv"
    forecast_file = f"../forecasts/forecast_segment_{clean_segment}.csv"

    if os.path.exists(actual_file) and os.path.exists(forecast_file):
        df_actual, df_forecast = load_data(actual_file, forecast_file)
        if df_actual is not None and df_forecast is not None:
            plot_forecast(df_actual, df_forecast, title=f"{segment}: Actual vs Forecast")
    else:
        st.error(f"Files for segment '{segment}' not found.")

# --------- Recommendations ---------
elif view == "Recommendations":
    st.header("📌 Business Recommendations")
    st.markdown("""
    - 📈 **Total Repayment Surge**: Investigate post-2015 spike in repayment activity.
    - 🔍 **Segment Monitoring**: Long-term Sleepers show volatile patterns – recommend closer monitoring.
    - 🧠 **Churn Reduction**: Focus on product diversification in high churn cohorts.
    - 🔄 **Hybrid Forecasting**: Combine SARIMA + Prophet for better segment accuracy.
    - 🧩 **Anomaly Detection**: Add unsupervised anomaly models to flag repayment drops.
    """)
