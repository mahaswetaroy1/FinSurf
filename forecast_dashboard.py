import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# --------------- Utility Functions ---------------
def load_data(actual_path, forecast_path, value_col):
    try:
        df_actual = pd.read_csv(actual_path)
        df_forecast = pd.read_csv(forecast_path)

        # Ensure datetime index
        df_actual["Month"] = pd.to_datetime(df_actual["Month"])
        df_forecast["Month"] = pd.to_datetime(df_forecast["Month"])

        return df_actual, df_forecast
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None


def plot_forecast(df_actual, df_forecast, value_col, title):
    df_merged = pd.merge(df_actual, df_forecast, on="Month", how="outer")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_merged["Month"], df_merged[f"{value_col}_actual"], label="Actual", marker='o')
    ax.plot(df_merged["Month"], df_merged[f"{value_col}_forecast"], label="Forecast", marker='x')

    if f"{value_col}_lower" in df_merged.columns and f"{value_col}_upper" in df_merged.columns:
        ax.fill_between(df_merged["Month"],
                        df_merged[f"{value_col}_lower"],
                        df_merged[f"{value_col}_upper"],
                        color='orange', alpha=0.3, label="Confidence Interval")

    ax.set_title(title)
    ax.set_xlabel("Month")
    ax.set_ylabel(value_col.replace("_", " "))
    ax.legend()
    st.pyplot(fig)


# --------------- Main App Logic ------------------

st.set_page_config(page_title="Forecast Overlay Dashboard", layout="wide")

st.title("📊 Forecast Overlay Dashboard")
st.caption("Compare actuals vs forecast (Prophet + SARIMA) for repayment, churn, and segment performance.")

# Left Sidebar View Selector
view = st.sidebar.selectbox("🔍 Select Dashboard View", [
    "Total Repayment",
    "Churn Risk Forecast",
    "Segment-Level Forecasts",
    "Recommendations"
])

# -------- View: Total Repayment Forecast --------
if view == "Total Repayment":
    st.header("Total Repayment Forecast")
    df_actual, df_forecast = load_data(
        "actuals/actual_total_repayment.csv",
        "forecasts/sarima_forecast_results.csv",
        "Repayment"
    )
    if df_actual is not None and df_forecast is not None:
        plot_forecast(df_actual, df_forecast, value_col="Repayment", title="Total Repayment: Actual vs Forecast")

# -------- View: Churn Risk Forecast --------
elif view == "Churn Risk Forecast":
    st.header("Churn Risk Forecast")
    df_actual, df_forecast = load_data(
        "actuals/actual_churn_rate.csv",
        "forecasts/forecast_churn_risk.csv",
        "Churn_Rate"
    )
    if df_actual is not None and df_forecast is not None:
        plot_forecast(df_actual, df_forecast, value_col="Churn_Rate", title="Churn Risk: Actual vs Forecast")

# -------- View: Segment-Level Forecasts --------
elif view == "Segment-Level Forecasts":
    st.header("Segment-Level Loan Volume Forecasts")
    segment = st.selectbox("Select Segment", ["At-Risk Value Drainers", "Long-term Sleepers"])
    actual_path = f"actuals/actual_segment_{segment}.csv"
    forecast_path = f"forecasts/forecast_segment_{segment}.csv"

    df_actual, df_forecast = load_data(actual_path, forecast_path, "Loan_Volume")
    if df_actual is not None and df_forecast is not None:
        plot_forecast(df_actual, df_forecast, value_col="Loan_Volume", title=f"{segment}: Actual vs Forecast")

# -------- View: Recommendations --------
elif view == "Recommendations":
    st.header("📌 Business Recommendations")
    st.markdown("""
    - 📈 **Total Repayment Surge**: Investigate post-2015 spike in repayment activity.
    - 🔍 **Segment Monitoring**: Long-term Sleepers show volatile patterns – recommend closer monitoring.
    - 🧠 **Churn Reduction**: Focus on product diversification in high churn cohorts.
    - 🔄 **Hybrid Forecasting**: Combine SARIMA + Prophet for better segment accuracy.
    - 🧩 **Anomaly Detection**: Add unsupervised anomaly models to flag repayment drops.
    """)

