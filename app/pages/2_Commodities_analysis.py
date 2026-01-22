import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
from theme import apply_paper_theme

# Apply the newspaper/paper theme
apply_paper_theme()

plt.switch_backend("Agg")

# Path adjustment so Streamlit can import commodities module
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
sys.path.append(app_dir)

from commodities import (
    get_commodities,
    compute_summary,
    commodity_correlation,
    plot_price,
    plot_normalized,
    plot_moving_averages,
    commodities
)

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Commodity Market Dashboard",
    layout="centered"
)

# ---- HEADER ----
st.markdown(
    """
    <div style='text-align:center; padding:1rem 0;'>
        <h1 style='margin:0; font-family:Times New Roman, serif;'>Commodity Market Analysis Dashboard</h1>
        <p style='margin:0; font-size:1.1rem; color:#555555;'>Tracking major global commodities over the past 12 months</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- INTRODUCTION ----
st.markdown(
    """
    <div style='padding:1rem; font-size:1rem; line-height:1.6;'>
    Commodities sit at the center of the global economy. They power factories, shape food prices, and often react first to shifts in growth, inflation, and geopolitics.

In 2025, commodity markets have reflected a world adjusting to tighter financial conditions, uneven global growth, and renewed trade and policy uncertainty. Tracking these price movements offers a useful lens into how investors and producers are responding to changing economic realities.

This dashboard follows key commodities across energy, metals, and agriculture to highlight emerging trends and the forces shaping them.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- LOAD DATA ----
data = get_commodities()

# ---- PERFORMANCE SUMMARY ----
st.markdown("<h2>Performance Summary</h2>", unsafe_allow_html=True)
summary = compute_summary(data)
st.dataframe(summary, use_container_width=True)
st.markdown(
    """
    <div style='padding:0.5rem 0; color:#555555; font-size:0.95rem;'>
    A snapshot of how each commodity has performed across different timeframes, along with volatility and recent trend direction.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- CORRELATION HEATMAP ----
st.markdown("<h2>Correlation Heatmap</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='padding:0.5rem 0; color:#555555; font-size:0.95rem;'>
    Commodity prices often move together when driven by shared forces such as global growth expectations, inflation trends, or currency movements. This heatmap shows where prices tend to align and where they diverge, offering insight into diversification and cross market dynamics.
    </div>
    """,
    unsafe_allow_html=True
)

# Compute correlation
pivoted = data.reset_index().pivot(index="Date", columns="Name", values="Close")
corr = pivoted.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

fig = plt.figure(figsize=(12, 8))
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.7,
    mask=mask,
    cbar_kws={"shrink": 0.8}
)
plt.title("Commodity Correlation Heatmap")
st.pyplot(fig)

st.divider()

# ---- NORMALIZED COMMODITY COMPARISON ----
st.markdown("<h2>Normalized Commodity Comparison (Indexed to 100)</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='padding:0.5rem 0; color:#555555; font-size:0.95rem;'>
    By indexing all prices to 100 at the start of 2025, this chart focuses on relative performance rather than absolute price levels. It makes it easier to see which commodities have led or lagged as market conditions evolved.
    </div>
    """,
    unsafe_allow_html=True
)

fig = plt.figure(figsize=(12, 6))
norm = pivoted / pivoted.iloc[0] * 100

plt.gca().set_prop_cycle(None)
for name in commodities.keys():
    plt.plot(norm.index, norm[name], label=name)

plt.title("Normalized Commodity Prices (Indexed to 100)")
plt.grid(True)
plt.legend()
st.pyplot(fig)

st.markdown(
    """
    <div style='padding:0.5rem 0; font-size:0.95rem; line-height:1.6; color:#555555;'>
    <b>The Safe-Haven Trade:</b> Gold and silver have been the standout performers in 2025, reflecting classic 
    safe-haven behavior during times of uncertainty.<br><br>
    <b>Energy Under Pressure:</b> Crude oil and Brent crude have faced headwinds, declining sharply over the period.<br><br>
    <b>Agriculture and Industrial Metals:</b> Corn, wheat, and copper show mixed performance due to weather, trade, and infrastructure spending.<br><br>
    <b>The Dollar's Influence:</b> USD fluctuations play a role but broader risk sentiment and supply-demand fundamentals are dominant.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- KEY TAKEAWAYS ----
st.markdown("<h2>Key Takeaways</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='padding:0.5rem 0; font-size:0.95rem; line-height:1.6; color:#555555;'>
    Commodity markets in 2025 reflect a cautious and uneven global environment.
    Strength in precious metals points to defensive positioning, while weakness in energy and mixed performance elsewhere suggest uncertainty around growth and demand.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    "<p style='font-size:14px; color:#444; margin-top:2rem;'>"
    "<strong>Sources:</strong> World Bank Commodity Markets Outlook, International Energy Agency (IEA), U.S. Energy Information Administration (EIA), "
    "Federal Reserve Economic Data (FRED), Bloomberg and Reuters market coverage"
    "</p>",
    unsafe_allow_html=True
)

