import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Feature Importance",
    page_icon="⭐",
    layout="wide"
)

st.title("⭐ Feature Importance Analysis")

st.write("""
This dashboard explains which features have the greatest influence
on Lead Time prediction using the trained Gradient Boosting model.
""")

st.divider()

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv("factory_dataset.csv")

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load("models/best_model.pkl")

# ==========================================================
# Feature Names
# ==========================================================

features = [
    "Factory",
    "Product Name",
    "Division",
    "Region",
    "Ship Mode",
    "Sales",
    "Units",
    "Cost",
    "Gross Profit"
]

# ==========================================================
# Feature Importance
# ==========================================================

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

# ==========================================================
# KPI Cards
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Features",
        len(features)
    )

with col2:
    st.metric(
        "Most Important",
        importance_df.iloc[0]["Feature"]
    )

with col3:
    st.metric(
        "Importance",
        f"{importance_df.iloc[0]['Importance']:.3f}"
    )

st.divider()

# ==========================================================
# Horizontal Bar Chart
# ==========================================================

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    text="Importance",
    title="Feature Importance Ranking"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig.update_layout(
    height=600,
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# Pie Chart
# ==========================================================

pie = px.pie(
    importance_df,
    names="Feature",
    values="Importance",
    title="Contribution of Each Feature"
)

st.plotly_chart(
    pie,
    use_container_width=True
)

st.divider()

# ==========================================================
# Feature Importance Table
# ==========================================================

st.subheader("📋 Feature Importance Table")

table = importance_df.copy()

table["Importance"] = table["Importance"].round(4)

st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# Top Features
# ==========================================================

st.subheader("🏆 Top 3 Most Important Features")

top3 = importance_df.head(3)

for i, row in top3.iterrows():

    st.success(
        f"""
### {row['Feature']}

Importance Score : **{row['Importance']:.4f}**

This feature has a strong influence on shipping lead time prediction.
"""
    )

st.divider()

# ==========================================================
# Business Insights
# ==========================================================

st.subheader("💡 Business Insights")

st.info(f"""
The trained **Gradient Boosting Regressor** identified **{importance_df.iloc[0]['Feature']}**
as the most influential factor affecting Lead Time.

Understanding feature importance helps managers:

• Improve factory allocation

• Optimize shipping strategies

• Reduce operational delays

• Increase overall supply chain efficiency
""")

st.divider()

# ==========================================================
# Download
# ==========================================================

csv = importance_df.to_csv(index=False)

st.download_button(
    "📥 Download Feature Importance",
    csv,
    file_name="feature_importance.csv",
    mime="text/csv",
    use_container_width=True
)

st.success("✅ Feature importance analysis completed successfully.")