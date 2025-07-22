# FinSurf: Credit Risk & Customer Retention Analytics Platform

A robust end-to-end data analytics and machine learning project simulating real-world churn and credit risk modeling in the fintech domain.

---

## Project Summary

**Objective:**  
Predict customer churn and credit risk, uncover revenue leakage, and build actionable dashboards using ML + BI.

**Stack:**  
- Python (Pandas, Scikit-Learn, XGBoost, SHAP, Matplotlib)  
- Power BI  
- PostgreSQL (optional)  
- Excel  

**Project Goals:**
- Clean and preprocess financial lending datasets
- Engineer churn-relevant and credit-relevant KPIs
- Build ML models to predict churn
- Explain predictions using SHAP
- Integrate predictions into Power BI dashboards

---

## Directory Structure
FinSurf/
│
├── data/
│ └── raw/ # Original data
| └── exports/
| └── processed/
│
├── notebooks/
│ └── data_cleaning.ipynb # Cleaning + EDA
│ └── kpi_calculator.ipynb # KPI computation
│ └── churn_model_xgboost.ipynb # ML modeling + SHAP
│
├── outputs/
│ └── shap_summary_plot.png
│ └── shap_bar_plot.png
│ └── xgb_churn_predictions.csv
│
├── README.md
└── requirements.txt


---

## Phase 1: Data Cleaning & Feature Engineering

- Loaded LendingClub-style dataset with churn flags
- Dropped columns with >50% missing
- Cleaned tenure, income, rate columns
- Engineered:
  - `customer_tenure` (months)
  - `ARPU`, `CLTV`
  - Income bins, product segments (planned)

---

## Phase 2: KPI Development

Computed and validated:

| KPI   | Description |
|-------|-------------|
| PD    | Probability of Default |
| LGD   | Loss Given Default |
| ECL   | Expected Credit Loss |
| ARPU  | Avg. Revenue Per User |
| CLTV  | Customer Lifetime Value |

Tools: Pandas, SQL views, Seaborn

---

## Phase 3: Churn Prediction Modeling

- **Model Used:** XGBoost Classifier  
- **Train/Test Split:** 80/20, stratified on churn_flag  
- **Metrics:** Accuracy, Precision, Recall, ROC AUC  
- **Probability Outputs:** Yes  
- **Model Outputs Saved to CSV:** `xgb_churn_predictions.csv`

---

## Phase 4: SHAP Explainability

- Used `shap.TreeExplainer` to interpret model decisions
- Plots saved:
├── outputs/
├── shap_summary_plot.png
└── shap_bar_plot.png


<img src="outputs/shap_bar_plot.png" width="400"/>

- Key churn drivers: e.g., `tenure`, `CLTV`, `int_rate` (based on bar plot)

---

## Phase 5: Power BI Integration

- Predictions imported into Power BI  
- Visualizations:
- Churn Probability Distribution (Histogram)
- Total Predicted Customers (Card)
- Churned vs Retained Count (Bar)
- KPI Cards: Avg ARPU, CLTV by Churn Status

> Dataset used in Power BI: `outputs/xgb_churn_predictions.csv`

---

## Next Phases (In Progress)

## Phase 6: Clustering Model

- **Algorithm**: KMeans (k=4, selected via silhouette analysis)
- **Input Features**: `CLTV`, `Churn_Probability`, `ARPU`, `Risk_Score_Normalized`
- **Output**: `Segment_Label` assigned to each customer

---

### Segment Naming
- **Budget Loyalists**: High volume, low ARPU/CLTV, moderate churn
- **High-Value Champions**: Low churn, high ARPU and CLTV
- **At-Risk Value Drainers**: High churn, low value
- **Long-term Sleepers**: Low activity, low value, moderate churn

---

### Segment KPI Analysis
Visualizations created in **Power BI**:
- Bar plots and donut charts for:
  - Segment count distribution
  - Average CLTV by segment
  - Average ARPU by segment
  - Average Churn Probability by segment
  - Average Risk Score by segment
- Interactive **segment slicer** added to filter all charts
- Segment label integrated into core dataset

---

### Segment Strategy Matrix

| Segment               | Volume       | CLTV       | Churn Risk | Strategic Action                              |
|-----------------------|--------------|------------|------------|-----------------------------------------------|
| **Budget Loyalists**  |  Very Hig   h|    Low     |   Medium   | Upsell with bundles; reduce acquisition cost  |
| **High-Value Champions**  Medium     |  Very High |      Low   | Retain aggressively; offer loyalty programs   |
| **At-Risk Drainers**  |   Moderate   |    Low     |   Very High| Targeted win-back or churn mitigation offers  |
| **Long-term Sleepers**|    Low       |  Very Low  |    Medium  | Dormant — deprioritize or archive             |

---

### Deliverables
- `Segment_Label` added to dataset (`loan_kpi_df`)
- Power BI Dashboard with segment-level KPIs and filters
- PNG visualizations saved under `/plots/segmentation`
- Segment strategy table included in report and README
- Enhanced usability with **segment-aware dashboards**

---

### Business Impact
This segmentation allows the business to:
- Prioritize retention for high-CLTV, low-churn customers
- Implement targeted churn-prevention campaigns
- Upsell or cross-sell to budget-loyal segments
- Reduce resource spend on dormant customers
"""
- Phase 7: Time Series Forecasting (ARIMA/Prophet)
- Phase 8: A/B Simulation
- Phase 9: Streamlit Deployment (Optional)

---

## How to Run

1. Clone the repo:
 ```bash
 git clone https://github.com/yourusername/FinSurf.git
 cd FinSurf
 ```
---


### Star This Project

If you found this project insightful or useful, please consider giving it a ⭐ on GitHub! It helps others discover it and supports the creator.

---

### License

This project is licensed under the **MIT License**.
MIT License

Copyright (c) 2025 Mahasweta Roy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

---

### Contact
Created by Mahasweta Roy

📧 Email Mahasweta

🔗 Connect on LinkedIn

---




