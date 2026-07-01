# ==========================================================
# Nassau Candy Distributor
# ML Based Factory Optimization Engine
# ==========================================================

import joblib
import pandas as pd

# ----------------------------------------------------------
# Load Model & Encoders
# ----------------------------------------------------------

model = joblib.load("models/best_model.pkl")
encoders = joblib.load("models/encoders.pkl")

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("factory_dataset.csv")

# ----------------------------------------------------------
# Factory List
# ----------------------------------------------------------

factories = [
    "Lot's O' Nuts",
    "Wicked Choccy's",
    "Sugar Shack",
    "Secret Factory",
    "The Other Factory"
]

recommendations = []

# ----------------------------------------------------------
# Simulate Every Factory
# ----------------------------------------------------------

for product in df["Product Name"].unique():

    product_rows = df[df["Product Name"] == product]

    sample = product_rows.iloc[0].copy()

    current_factory = sample["Factory"]

    current_prediction = None

    best_prediction = float("inf")
    best_factory = current_factory

    for factory in factories:

        row = sample.copy()

        row["Factory"] = factory

        # Encode categorical values
        encoded = {}

        for column in [
            "Ship Mode",
            "Country/Region",
            "State/Province",
            "Division",
            "Region",
            "Product Name",
            "Factory"
        ]:

            encoder = encoders[column]

            try:
                encoded[column] = encoder.transform([str(row[column])])[0]
            except ValueError:
                encoded[column] = 0

        features = pd.DataFrame([{
            "Factory": encoded["Factory"],
            "Product Name": encoded["Product Name"],
            "Division": encoded["Division"],
            "Region": encoded["Region"],
            "Ship Mode": encoded["Ship Mode"],
            "Sales": row["Sales"],
            "Units": row["Units"],
            "Cost": row["Cost"],
            "Gross Profit": row["Gross Profit"]
        }])

        prediction = model.predict(features)[0]

        if factory == current_factory:
            current_prediction = prediction

        if prediction < best_prediction:
            best_prediction = prediction
            best_factory = factory

    improvement = current_prediction - best_prediction

    recommendations.append({
        "Product": product,
        "Current Factory": current_factory,
        "Recommended Factory": best_factory,
        "Current Lead Time": round(current_prediction, 2),
        "Predicted Lead Time": round(best_prediction, 2),
        "Lead Time Improvement": round(improvement, 2)
    })

# ----------------------------------------------------------
# Save Recommendations
# ----------------------------------------------------------

recommendation_df = pd.DataFrame(recommendations)

recommendation_df = recommendation_df.sort_values(
    by="Lead Time Improvement",
    ascending=False
)

recommendation_df.to_csv(
    "factory_recommendations.csv",
    index=False
)

print("\n==============================")
print("Optimization Completed!")
print("==============================\n")

print(recommendation_df)

print("\nRecommendations saved to factory_recommendations.csv")