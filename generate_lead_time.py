import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.read_csv("factory_dataset.csv")

# -------------------------------
# Factory Delay
# -------------------------------

factory_delay = {
    "Lot's O' Nuts": 2,
    "Wicked Choccy's": 3,
    "Sugar Shack": 4,
    "Secret Factory": 5,
    "The Other Factory": 6
}

# -------------------------------
# Ship Mode Delay
# -------------------------------

ship_delay = {
    "Same Day": 1,
    "First Class": 2,
    "Second Class": 4,
    "Standard Class": 6
}

# -------------------------------
# Region Delay
# -------------------------------

region_delay = {
    "Interior": 2,
    "Atlantic": 3,
    "Gulf": 4,
    "Pacific": 5
}

lead_time = []

for _, row in df.iterrows():

    base = 5

    factory = factory_delay[row["Factory"]]

    ship = ship_delay[row["Ship Mode"]]

    region = region_delay[row["Region"]]

    units = row["Units"] * 0.20

    sales = row["Sales"] * 0.02

    noise = np.random.normal(0,0.5)

    days = (
        base
        + factory
        + ship
        + region
        + units
        + sales
        + noise
    )

    lead_time.append(round(days,2))

df["Lead Time"] = lead_time

df.to_csv("factory_dataset.csv",index=False)

print("Lead Time regenerated successfully!")