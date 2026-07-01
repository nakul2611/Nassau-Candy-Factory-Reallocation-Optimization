# ==========================================================
# Nassau Candy Distributor Project
# Data Preprocessing
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("Nassau Candy Distributor.csv")

print("=" * 60)
print("Dataset Loaded Successfully")
print("=" * 60)

# ----------------------------------------------------------
# Basic Information
# ----------------------------------------------------------

print("\nFirst 5 Rows\n")
print(df.head())

print("\nShape of Dataset")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# ----------------------------------------------------------
# Duplicate Records
# ----------------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows : {duplicates}")

if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates Removed Successfully.")
else:
    print("No Duplicate Rows Found.")

# ----------------------------------------------------------
# Convert Date Columns
# ----------------------------------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# ----------------------------------------------------------
# Create Lead Time
# ----------------------------------------------------------

df["Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print("\nLead Time Statistics")
print(df["Lead Time"].describe())

# ----------------------------------------------------------
# Check for Negative Lead Time
# ----------------------------------------------------------

negative = df[df["Lead Time"] < 0]

print(f"\nNegative Lead Time Records : {len(negative)}")

# ----------------------------------------------------------
# Numerical Columns
# ----------------------------------------------------------

numerical_cols = [
    "Sales",
    "Units",
    "Gross Profit",
    "Cost",
    "Lead Time"
]

# ----------------------------------------------------------
# Boxplots
# ----------------------------------------------------------

for col in numerical_cols:

    plt.figure(figsize=(7,4))

    plt.boxplot(df[col])

    plt.title(f"{col} Outliers")

    plt.ylabel(col)

   

os.makedirs("plots", exist_ok=True)

plt.savefig(f"plots/{col}_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

# ----------------------------------------------------------
# Remove Extreme Outliers (IQR Method)
# ----------------------------------------------------------

clean_df = df.copy()

for col in numerical_cols:

    Q1 = clean_df[col].quantile(0.25)

    Q3 = clean_df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR

    upper = Q3 + 1.5 * IQR

    clean_df = clean_df[
        (clean_df[col] >= lower) &
        (clean_df[col] <= upper)
    ]

print("\nDataset Shape After Removing Outliers")
print(clean_df.shape)

# ----------------------------------------------------------
# Save Clean Dataset
# ----------------------------------------------------------

clean_df.to_csv(
    "cleaned_nassau_candy.csv",
    index=False
)

print("\nClean Dataset Saved Successfully!")

# ----------------------------------------------------------
# Final Information
# ----------------------------------------------------------

print("\nFinal Dataset Information")

print(clean_df.info())

print("\nFirst Five Rows")

print(clean_df.head())

print("\nCompleted Successfully!")