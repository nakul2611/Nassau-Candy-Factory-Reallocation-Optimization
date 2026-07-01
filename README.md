# 🍬 Nassau Candy Factory Reallocation & Shipping Optimization Recommendation System

An AI-powered Decision Intelligence system that predicts shipping lead time, recommends optimal factory allocation, and improves logistics efficiency for Nassau Candy Distributor.

---

## 📌 Project Overview

Traditional factory allocation methods use static business rules that often result in:

- High shipping lead times
- Increased logistics costs
- Lower operational efficiency
- Reduced profitability

This project combines Machine Learning with Factory Optimization to recommend better factory assignments while balancing speed and profit.

---

## 🎯 Objectives

- Predict shipping lead time using Machine Learning
- Simulate multiple factory assignment scenarios
- Recommend the optimal factory for each product
- Improve operational efficiency
- Minimize shipping delays
- Maximize profitability

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib

---

## 🤖 Machine Learning Models

The following regression models were trained and evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Evaluation Metrics:

- MAE
- RMSE
- R² Score

Best Performing Model:

**Gradient Boosting Regressor**

---

## 📊 Dashboard Features

### 🏠 Home Dashboard

- Sales KPIs
- Profit KPIs
- Product Overview
- Factory Distribution
- Sales by Division

---

### 📈 Model Performance

- Model Comparison
- MAE
- RMSE
- R² Score
- Interactive Charts
- Download Model Results

---

### 🛣 Route Clustering

- K-Means Route Clustering
- Regional Performance Analysis
- Cluster Visualization

---

### 📌 Feature Importance

- Feature Ranking
- Importance Visualization
- Model Interpretation

---

### 📋 Executive Dashboard

- Business KPIs
- Factory Summary
- Sales Analysis
- Executive Insights

---

### 🏭 Factory Optimization Simulator

- Product Selection
- Region Selection
- Ship Mode Selection
- Optimization Priority Slider
- Current Factory
- Recommended Factory
- Lead Time Improvement

---

### 🔄 What-If Scenario Analysis

- Factory Simulation
- Lead Time Prediction
- Profit Estimation
- Confidence Score
- Risk Analysis
- Executive Recommendation

---

### 🗺 Factory Map

- Factory Locations
- Geographic Visualization

---

### 🔮 Prediction Page

Predict lead time using trained Machine Learning models.

---

### 📊 Exploratory Data Analysis (EDA)

Includes visualizations for:

- Sales Distribution
- Monthly Sales
- Profit Distribution
- Regional Sales
- Division Analysis
- Heatmaps
- Lead Time Analysis
- Product Analysis

---

## 📂 Project Structure

```
DataAnalytic/
│
├── Home.py
├── train_model.py
├── preprocessing.py
├── feature_engineering.py
├── optimization.py
├── generate_lead_time.py
│
├── models/
│   ├── best_model.pkl
│   ├── encoders.pkl
│   └── model_results.csv
│
├── pages/
│   ├── Model_Performance.py
│   ├── Route_Clustering.py
│   ├── Feature_Importance.py
│   ├── Executive_Dashboard.py
│   ├── Optimization.py
│   ├── Recommendations.py
│   ├── Prediction.py
│   ├── Factory_Map.py
│   ├── EDA.py
│   └── About.py
│
├── plots/
│
├── processed_data.csv
├── factory_dataset.csv
├── factory_recommendations.csv
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/nakul2611/Nassau-Candy-Factory-Reallocation-Optimization.git
```

Go inside the project

```bash
cd Nassau-Candy-Factory-Reallocation-Optimization
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run Home.py
```

or

```bash
py -m streamlit run Home.py
```

---

## 📈 Dataset

The dataset contains information such as:

- Orders
- Products
- Factories
- Sales
- Cost
- Gross Profit
- Region
- Ship Mode
- Lead Time

---

## 📊 Business Benefits

- Faster deliveries
- Reduced shipping delays
- Better factory utilization
- Higher operational efficiency
- Data-driven decision making
- Improved profitability

---

## 📷 Dashboard Preview

The dashboard includes:

- Interactive Charts
- KPI Cards
- Factory Optimization Simulator
- Recommendation Engine
- Scenario Analysis
- Machine Learning Insights
- Executive Dashboard

---

## 📄 Future Improvements

- Real-time optimization
- Live shipment tracking
- Weather integration
- Demand forecasting
- Deep Learning models
- Cloud deployment
- API integration

---

## 👨‍💻 Author

**Nakul Vashishtha**

GitHub:
https://github.com/nakul2611

---

## 📜 License

This project is developed for educational and research purposes under the Unified Mentor Data Analytics Internship.
