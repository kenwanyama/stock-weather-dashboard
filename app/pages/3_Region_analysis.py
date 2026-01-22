import streamlit as st
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from region_data import run_region_analysis
from theme import apply_paper_theme

# Theme
apply_paper_theme()

st.set_page_config(
    page_title="Regional Markets | Stock Weather",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Masthead
st.markdown(
    "<h1 style='text-align:center; font-family: Georgia, Times New Roman, serif;'>"
    "Regional Market Performance"
    "</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-style:italic; color:#333;'>"
    "Tracking seven major equity markets across the global economy throughout 2025"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# Intro
st.markdown("""
Global equity markets are connected. Trade, capital flows, currency moves, and geopolitical decisions link regions together and can amplify shocks or accelerate recoveries.

Here we will look at major stock indices across the United States, Europe, the United Kingdom, Japan, China, India, and The Emerging Markets. The aim is to show how policy moves, currency swings, and regional economic fundamentals shaped market outcomes over 2025.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Data
figs = run_region_analysis()

# Normalized Perfomance
st.markdown("## Normalized Market Performance")

st.markdown("""
To make comparisons fair, all indices are normalized to 100 at the start of 2025. This highlights relative performance across regions rather than absolute index levels.
""")

st.pyplot(figs["normalized"])

st.markdown("""
### Market Commentary

**The April “Liberation Day” Shock**  
In early April 2025, global markets dropped sharply after sweeping tariffs were announced in the United States. Over six trillion dollars in value was lost across two trading days, showing how policy shocks can ripple across the globe.

**Japan’s Relative Resilience**  
Japan held up well despite a 25% tariff on automobiles and parts. Corporate earnings were strong, business confidence rose, and investment in semiconductors and AI provided a solid foundation for the market.

**Emerging Markets Outperformance**  
Emerging markets stood out in 2025. The MSCI Emerging Markets Index rose over 30% by October, helped by a weaker U.S. dollar which lowered debt costs and drew capital flows into higher-yielding economies.

**The Dollar Effect**  
Dollar trends played a key role. A softer dollar boosted risk appetite beyond U.S. equities, supporting growth in regions sensitive to currency fluctuations.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Volatility
st.markdown("## Annualized Volatility by Region")

st.markdown("""
Volatility measures the magnitude of price swings within each market. Higher volatility reflects greater uncertainty
and sensitivity to shocks, while lower volatility suggests relative stability.
""")

st.pyplot(figs["volatility"])

st.markdown("""
In 2025, Japan had the highest annualized volatility among major markets, reflecting sharper swings despite strong fundamentals. The April tariff shock affected nearly all regions at once, producing synchronized drawdowns across the globe. Even markets that eventually recovered quickly experienced heightened short-term swings.

These patterns show that even stable economies are not immune to sudden policy shocks and highlight the importance of monitoring risk as well as returns.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Correlation
st.markdown("## Cross-Market Correlations")

st.markdown("""
Correlation measures how closely markets move together. High correlations indicate synchronized movements,
while lower correlations suggest diversification potential.
""")

st.pyplot(figs["correlation"])

st.markdown("""
During periods of global stress, correlations tend to rise as investors react simultaneously to systemic risks.
The April 2025 sell-off was no exception. However, structural differences—such as monetary policy frameworks,
trade exposure, and sector composition—continue to create meaningful divergence across regions.
""")

st.markdown("<hr>", unsafe_allow_html=True)

#Takeaways
st.markdown("## Key Takeaways")

st.markdown("""
2025 highlighted the value of regional diversification. A U.S.-originating policy shock quickly affected global markets, but recovery paths varied.

Japan’s manufacturing strength, the currency-driven rally in emerging markets, and broad resilience in risk appetite show that market leadership can shift quickly when macro conditions change.

""")

st.markdown(
    "<p style='font-size:14px; color:#444; margin-top:2rem;'>"
    "<strong>Sources:</strong> Wikipedia (2025 stock market crash), Nikkei Asia, AllianceBernstein, "
    "VT Markets, Yahoo Finance, Cambridge Associates, S&P Global Japan Manufacturing PMI"
    "</p>",
    unsafe_allow_html=True
)

