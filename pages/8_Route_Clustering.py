import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Route Clustering",
    page_icon="🛣️",
    layout="wide"
)

st.title("🛣️ Route Performance Clustering")

st.write("""
This dashboard groups shipping routes based on operational performance
using Machine Learning (K-Means Clustering). It helps identify
high-performing and low-performing shipping routes.
""")

st.divider()

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv("factory_dataset.csv")

# ==========================================================
# Features for Clustering
# ==========================================================

features = [
    "Sales",
    "Gross Profit",
    "Lead Time",
    "Units",
    "Cost"
]

X = df[features]

# ==========================================================
# Scale Features
# ==========================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ==========================================================
# K-Means Clustering
# ==========================================================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

cluster_names = {
    0: "High Performance",
    1: "Medium Performance",
    2: "Low Performance"
}

df["Cluster Name"] = df["Cluster"].map(cluster_names)

# ==========================================================
# KPI Cards
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Routes",
        len(df)
    )

with col2:
    st.metric(
        "Factories",
        df["Factory"].nunique()
    )

with col3:
    st.metric(
        "Regions",
        df["Region"].nunique()
    )

with col4:
    st.metric(
        "Average Lead Time",
        f"{df['Lead Time'].mean():.2f} Days"
    )

st.divider()

# ==========================================================
# Interactive Scatter Plot
# ==========================================================

fig = px.scatter(
    df,
    x="Sales",
    y="Lead Time",
    color="Cluster Name",
    size="Gross Profit",
    hover_name="Product Name",
    hover_data=[
        "Factory",
        "Region",
        "Units"
    ],
    title="Shipping Route Clusters"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# Cluster Summary
# ==========================================================

summary = (
    df.groupby("Cluster Name")
    .agg(
        Routes=("Cluster Name", "count"),
        Avg_Sales=("Sales", "mean"),
        Avg_Lead_Time=("Lead Time", "mean"),
        Avg_Profit=("Gross Profit", "mean")
    )
    .reset_index()
)

summary = summary.round(2)

st.subheader("📋 Cluster Summary")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# Cluster Distribution
# ==========================================================

pie = px.pie(
    summary,
    names="Cluster Name",
    values="Routes",
    title="Route Cluster Distribution"
)

st.plotly_chart(
    pie,
    use_container_width=True
)

st.divider()

# ==========================================================
# Average Lead Time by Cluster
# ==========================================================

bar = px.bar(
    summary,
    x="Cluster Name",
    y="Avg_Lead_Time",
    color="Cluster Name",
    text="Avg_Lead_Time",
    title="Average Lead Time by Cluster"
)

bar.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    bar,
    use_container_width=True
)

st.divider()

# ==========================================================
# Detailed Routes
# ==========================================================

st.subheader("📦 Route Details")

st.dataframe(
    df[
        [
            "Factory",
            "Product Name",
            "Region",
            "Sales",
            "Gross Profit",
            "Lead Time",
            "Cluster Name"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# Download
# ==========================================================

st.download_button(
    "📥 Download Clustered Dataset",
    data=df.to_csv(index=False),
    file_name="route_clusters.csv",
    mime="text/csv"
)

st.success(
    """
✅ Machine Learning clustering completed successfully.

Routes have been grouped into High, Medium, and Low Performance clusters
based on Sales, Gross Profit, Lead Time, Units, and Cost.
"""
)