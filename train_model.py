# ==========================================================
# Nassau Candy Distributor
# Machine Learning Model Training
# ==========================================================

import os
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ----------------------------------------------------------
# Create Models Folder
# ----------------------------------------------------------

os.makedirs("models", exist_ok=True)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("factory_dataset.csv")

print("=" * 60)
print("Dataset Loaded Successfully")
print("=" * 60)

print(df.head())

# ----------------------------------------------------------
# Encode Categorical Columns
# ----------------------------------------------------------

categorical_columns = [
    "Ship Mode",
    "Country/Region",
    "State/Province",
    "Division",
    "Region",
    "Product Name",
    "Factory"
]

encoders = {}

for col in categorical_columns:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col].astype(str))

    encoders[col] = encoder

# Save encoders
joblib.dump(encoders, "models/encoders.pkl")

print("\nEncoders Saved Successfully.")

# ----------------------------------------------------------
# Features
# ----------------------------------------------------------

feature_columns = [

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

X = df[feature_columns]

# ----------------------------------------------------------
# Target
# ----------------------------------------------------------

y = df["Lead Time"]

# ----------------------------------------------------------
# Train Test Split
# ----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

# ----------------------------------------------------------
# Models
# ----------------------------------------------------------

models = {

    "Linear Regression":

        LinearRegression(),

    "Random Forest":

        RandomForestRegressor(

            n_estimators=300,

            random_state=42

        ),

    "Gradient Boosting":

        GradientBoostingRegressor(

            random_state=42

        )

}

best_model = None

best_r2 = float("-inf")

results = []

print("\nTraining Models...\n")

# ----------------------------------------------------------
# Train Models
# ----------------------------------------------------------

for name, model in models.items():

    print("=" * 60)

    print(name)

    model.fit(

        X_train,

        y_train

    )

    predictions = model.predict(

        X_test

    )

    mae = mean_absolute_error(

        y_test,

        predictions

    )

    rmse = mean_squared_error(

        y_test,

        predictions

    ) ** 0.5

    r2 = r2_score(

        y_test,

        predictions

    )

    print(f"MAE  : {mae:.4f}")

    print(f"RMSE : {rmse:.4f}")

    print(f"R²   : {r2:.4f}")

    results.append({

        "Model": name,

        "MAE": mae,

        "RMSE": rmse,

        "R2": r2

    })

    if r2 > best_r2:

        best_r2 = r2

        best_model = model

# ----------------------------------------------------------
# Save Best Model
# ----------------------------------------------------------

joblib.dump(

    best_model,

    "models/best_model.pkl"

)

print("\nBest Model Saved Successfully!")

# ----------------------------------------------------------
# Model Comparison
# ----------------------------------------------------------

results_df = pd.DataFrame(results)

print("\n")

print("=" * 60)

print("MODEL COMPARISON")

print("=" * 60)

print(results_df)

results_df.to_csv(

    "models/model_results.csv",

    index=False

)

print("\nModel Results Saved.")

print("\nCompleted Successfully!")
