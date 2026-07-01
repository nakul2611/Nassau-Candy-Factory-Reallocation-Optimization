# ==========================================================
# Nassau Candy Distributor Project
# Exploratory Data Analysis (EDA)
# ==========================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Create plots folder
# ----------------------------------------------------------

os.makedirs("plots", exist_ok=True)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("cleaned_nassau_candy.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create Month Column
df["Month"] = df["Order Date"].dt.strftime("%b")

sns.set_style("whitegrid")

# ==========================================================
# 1 Sales Distribution
# ==========================================================

plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=30, kde=True)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("plots/01_sales_distribution.png")
plt.close()

# ==========================================================
# 2 Sales by Region
# ==========================================================

plt.figure(figsize=(8,5))
sns.barplot(
    x=df.groupby("Region")["Sales"].sum().index,
    y=df.groupby("Region")["Sales"].sum().values
)
plt.title("Sales by Region")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("plots/02_sales_by_region.png")
plt.close()

# ==========================================================
# 3 Sales by Division
# ==========================================================

plt.figure(figsize=(7,5))
sns.barplot(
    x=df.groupby("Division")["Sales"].sum().index,
    y=df.groupby("Division")["Sales"].sum().values
)
plt.title("Sales by Division")
plt.tight_layout()
plt.savefig("plots/03_sales_by_division.png")
plt.close()

# ==========================================================
# 4 Ship Mode Distribution
# ==========================================================

plt.figure(figsize=(7,5))
df["Ship Mode"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Ship Mode Distribution")
plt.tight_layout()
plt.savefig("plots/04_ship_mode_distribution.png")
plt.close()

# ==========================================================
# 5 Monthly Sales Trend
# ==========================================================

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("plots/05_monthly_sales.png")
plt.close()

# ==========================================================
# 6 Gross Profit Distribution
# ==========================================================

plt.figure(figsize=(8,5))
sns.histplot(df["Gross Profit"], bins=30, kde=True)
plt.title("Gross Profit Distribution")
plt.tight_layout()
plt.savefig("plots/06_profit_distribution.png")
plt.close()

# ==========================================================
# 7 Top 10 Products
# ==========================================================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.tight_layout()
plt.savefig("plots/07_top_products.png")
plt.close()

# ==========================================================
# 8 Top 10 States
# ==========================================================

top_states = df.groupby("State/Province")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_states.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.tight_layout()
plt.savefig("plots/08_top_states.png")
plt.close()

# ==========================================================
# 9 Correlation Heatmap
# ==========================================================

plt.figure(figsize=(8,6))

corr = df[[
    "Sales",
    "Units",
    "Gross Profit",
    "Cost",
    "Lead Time"
]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("plots/09_heatmap.png")

plt.close()

# ==========================================================
# 10 Sales vs Gross Profit
# ==========================================================

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Gross Profit"
)

plt.title("Sales vs Gross Profit")

plt.tight_layout()

plt.savefig("plots/10_sales_profit.png")

plt.close()

# ==========================================================
# 11 Units Distribution
# ==========================================================

plt.figure(figsize=(8,5))

sns.histplot(df["Units"], bins=30)

plt.title("Units Distribution")

plt.tight_layout()

plt.savefig("plots/11_units_distribution.png")

plt.close()

# ==========================================================
# 12 Lead Time Distribution
# ==========================================================

plt.figure(figsize=(8,5))

sns.histplot(df["Lead Time"], bins=30)

plt.title("Lead Time Distribution")

plt.tight_layout()

plt.savefig("plots/12_leadtime_distribution.png")

plt.close()

# ==========================================================
# 13 Region-wise Profit
# ==========================================================

plt.figure(figsize=(8,5))

sns.barplot(
    x=df.groupby("Region")["Gross Profit"].sum().index,
    y=df.groupby("Region")["Gross Profit"].sum().values
)

plt.xticks(rotation=30)

plt.title("Region-wise Profit")

plt.tight_layout()

plt.savefig("plots/13_region_profit.png")

plt.close()

# ==========================================================
# 14 Division-wise Profit
# ==========================================================

plt.figure(figsize=(7,5))

sns.barplot(
    x=df.groupby("Division")["Gross Profit"].sum().index,
    y=df.groupby("Division")["Gross Profit"].sum().values
)

plt.title("Division-wise Profit")

plt.tight_layout()

plt.savefig("plots/14_division_profit.png")

plt.close()

# ==========================================================
# 15 Product Count
# ==========================================================

plt.figure(figsize=(7,5))

df["Division"].value_counts().plot(kind="bar")

plt.title("Number of Products by Division")

plt.tight_layout()

plt.savefig("plots/15_product_count.png")

plt.close()

print("="*60)
print("EDA Completed Successfully!")
print("15 Charts Saved Inside 'plots' Folder")
print("="*60)