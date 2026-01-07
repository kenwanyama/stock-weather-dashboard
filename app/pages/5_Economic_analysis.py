import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from economic_conditions import run_economic_analysis, economic_indicators_raw
from theme import apply_paper_theme

apply_paper_theme()

st.title('U.S. Economic Indicators in 2025')

st.markdown("""
<div style="font-size:0.95rem; color:#555; line-height:1.6;">
Economic indicators reveal how the U.S. economy is performing. In 2025, policy shifts, trade tensions, 
and a federal government shutdown created unusual patterns in inflation, employment, and spending.  
This dashboard tracks key indicators to show which sectors of the economy gained or slowed.
</div>
""", unsafe_allow_html=True)

st.divider()

st.info("""
**Data Note:** A 43-day government shutdown (Oct 1–Nov 12) disrupted Bureau of Labor Statistics surveys. October data is missing, 
and some November figures cover two months. Alternative estimates were used where possible.
""")

st.divider()

# ---- RUN ANALYSIS ----
figs = run_economic_analysis()
indicators = figs['columns']

st.subheader('Raw Indicator Performance')
st.markdown("Pick an indicator to see its monthly trend and how it moved through 2025.")
choice = st.selectbox('Select indicator:', indicators)
fig = economic_indicators_raw(figs['data'], choice)
st.pyplot(fig)

st.divider()

st.subheader('Normalized Performance')
st.markdown("All indicators are set to 100 at the start of 2025 for easy comparison.")
st.pyplot(figs['normalized'])

st.markdown("""
### Highlights

**Inflation:** CPI rose 2.7% in November, still above the Fed's 2% target, with core inflation at 2.6%. Tariffs continue to push costs higher.  

**Labor Market:** Unemployment reached 4.6%. Job creation slowed, with healthcare accounting for most gains and manufacturing struggling.  

**Wages:** Average hourly earnings rose 0.1% in November, up 3.5% year-over-year. Growth is slowing but remains positive.  

**The Fed:** The Fed cut rates three times in late 2025 to support growth while monitoring inflation. GDP growth is forecast around 1.9% for 2025.  

**Outlook:** Inflation is easing, the labor market is cooling, and spending continues moderately. The question remains whether the U.S. can achieve a soft landing in 2026.
""")

st.markdown("""
**Sources:** Bureau of Labor Statistics (CPI & Employment Nov 2025), Federal Reserve, Philadelphia Fed Survey Q4 2025, CNBC, NPR, Yahoo Finance
""")

