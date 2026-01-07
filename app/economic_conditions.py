from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime as dt
from dotenv import load_dotenv
import streamlit as st

# Indicators mapping----------------------------------------------------------------
indicators = {
    "CPI (Inflation)": "CPIAUCSL",
    "Core CPI": "CPILFESL",
    "Unemployment Rate": "UNRATE",
    "Fed Funds Rate": "FEDFUNDS",
    "GDP (US)": "GDP",
    "PCE (Consumption)": "PCE",
    "10-Year Treasury Yield": "DGS10",
    "Industrial Production": "INDPRO",
    "Retail Sales": "RSXFS"
}

# Fetch economic snapshot from FRED, restricted to 2025, cached--------------------------------
@st.cache_data(show_spinner=False)
def get_economic_snapshot():
    load_dotenv()
    fred = Fred(api_key=os.getenv('FRED_API_KEY'))
    data = pd.DataFrame()

    start = dt.date(2025, 1, 1)
    end = dt.date(2025, 12, 31)

    for name, series_id in indicators.items():
        series = fred.get_series(series_id)
        series = series.loc[start:end]  # only 2025
        data[name] = series

    data.index = pd.to_datetime(data.index)
    return data

# Plot raw indicator time series----------------------------------------------------------------
def economic_indicators_raw(data, indicator):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(data.index, data[indicator], color='tab:blue')
    ax.set_title(f'{indicator} - 2025')
    ax.set_xlabel('Date')
    ax.set_ylabel(indicator)
    ax.grid(True)
    return fig

# Plot normalized indicator comparison--------------------------------------------------------
def economic_indicators_normalized(data):
    normalized_data = data / data.iloc[0] * 100

    fig, ax = plt.subplots(figsize=(14, 7))
    for col in normalized_data.columns:
        ax.plot(normalized_data.index, normalized_data[col], label=col)
    ax.set_title('Normalized Economic Indicators (Indexed to 100, 2025)')
    ax.legend(loc='upper left')
    ax.grid(True)
    return fig

# Run analysis and return raw + normalized data------------------------------------------------
def run_economic_analysis():
    data = get_economic_snapshot()
    data_columns = data.columns.tolist()
    normalized = economic_indicators_normalized(data)
    return {
        'data': data,
        'columns': data_columns,
        'normalized': normalized
    }

