import streamlit as st
from theme import apply_paper_theme


st.set_page_config(
    page_title="Stock Weather Dashboard",
    page_icon="📰",
    layout="centered"
)

apply_paper_theme()


# masthead
#------------------------------------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; padding:1.5rem 0; border-bottom:2px solid #111;">
        <h1 style="margin-bottom:0.2rem;">Stock Weather Dashboard</h1>
        <p style="margin:0; font-size:1.05rem; color:#444;">
            An educational dashboard exploring how markets behave across assets, regions, and economic cycles
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:0.9rem; color:#666; margin-top:0.5rem;'>"
    "Global Markets • Sectors • Commodities • Macro Signals"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

#lead story
#-----------------------------------------------------------------------------
st.markdown(
    """
    <h2 style="text-align:center;">Market Overview</h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p>
    Welcome to the Stock Weather Dashboard, this project is designed as an educational guide to understanding financial markets through a macro lens.
    The dashboard examines the broader
    structure of markets. how capital moves across regions, sectors, and asset classes, and what those movements
    reveal about risk, confidence, and economic expectations. Think of it as a your stock wrapped for 2025
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

#theme
#--------------------------------------------------------------------
st.markdown("<h2>Today’s Market Themes</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <ul>
        <li><b>Risk is being repriced</b>, not abandoned, capital is rotating rather than exiting markets entirely.</li>
        <li><b>Safe-haven assets are outperforming</b>, reflecting a market that’s playing it safe as policy uncertainty and tariff debates resurface.</li>
        <li><b>Regional and sector divergence</b> highlights uneven growth and differing economic exposures.</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.divider()


#Inside this edition
# ------------------------------------------------------------------------------
st.markdown("<h2>Inside This Edition</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <h3>🛢️ Commodities</h3>
        <p>
        Commodities often act as the market’s early-warning system. Movements in energy, metals,
        and agriculture reflect inflation pressures, supply disruptions, and shifts in global demand.
        </p>
        <p><i>Best used to understand inflation dynamics and uncertainty.</i></p>
        """,
        unsafe_allow_html=True
    )
    st.page_link("pages/2_Commodities_analysis.py", label="→ Read Commodities Analysis")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
        <h3>🌍 Regional Markets</h3>
        <p>
        Regional indices reveal how policy, currency movements, and trade exposure shape market outcomes
        across countries. Correlations rise during crises and fall during periods of rotation.
        </p>
        <p><i>Best used to assess global diversification and macro risk transmission.</i></p>
        """,
        unsafe_allow_html=True
    )
    st.page_link("pages/3_Region_analysis.py", label="→ Read Regional Markets")

with col2:
    st.markdown(
        """
        <h3>📊 Market Sectors</h3>
        <p>
        Sector performance shows where capital is flowing within equity markets. Leadership from growth
        sectors signals optimism, while defensive leadership points to caution.
        </p>
        <p><i>Best used to track investor sentiment and market leadership.</i></p>
        """,
        unsafe_allow_html=True
    )
    st.page_link("pages/4_Sector_analysis.py", label="→ Read Sector Analysis")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
        <h3>📉 Economic Conditions</h3>
        <p>
        Macroeconomic indicators provide the backdrop for market movements, capturing inflation trends,
        labor market strength, and monetary policy pressures.
        </p>
        <p><i>Best used to contextualize market behavior within the real economy.</i></p>
        """,
        unsafe_allow_html=True
    )
    st.page_link("pages/5_Economic_analysis.py", label="→ Read Economic Indicators")

st.divider()

#Editorial Takeaway..............................................................
st.markdown("<h2>Editorial Takeaway</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <p>
    Across commodities, sectors, and regions, a consistent narrative emerges:
    </p>

    <blockquote style="font-size:1.1rem; border-left:3px solid #111; padding-left:1rem; color:#333;">
    Markets are not in crisis — they are reassessing risk.
    </blockquote>
    """,
    unsafe_allow_html=True
)

st.divider()


#footer
# -----------------------------------------------------------
st.markdown(
    """
    <p style="font-size:0.85rem; color:#666;">
    This project is an analytical and educational tool. All analysis is descriptive and intended to
    study how markets and economic indicators evolve over the year.
    </p>
    """,
    unsafe_allow_html=True
)

