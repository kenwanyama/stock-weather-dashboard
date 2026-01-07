import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys, os

from theme import apply_paper_theme
apply_paper_theme()

# Allow imports from app root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sector_data import (
    get_sector_performance,
    prepare_data,
    cumulative_sector_performance,
    volatility,
    trend_analysis
)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Sector Performance Dashboard",
    layout="centered"
)

# ---- HEADER ----
st.markdown(
    """
    <div style="text-align:center; padding:1rem 0;">
        <h1 style="margin:0;">U.S. Sector Highlights in 2025</h1>
        <p style="margin:0; color:#555;">
            A snapshot of sector performance, trends, and market dynamics
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- LOAD DATA ----
raw_data = get_sector_performance()
data = prepare_data(raw_data)

# ---- INTRODUCTION ----
st.markdown(
    """
    <div style="font-size:0.95rem; color:#555; line-height:1.6;">
    2025 was a year of clear sector rotation in the U.S. Technology and Communication Services
    led the way, fueled by strong earnings and continued adoption of AI and digital solutions.
    Defensive areas like Utilities and Healthcare kept portfolios grounded amid interest rate
    changes and trade policy updates. The charts below show how different sectors performed,
    how much they fluctuated, and what trends emerged.  
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---- CUMULATIVE PERFORMANCE ----
st.markdown("<h2>Cumulative Sector Performance</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="font-size:0.95rem; color:#555; line-height:1.6;">
    Imagine investing $100 in each sector at the start of 2025. Technology and Communication Services
    would have led returns, reflecting strong earnings and growing demand for digital infrastructure.
    Energy and Materials trailed, impacted by softer oil prices and uneven industrial demand.
    </div>
    """,
    unsafe_allow_html=True
)

fig1 = plt.figure(figsize=(12, 6))
cumulative_sector_performance(data)
st.pyplot(fig1)

st.divider()

# ---- VOLATILITY ----
st.markdown("<h2>Sector Volatility (Annualized)</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="font-size:0.95rem; color:#555; line-height:1.6;">
    Volatility shows how much a sector’s value swings. High volatility can mean higher risk but also
    higher potential reward. In 2025, Technology and Consumer Discretionary had larger swings,
    while Utilities and Healthcare were steadier, offering defensive stability.
    </div>
    """,
    unsafe_allow_html=True
)

fig2 = plt.figure(figsize=(12, 6))
volatility(data)
st.pyplot(fig2)

st.divider()

# ---- TREND ANALYSIS ----
st.markdown("<h2>Sector Trend Analysis</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="font-size:0.95rem; color:#555; line-height:1.6;">
    Moving averages help highlight trends by smoothing out daily fluctuations. When a short-term
    average moves above a long-term average, momentum is strengthening. In 2025, growth-oriented
    sectors generally showed upward trends, while Energy, Materials, and Real Estate showed
    flatter or weaker patterns.
    </div>
    """,
    unsafe_allow_html=True
)

sector_choice = st.selectbox(
    "Select a sector to examine its trend:",
    raw_data.index.get_level_values(0).unique().tolist()
)

fig3 = plt.figure(figsize=(12, 6))
trend_analysis(raw_data, sector_choice)
st.pyplot(fig3)

st.divider()

# ---- KEY TAKEAWAYS ----
st.markdown("<h2>Key Takeaways</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="font-size:0.95rem; color:#555; line-height:1.6;">

    <b>1. Growth Leaders:</b> Technology and Communication Services drove market returns in 2025,
    supported by strong earnings and adoption of AI and digital solutions.

    <br><br><b>2. Defensive Anchors:</b> Utilities and Healthcare provided steadier returns, helping
    balance portfolios amid interest rate changes and trade uncertainty.

    <br><br><b>3. Volatility Matters:</b> High-volatility sectors offered both opportunity and risk,
    while low-volatility sectors helped stabilize returns.

    <br><br><b>4. Trend Signals:</b> Moving averages show growth sectors sustaining upward momentum,
    while lagging sectors flattened or weakened. Understanding these trends helps investors
    anticipate where capital is flowing.

    <br><br><b>Sources:</b> S&P 500 sector performance reports (2025), Yahoo Finance, CBOE sector
    volatility indices, Bloomberg, Federal Reserve market reports
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

