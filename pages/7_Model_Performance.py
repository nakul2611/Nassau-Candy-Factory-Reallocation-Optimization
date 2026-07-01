import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning Model Performance")

st.write(
    "Comparison of all Machine Learning models used for lead time prediction."
)

st.divider()

# --------------------------------------------------
# Load Results
# --------------------------------------------------

results = pd.read_csv("models/model_results.csv")

best_model = results.sort_values(
    "R2",
    ascending=False
).iloc[0]

st.subheader("🏆 Best Model")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Best Model",
        best_model["Model"]
    )

with col2:
    st.metric(
        "MAE",
        f"{best_model['MAE']:.4f}"
    )

with col3:
    st.metric(
        "RMSE",
        f"{best_model['RMSE']:.4f}"
    )

with col4:
    st.metric(
        "R² Score",
        f"{best_model['R2']:.4f}"
    )

st.divider()
# ============================================================
# Model Comparison Table
# ============================================================

st.subheader("📋 Model Comparison")

display_df = results.copy()

display_df["MAE"] = display_df["MAE"].round(4)
display_df["RMSE"] = display_df["RMSE"].round(4)
display_df["R2"] = display_df["R2"].round(4)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ============================================================
# Interactive Bar Chart
# ============================================================

st.subheader("📊 Model Performance Comparison")

import plotly.express as px

fig = px.bar(
    display_df,
    x="Model",
    y="R2",
    color="Model",
    text="R2",
    title="R² Score Comparison"
)

fig.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)

fig.update_layout(
    xaxis_title="Machine Learning Model",
    yaxis_title="R² Score",
    showlegend=False,
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ============================================================
# MAE Comparison
# ============================================================

fig2 = px.bar(
    display_df,
    x="Model",
    y="MAE",
    color="Model",
    text="MAE",
    title="Mean Absolute Error Comparison"
)

fig2.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)

fig2.update_layout(
    xaxis_title="Machine Learning Model",
    yaxis_title="MAE",
    showlegend=False,
    height=500
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ============================================================
# RMSE Comparison
# ============================================================

fig3 = px.bar(
    display_df,
    x="Model",
    y="RMSE",
    color="Model",
    text="RMSE",
    title="Root Mean Squared Error Comparison"
)

fig3.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)

fig3.update_layout(
    xaxis_title="Machine Learning Model",
    yaxis_title="RMSE",
    showlegend=False,
    height=500
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# ============================================================
# Best Model Highlight
# ============================================================

st.success(
    f"""
### 🏆 Best Performing Model

**{best_model['Model']}**

✅ R² Score : **{best_model['R2']:.4f}**

✅ RMSE : **{best_model['RMSE']:.4f}**

✅ MAE : **{best_model['MAE']:.4f}**

This model achieved the highest predictive performance and is selected as the production model for the Factory Reallocation & Shipping Optimization Recommendation System.
"""
)

st.divider()

# ============================================================
# Download CSV
# ============================================================

csv = display_df.to_csv(index=False)

st.download_button(
    "📥 Download Model Results",
    data=csv,
    file_name="model_results.csv",
    mime="text/csv"
)