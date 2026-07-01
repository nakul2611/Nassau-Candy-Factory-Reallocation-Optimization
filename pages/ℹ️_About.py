import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("""
# Nassau Candy Distributor Factory Optimization

## Problem Statement

Nassau Candy currently assigns products to factories using static rules.
This project applies Machine Learning to recommend improved factory assignments
that reduce shipping lead time while maintaining profitability.

---

## Objectives

- Predict shipping lead time
- Recommend optimal factory assignments
- Compare current vs recommended factories
- Support what-if analysis
- Improve operational efficiency

---

## Machine Learning Models

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

---

## Technologies

- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly
- Folium

---

## Dashboard Modules

- Home Dashboard
- Exploratory Data Analysis
- Lead Time Prediction
- Factory Optimization
- Recommendations
- Factory Map

---

## Future Scope

- Real-time logistics integration
- GPS route optimization
- Live shipment tracking
- Cost optimization using Linear Programming
- Cloud deployment (AWS / Azure)

---

## Developed By

B.Tech CSE (Cloud Computing & Automation)

Nassau Candy Distributor ML Optimization Project
""")