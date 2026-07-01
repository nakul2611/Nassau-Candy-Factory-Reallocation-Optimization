import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Recommendations",
    page_icon="📈",
    layout="wide"
)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv("factory_recommendations.csv")

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.card{
    padding:18px;
    border-radius:18px;
    text-align:center;
    color:white;
    font-weight:bold;
    box-shadow:0px 8px 20px rgba(0,0,0,0.35);
}

.green{
background:linear-gradient(135deg,#00C853,#64DD17);
}

.blue{
background:linear-gradient(135deg,#1E88E5,#42A5F5);
}

.orange{
background:linear-gradient(135deg,#FB8C00,#FFA726);
}

.purple{
background:linear-gradient(135deg,#8E24AA,#BA68C8);
}

.big{
font-size:34px;
font-weight:bold;
}

.small{
font-size:16px;
opacity:.9;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown("""
<h1 style='text-align:center;color:#39FF14'>
📈 Factory Recommendation Dashboard
</h1>

<h4 style='text-align:center;color:gray'>
AI Generated Product Reallocation Recommendations
</h4>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

products = len(df)

avg_improvement = df["Lead Time Improvement"].mean()

max_improvement = df["Lead Time Improvement"].max()

best_factory = (
    df["Recommended Factory"]
    .value_counts()
    .idxmax()
)

c1,c2,c3,c4 = st.columns(4)

cards=[
("green","📦 Products",products),
("blue","📈 Avg Improvement",f"{avg_improvement:.2f} Days"),
("orange","🚀 Maximum",f"{max_improvement:.2f} Days"),
("purple","🏭 Best Factory",best_factory)
]

for col,(css,title,value) in zip([c1,c2,c3,c4],cards):

    with col:

        st.markdown(f"""
        <div class="card {css}">
        <div class="small">{title}</div>
        <div class="big">{value}</div>
        </div>
        """,unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# Search + Sort
# ---------------------------------------------------

left,right=st.columns([2,1])

with left:

    search=st.text_input(
        "🔍 Search Product"
    )

with right:

    sort_option=st.selectbox(
        "Sort By",
        [
            "Lead Time Improvement",
            "Current Lead Time",
            "Predicted Lead Time"
        ]
    )

filtered=df.copy()

if search:

    filtered=filtered[
        filtered["Product"].str.contains(
            search,
            case=False
        )
    ]

filtered=filtered.sort_values(
    by=sort_option,
    ascending=False
)

# ---------------------------------------------------
# Download
# ---------------------------------------------------

st.download_button(
    "📥 Download Recommendation Report",
    filtered.to_csv(index=False),
    file_name="factory_recommendations.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()
# ---------------------------------------------------
# Recommendation Table
# ---------------------------------------------------

st.subheader("📋 Factory Recommendations")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------------------------------------------
# Charts
# ---------------------------------------------------

left,right=st.columns(2)

with left:

    top10 = filtered.head(10)

    fig = px.bar(
        top10,
        x="Product",
        y="Lead Time Improvement",
        color="Recommended Factory",
        text_auto=".2f",
        title="🏆 Top Lead Time Improvements"
    )

    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        height=500,
        legend_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="recommendation_bar"
    )

with right:

    factory_counts = (
        filtered["Recommended Factory"]
        .value_counts()
        .reset_index()
    )

    factory_counts.columns = [
        "Factory",
        "Recommendations"
    ]

    pie = px.pie(
        factory_counts,
        names="Factory",
        values="Recommendations",
        hole=0.55,
        title="🏭 Recommended Factory Distribution"
    )

    pie.update_layout(
        template="plotly_dark",
        title_x=0.5,
        height=500
    )

    st.plotly_chart(
        pie,
        use_container_width=True,
        key="recommendation_pie"
    )

st.divider()

# ---------------------------------------------------
# Business Insights
# ---------------------------------------------------

st.subheader("💡 Business Insights")

best_product = filtered.iloc[0]["Product"]

best_factory = filtered.iloc[0]["Recommended Factory"]

best_gain = filtered.iloc[0]["Lead Time Improvement"]

col1,col2 = st.columns(2)

with col1:

    st.markdown(f"""
    <div style="
    background:#145A32;
    padding:25px;
    border-radius:15px;
    color:white;
    ">

    <h3>🏆 Highest Improvement</h3>

    <h2>{best_product}</h2>

    <p>
    Expected Lead Time Improvement
    </p>

    <h2>{best_gain:.2f} Days</h2>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div style="
    background:#154360;
    padding:25px;
    border-radius:15px;
    color:white;
    ">

    <h3>🏭 Most Recommended Factory</h3>

    <h2>{best_factory}</h2>

    <p>
    Frequently selected by the optimization engine.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------

st.success(
    f"""
### 📌 Recommendation Summary

- Products Analysed: **{products}**
- Average Improvement: **{avg_improvement:.2f} Days**
- Maximum Improvement: **{max_improvement:.2f} Days**
- Recommended Factory Most Often: **{best_factory}**

The recommendation engine evaluates every product and identifies
factory assignments that are expected to reduce shipping lead time.
"""
)

st.divider()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("""
<div style="
text-align:center;
padding:20px;
background:#1F2937;
border-radius:15px;
color:white;
">

<h3>🚀 Nassau Candy Recommendation Engine</h3>

Machine Learning • Optimization • Streamlit Dashboard

</div>
""", unsafe_allow_html=True)