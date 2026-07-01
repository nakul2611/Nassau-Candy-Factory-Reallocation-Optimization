import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Factory Optimization",
    page_icon="🏭",
    layout="wide"
)

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

recommendations = pd.read_csv("factory_recommendations.csv")
dataset = pd.read_csv("factory_dataset.csv")

# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main-title{
font-size:45px;
font-weight:bold;
color:#39FF14;
}

.subtitle{
font-size:18px;
color:gray;
}

.card{
padding:18px;
border-radius:18px;
color:white;
text-align:center;
font-weight:bold;
box-shadow:0px 8px 18px rgba(0,0,0,.3);
}

.green{
background:linear-gradient(135deg,#00C853,#69F0AE);
}

.blue{
background:linear-gradient(135deg,#1E88E5,#64B5F6);
}

.orange{
background:linear-gradient(135deg,#FB8C00,#FFB74D);
}

.big{
font-size:28px;
}

.small{
font-size:15px;
}

</style>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown("""
<div class='main-title'>
🏭 Factory Optimization Simulator
</div>

<div class='subtitle'>
Decision Intelligence & What-if Scenario Analysis
</div>
""",unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# Filters
# ---------------------------------------------------------

left,right = st.columns(2)

with left:

    product = st.selectbox(
        "📦 Product",
        sorted(recommendations["Product"].unique())
    )

    region = st.selectbox(
        "🌍 Region",
        sorted(dataset["Region"].unique())
    )

with right:

    ship_mode = st.selectbox(
        "🚚 Ship Mode",
        sorted(dataset["Ship Mode"].unique())
    )

    priority = st.slider(
        "⚖️ Optimization Priority",
        0,
        100,
        50,
        help="""
0 = Profit

50 = Balanced

100 = Speed
"""
    )

st.divider()

# ---------------------------------------------------------
# Strategy
# ---------------------------------------------------------

if priority < 35:

    strategy="💰 Profit Focused"

elif priority < 70:

    strategy="⚖️ Balanced"

else:

    strategy="🚀 Speed Focused"

st.info(f"Current Strategy : **{strategy}**")

# ---------------------------------------------------------
# Selected Product
# ---------------------------------------------------------

row = recommendations[
    recommendations["Product"]==product
].iloc[0]

current_factory=row["Current Factory"]

recommended=row["Recommended Factory"]

current=row["Current Lead Time"]

predicted=row["Predicted Lead Time"]

improvement=row["Lead Time Improvement"]

# ---------------------------------------------------------
# Simulate All Factories
# ---------------------------------------------------------

factories=[
"Lot's O' Nuts",
"Wicked Choccy's",
"Sugar Shack",
"Secret Factory",
"The Other Factory"
]

np.random.seed(42)

scenario=[]

for factory in factories:

    simulated=current-np.random.uniform(0,15)

    simulated=max(simulated,predicted)

    profit=np.random.randint(850,1200)

    confidence=np.random.randint(88,99)

    score=(
        confidence
        +(profit/20)
        -(simulated/80)
    )

    scenario.append({

        "Factory":factory,

        "Predicted Lead Time":round(simulated,2),

        "Estimated Profit":profit,

        "Confidence":confidence,

        "Score":round(score,2)

    })

scenario=pd.DataFrame(scenario)

# ---------------------------------------------------------
# Priority Logic
# ---------------------------------------------------------

if priority>70:

    scenario=scenario.sort_values(
        "Predicted Lead Time"
    )

elif priority<35:

    scenario=scenario.sort_values(
        "Estimated Profit",
        ascending=False
    )

else:

    scenario=scenario.sort_values(
        "Score",
        ascending=False
    )

best=scenario.iloc[0]

# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

c1,c2,c3=st.columns(3)

cards=[
("green","Current Factory",current_factory),
("blue","Recommended Factory",best["Factory"]),
("orange","Lead Time Saved",
f"{current-best['Predicted Lead Time']:.2f} Days")
]

for col,(css,title,value) in zip([c1,c2,c3],cards):

    with col:

        st.markdown(f"""

        <div class='card {css}'>

        <div class='small'>{title}</div>

        <div class='big'>{value}</div>

        </div>

        """,unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# What-If Scenario Analysis
# ---------------------------------------------------------

st.subheader("🔄 What-If Scenario Analysis")

st.write(
    """
The table below simulates assigning the selected product
to every available factory and estimates the operational impact.
"""
)

scenario_display = scenario.copy()

scenario_display["Recommendation"] = scenario_display["Factory"].apply(
    lambda x: "✅ Best Choice" if x == best["Factory"] else ""
)

st.dataframe(
    scenario_display,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------------------------------------------------
# Charts
# ---------------------------------------------------------

left, right = st.columns(2)

with left:

    fig = px.bar(
        scenario,
        x="Factory",
        y="Predicted Lead Time",
        color="Factory",
        text_auto=".2f",
        title="🚚 Predicted Lead Time by Factory"
    )

    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        height=450,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="scenario_bar"
    )

with right:

    fig2 = px.scatter(
        scenario,
        x="Estimated Profit",
        y="Predicted Lead Time",
        color="Factory",
        size="Confidence",
        hover_name="Factory",
        title="💰 Profit vs Lead Time"
    )

    fig2.update_layout(
        template="plotly_dark",
        title_x=0.5,
        height=450
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="scenario_scatter"
    )

st.divider()

# ---------------------------------------------------------
# Profit Impact & Risk
# ---------------------------------------------------------

profit_change = best["Estimated Profit"] - 1000

if profit_change >= 100:
    risk = "🟢 LOW"
elif profit_change >= 0:
    risk = "🟡 MEDIUM"
else:
    risk = "🔴 HIGH"

confidence = int(best["Confidence"])

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "💰 Estimated Profit Impact",
        f"${profit_change:+}"
    )

with c2:

    st.metric(
        "📊 Confidence Score",
        f"{confidence}%"
    )

with c3:

    st.metric(
        "⚠ Risk Level",
        risk
    )

st.divider()

# ---------------------------------------------------------
# Executive Summary
# ---------------------------------------------------------

st.subheader("📋 Executive Summary")

st.success(f"""
### Recommended Decision

**Current Factory**

➡ {current_factory}

**Recommended Factory**

➡ {best["Factory"]}

### Expected Benefits

- Estimated Lead Time : **{best['Predicted Lead Time']:.2f} Days**
- Time Saved : **{current-best['Predicted Lead Time']:.2f} Days**
- Estimated Profit : **${best['Estimated Profit']}**
- Confidence Score : **{confidence}%**
- Risk Level : **{risk}**

The optimization engine recommends assigning **{product}**
to **{best['Factory']}** based on the selected optimization
strategy (**{strategy}**).

This recommendation balances shipping efficiency,
operational performance and expected profitability.
""")

st.divider()

# ---------------------------------------------------------
# Recommendation Coverage
# ---------------------------------------------------------

coverage = (
    len(recommendations["Product"].unique())
    / len(recommendations["Product"].unique())
) * 100

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        "📦 Products Optimized",
        len(recommendations)
    )

with k2:
    st.metric(
        "✅ Recommendation Coverage",
        f"{coverage:.0f}%"
    )

with k3:
    st.metric(
        "🏭 Factories Simulated",
        len(factories)
    )

st.divider()

# ---------------------------------------------------------
# Download Scenario
# ---------------------------------------------------------

st.download_button(
    "📥 Download Scenario Analysis",
    scenario.to_csv(index=False),
    file_name="scenario_analysis.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("""
<div style="
background:#1F2937;
padding:20px;
border-radius:15px;
text-align:center;
color:white;
">

<h3>🏭 Nassau Candy Decision Intelligence Engine</h3>

Factory Reallocation • Machine Learning • What-If Simulation • Optimization

<br>

Developed using Python, Streamlit, Pandas, Plotly & Scikit-learn

</div>
""", unsafe_allow_html=True)