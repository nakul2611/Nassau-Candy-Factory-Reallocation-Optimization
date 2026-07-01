import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Factory Map",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Nassau Candy Factory Locations")

st.write("Interactive map showing all manufacturing factories.")

# -------------------------------------------------------
# Factory Coordinates
# -------------------------------------------------------

factories = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.119140, -96.181150),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.117500, -89.971107)
}

# -------------------------------------------------------
# Create Map
# -------------------------------------------------------

m = folium.Map(
    location=[39.5, -98.35],   # Center of USA
    zoom_start=4
)

# -------------------------------------------------------
# Add Markers
# -------------------------------------------------------

for name, (lat, lon) in factories.items():

    folium.Marker(
        location=[lat, lon],
        popup=f"<b>{name}</b>",
        tooltip=name,
        icon=folium.Icon(color="blue", icon="industry", prefix="fa")
    ).add_to(m)

# -------------------------------------------------------
# Display Map
# -------------------------------------------------------

st_folium(
    m,
    width=1200,
    height=600
)

st.success("Showing all factory locations.")