import streamlit as st
import os
from PIL import Image
import pandas as pd

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

df = pd.read_csv("factory_dataset.csv")

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.markdown("""
# 📊 Exploratory Data Analysis

### Explore the Nassau Candy Dataset through interactive statistics and visualizations.
""")

st.divider()

# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(
        "📦 Products",
        df["Product Name"].nunique()
    )

with col2:
    st.metric(
        "🏭 Factories",
        df["Factory"].nunique()
    )

with col3:
    st.metric(
        "🌍 Regions",
        df["Region"].nunique()
    )

with col4:
    st.metric(
        "💰 Total Sales",
        f"${df['Sales'].sum():,.0f}"
    )

with col5:
    st.metric(
        "💵 Gross Profit",
        f"${df['Gross Profit'].sum():,.0f}"
    )

with col6:
    st.metric(
        "⏱ Avg Lead Time",
        f"{df['Lead Time'].mean():.2f}"
    )

st.divider()

# ---------------------------------------------------------
# Filters
# ---------------------------------------------------------

st.subheader("🔍 Filter Dataset")

c1, c2, c3 = st.columns(3)

factory = c1.selectbox(
    "Factory",
    ["All"] + sorted(df["Factory"].unique().tolist())
)

division = c2.selectbox(
    "Division",
    ["All"] + sorted(df["Division"].unique().tolist())
)

region = c3.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

filtered = df.copy()

if factory != "All":
    filtered = filtered[
        filtered["Factory"] == factory
    ]

if division != "All":
    filtered = filtered[
        filtered["Division"] == division
    ]

if region != "All":
    filtered = filtered[
        filtered["Region"] == region
    ]

st.success(f"Showing {len(filtered)} records")

st.divider()

# ---------------------------------------------------------
# Download Dataset
# ---------------------------------------------------------

st.download_button(
    "📥 Download Filtered Dataset",
    filtered.to_csv(index=False),
    file_name="filtered_factory_dataset.csv",
    mime="text/csv"
)

st.divider()

# ---------------------------------------------------------
# EDA Images
# ---------------------------------------------------------

st.header("📈 Visualizations")

plots_folder = "plots"

if not os.path.exists(plots_folder):
    st.error("Plots folder not found!")
    st.stop()

images = sorted([
    file
    for file in os.listdir(plots_folder)
    if file.endswith(".png")
])

if not images:

    st.warning("No plots found.")

else:

    for img in images:

        title = img.replace(
            ".png",
            ""
        ).replace(
            "_",
            " "
        ).title()

        st.subheader(title)

        image = Image.open(
            os.path.join(
                plots_folder,
                img
            )
        )

        st.image(
            image,
            use_container_width=True
        )

        st.divider()

# ---------------------------------------------------------
# Dataset Preview
# ---------------------------------------------------------

with st.expander("📋 Dataset Preview"):

    st.dataframe(
        filtered,
        use_container_width=True
    )

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

st.subheader("📊 Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Rows",
        filtered.shape[0]
    )

with c2:
    st.metric(
        "Columns",
        filtered.shape[1]
    )

with c3:
    st.metric(
        "Missing Values",
        filtered.isnull().sum().sum()
    )

with c4:
    st.metric(
        "Duplicate Rows",
        filtered.duplicated().sum()
    )

st.divider()

# ---------------------------------------------------------
# Business Insights
# ---------------------------------------------------------

st.subheader("💡 Business Insights")

st.info(f"""
### 📌 Key Insights

- Highest Sales : **${filtered['Sales'].max():,.2f}**

- Average Sales : **${filtered['Sales'].mean():,.2f}**

- Average Lead Time : **{filtered['Lead Time'].mean():.2f} Days**

- Total Profit : **${filtered['Gross Profit'].sum():,.2f}**

- Factories Present : **{filtered['Factory'].nunique()}**

- Products Available : **{filtered['Product Name'].nunique()}**
""")

st.divider()

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("""
---
<div style="text-align:center">

## 🚀 Nassau Candy Data Analytics Dashboard

Built using **Python • Streamlit • Pandas • Machine Learning**

Developed by **Parth Vashishtha**

</div>
""", unsafe_allow_html=True)