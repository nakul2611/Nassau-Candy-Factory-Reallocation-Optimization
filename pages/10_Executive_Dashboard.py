import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")

st.write("""
Executive Summary for the Factory Reallocation &
Shipping Optimization Recommendation System.
""")

st.divider()

# ==========================================================
# Load Data
# ==========================================================

df = pd.read_csv("factory_dataset.csv")
recommendations = pd.read_csv("factory_recommendations.csv")
models = pd.read_csv("models/model_results.csv")

best_model = models.sort_values(
    by="R2",
    ascending=False
).iloc[0]

# ==========================================================
# KPI Cards
# ==========================================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Orders",
        len(df)
    )

with c2:
    st.metric(
        "Products",
        df["Product Name"].nunique()
    )

with c3:
    st.metric(
        "Factories",
        df["Factory"].nunique()
    )

with c4:
    st.metric(
        "Regions",
        df["Region"].nunique()
    )

st.divider()

# ==========================================================
# Business KPI
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric(
        "Total Sales",
        f"${df['Sales'].sum():,.0f}"
    )

with k2:
    st.metric(
        "Gross Profit",
        f"${df['Gross Profit'].sum():,.0f}"
    )

with k3:
    st.metric(
        "Average Lead Time",
        f"{df['Lead Time'].mean():.2f} Days"
    )

with k4:
    st.metric(
        "Best ML Model",
        best_model["Model"]
    )

st.divider()

# ==========================================================
# Sales by Factory
# ==========================================================

sales = (
    df.groupby("Factory")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    sales,
    x="Factory",
    y="Sales",
    color="Factory",
    title="Sales by Factory",
    text="Sales"
)

fig.update_traces(
    texttemplate="%{text:.0f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# Profit Distribution
# ==========================================================

profit = (
    df.groupby("Factory")["Gross Profit"]
    .sum()
    .reset_index()
)

pie = px.pie(
    profit,
    names="Factory",
    values="Gross Profit",
    title="Gross Profit Distribution"
)

st.plotly_chart(
    pie,
    use_container_width=True
)

st.divider()

# ==========================================================
# Recommendation Summary
# ==========================================================

st.subheader("🏭 Factory Recommendation Summary")

top = recommendations.sort_values(
    by="Lead Time Improvement",
    ascending=False
)

st.dataframe(
    top.head(10),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# Executive Insights
# ==========================================================

best_factory = (
    df.groupby("Factory")["Gross Profit"]
    .sum()
    .idxmax()
)

best_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

st.success(f"""
### 📌 Executive Insights

✅ Best Performing Factory:
**{best_factory}**

✅ Highest Revenue Region:
**{best_region}**

✅ Best Machine Learning Model:
**{best_model['Model']}**

✅ Model Accuracy (R²):
**{best_model['R2']:.4f}**

✅ Average Lead Time:
**{df['Lead Time'].mean():.2f} Days**

The optimization system recommends reallocating products
to improve shipping efficiency while maintaining profitability.
""")

st.divider()

# ==========================================================
# Download Reports
# ==========================================================

col1,col2 = st.columns(2)

with col1:

    st.download_button(
        "📥 Download Recommendations",
        recommendations.to_csv(index=False),
        "factory_recommendations.csv",
        "text/csv",
        use_container_width=True
    )

with col2:

    st.download_button(
        "📥 Download Model Results",
        models.to_csv(index=False),
        "model_results.csv",
        "text/csv",
        use_container_width=True
    )

st.divider()

# ==========================================================
# Footer
# ==========================================================

st.markdown("""
---
### 📄 Project Summary

**Project Title**

Factory Reallocation & Shipping Optimization Recommendation System
for Nassau Candy Distributor

**Developed Using**

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- Machine Learning
- K-Means Clustering

**Models Used**

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

This system predicts shipping lead time, recommends
factory reallocation strategies, performs scenario
analysis and provides executive-level insights to
improve logistics efficiency.
""")