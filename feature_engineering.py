import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

os.makedirs("models", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("cleaned_nassau_candy.csv")

# Encode categorical columns
categorical_cols = [
    "Ship Mode",
    "Country/Region",
    "State/Province",
    "Division",
    "Region",
    "Product Name"
]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Save encoders
joblib.dump(encoders, "models/label_encoders.pkl")

# Save processed dataset
df.to_csv("processed_data.csv", index=False)

print("Feature Engineering Completed Successfully!")