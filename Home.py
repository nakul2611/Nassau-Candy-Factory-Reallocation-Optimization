import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="🍬",
    layout="wide"
)

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

df = pd.read_csv("factory_dataset.csv")
recommendation = pd.read_csv("factory_recommendations.csv")
model_results = pd.read_csv("models/model_results.csv")

# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main-title{
font-size:48px;
font-weight:bold;
color:#4CAF50;
}

.sub-title{
font-size:24px;
color:gray;
}

.kpi{
background-color:#1E1E1E;
padding:20px;
border-radius:12px;
text-align:center;
box-shadow:2px 2px 10px rgba(0,0,0,0.3);
}

</style>
""",unsafe_allow_html=True)

# ----------------------------------------------------
# Title
# ----------------------------------------------------

st.markdown(
"""
<div class='main-title'>
🍬 Nassau Candy Distributor
</div>

<div class='sub-title'>
AI Powered Factory Optimization Dashboard
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ----------------------------------------------------
# KPIs
# ----------------------------------------------------

avg_lead = df["Lead Time"].mean()

best_model = model_results.sort_values(
    by="R2",
    ascending=False
).iloc[0]["Model"]

st.markdown("""
<style>

.card{
padding:18px;
border-radius:18px;
text-align:center;
color:white;
font-weight:bold;
box-shadow:0px 6px 18px rgba(0,0,0,0.35);
}

.sales{
background:linear-gradient(135deg,#0F9D58,#34A853);
}

.profit{
background:linear-gradient(135deg,#1E88E5,#42A5F5);
}

.product{
background:linear-gradient(135deg,#F57C00,#FFA726);
}

.factory{
background:linear-gradient(135deg,#8E24AA,#BA68C8);
}

.lead{
background:linear-gradient(135deg,#D81B60,#EC407A);
}

.model{
background:linear-gradient(135deg,#546E7A,#78909C);
}

.big{
font-size:34px;
}

.small{
font-size:16px;
opacity:0.9;
}

</style>
""", unsafe_allow_html=True)

c1,c2,c3,c4,c5,c6 = st.columns([1.2,1.2,1,1,1,1.5])

cards = [
("sales","💰 Sales",f"${df['Sales'].sum()/1000:.1f}K"),
("profit","💵 Profit",f"${df['Gross Profit'].sum():,.0f}"),
("product","📦 Products",df["Product Name"].nunique()),
("factory","🏭 Factories",df["Factory"].nunique()),
("lead","⏱ Avg Lead",f"{avg_lead:.0f}"),
("model","🤖 Best Model",best_model)
]

for col,(css,title,value) in zip([c1,c2,c3,c4,c5,c6],cards):

    with col:

        st.markdown(f"""
        <div class="card {css}">
            <div class="small">{title}</div>
            <div class="big">{value}</div>
        </div>
        """,unsafe_allow_html=True)

st.divider()

# ----------------------------------------------------
# Charts
# ----------------------------------------------------

left,right=st.columns(2)

with left:

    sales=df.groupby("Division")["Sales"].sum().reset_index()

    fig=px.bar(
        sales,
        x="Division",
        y="Sales",
        color="Division",
        title="Sales by Division"
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    fig2=px.pie(
        df,
        names="Factory",
        title="Factory Distribution"
    )

    st.plotly_chart(fig2,use_container_width=True)

st.divider()

# ----------------------------------------------------
# Top Recommendations
# ----------------------------------------------------

st.subheader("🏆 Top Factory Recommendations")

top = recommendation.sort_values(
    by="Lead Time Improvement",
    ascending=False
)

st.dataframe(
    top.head(5),
    use_container_width=True
)

st.divider()

# ----------------------------------------------------
# Business Insights
# ----------------------------------------------------

st.subheader("💡 Business Insights")

col1,col2=st.columns(2)

with col1:

    st.success(
        f"""
Best ML Model

**{best_model.replace("Regression","Reg.")}**

Average Lead Time

**{avg_lead:.2f} Days**
"""
    )

with col2:

    best_factory=top.iloc[0]["Recommended Factory"]

    improvement=top["Lead Time Improvement"].mean()

    st.info(
        f"""
Most Recommended Factory

**{best_factory}**

Average Improvement

**{improvement:.2f} Days**
"""
    )

st.divider()

# ----------------------------------------------------
# Dataset Preview
# ----------------------------------------------------

with st.expander("📋 Dataset Preview"):

    st.dataframe(df.head())

# ----------------------------------------------------
# Footer
# ----------------------------------------------------
st.markdown("<br>",unsafe_allow_html=True)

st.markdown("""
<div style="
text-align:center;
padding:25px;
border-radius:15px;
background:#222831;
color:white;
">

<h3>🚀 Nassau Candy Factory Optimization Dashboard</h3>

Built using

Python • Streamlit • Plotly • Scikit-learn • Pandas

<br>


</div>
""",unsafe_allow_html=True)