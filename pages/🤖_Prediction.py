import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Lead Time Prediction",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🤖 Lead Time Prediction")
st.write("Predict shipping lead time using the trained Machine Learning model.")

st.divider()

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = joblib.load("models/best_model.pkl")
encoders = joblib.load("models/encoders.pkl")

df = pd.read_csv("factory_dataset.csv")

# ---------------------------------------------------
# Input Columns
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    factory = st.selectbox(
        "🏭 Factory",
        sorted(df["Factory"].unique())
    )

    product = st.selectbox(
        "📦 Product",
        sorted(df["Product Name"].unique())
    )

    division = st.selectbox(
        "📂 Division",
        sorted(df["Division"].unique())
    )

    region = st.selectbox(
        "🌍 Region",
        sorted(df["Region"].unique())
    )

with col2:

    ship_mode = st.selectbox(
        "🚚 Ship Mode",
        sorted(df["Ship Mode"].unique())
    )

    sales = st.number_input(
        "💰 Sales",
        min_value=0.0,
        value=10.0
    )

    units = st.number_input(
        "📦 Units",
        min_value=1,
        value=1
    )

    cost = st.number_input(
        "💵 Cost",
        min_value=0.0,
        value=5.0
    )

    gross_profit = st.number_input(
        "📈 Gross Profit",
        min_value=0.0,
        value=5.0
    )

st.divider()

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("🚀 Predict Lead Time", use_container_width=True):

    encoded = {}

    columns = [
        "Factory",
        "Product Name",
        "Division",
        "Region",
        "Ship Mode"
    ]

    values = [
        factory,
        product,
        division,
        region,
        ship_mode
    ]

    for col, value in zip(columns, values):
        encoder = encoders[col]
        encoded[col] = encoder.transform([str(value)])[0]

    input_df = pd.DataFrame([{

        "Factory": encoded["Factory"],
        "Product Name": encoded["Product Name"],
        "Division": encoded["Division"],
        "Region": encoded["Region"],
        "Ship Mode": encoded["Ship Mode"],
        "Sales": sales,
        "Units": units,
        "Cost": cost,
        "Gross Profit": gross_profit

    }])

    prediction = model.predict(input_df)[0]

    st.markdown("""
    <style>

    .prediction-card{
        background:linear-gradient(135deg,#11998e,#38ef7d);
        border-radius:20px;
        padding:35px;
        text-align:center;
        color:white;
        margin-top:30px;
        box-shadow:0px 10px 25px rgba(0,0,0,0.35);
    }

    .prediction-title{
        font-size:28px;
        font-weight:bold;
    }

    .prediction-value{
        font-size:58px;
        font-weight:bold;
        margin-top:15px;
        margin-bottom:15px;
    }

    .prediction-text{
        font-size:20px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
    f"""
<div class="prediction-card">
    <div class="prediction-title">🚚 Predicted Lead Time</div>
    <div class="prediction-value">{prediction:.2f} Days</div>
    <div class="prediction-text">
        ✅ Prediction generated successfully using the trained Machine Learning Model
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.divider()

# ---------------------------------------------------
# Information
# ---------------------------------------------------

st.info("""
### 💡 About this Prediction

The prediction is generated using the trained **Linear Regression Machine Learning model**.

The model considers the following features:

- 🏭 Factory
- 📦 Product
- 📂 Division
- 🌍 Region
- 🚚 Ship Mode
- 💰 Sales
- 📦 Units
- 💵 Cost
- 📈 Gross Profit

to estimate the expected shipping lead time.

The predicted value helps identify expected shipping performance before production begins.
""")