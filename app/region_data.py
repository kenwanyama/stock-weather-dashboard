import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Regional market tickers----------------------------------------------------------------
regional_INDEXES = {
    "US (S&P 500)": "^GSPC",
    "Europe (STOXX 600)": "^STOXX",
    "UK (FTSE 100)": "^FTSE",
    "Japan (Nikkei 225)": "^N225",
    "China (Shanghai)": "000001.SS",
    "India (Nifty 50)": "^NSEI",
    "Emerging Markets (EEM)": "EEM"
}

# Fetch regional market data (2025 only), cached------------------------------------------------
@st.cache_data(show_spinner=False)
def get_region_performance():
    start = dt.date(2025, 1, 1)
    end = dt.date(2025, 12, 31)

    data = {}
    for region, symbol in regional_INDEXES.items():
        df = yf.download(symbol, start=start, end=end, auto_adjust=True)
        df.columns = df.columns.droplevel(1) if isinstance(df.columns, pd.MultiIndex) else df.columns
        df['Region'] = region
        data[region] = df
    return pd.concat(data)

# Prepare close price data for analysis-------------------------------------------------------
def prepare_data(data):
    close_prices = data['Close'].unstack(level=0)
    close_prices = close_prices.ffill().bfill()
    return close_prices

# Normalized cumulative performance----------------------------------------------------------
def normalized_performance(data):
    returns = data.pct_change().dropna()
    cumulative_returns = (1 + returns).cumprod() * 100

    fig, ax = plt.subplots(figsize=(12, 6))
    for col in cumulative_returns.columns:
        ax.plot(cumulative_returns.index, cumulative_returns[col], label=col)
    ax.set_title('Regional Market Performance (Normalized, 2025)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Performance Index (Indexed to 100)')
    ax.legend()
    ax.grid(True)
    return fig

# Annualized volatility-----------------------------------------------------------------------
def annualized_volatility(data):
    returns = data.pct_change().dropna()
    volatility = returns.std() * np.sqrt(252)
    volatility.sort_values(ascending=False, inplace=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    volatility.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Annualized Volatility by Region (2025)')
    ax.set_ylabel('Volatility (Std Dev)')
    ax.grid(axis='y')
    return fig

# Correlation heatmap--------------------------------------------------------------------------
def correlation_matrix(data):
    returns = data.pct_change().dropna()
    corr_matrix = returns.corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', mask=mask, ax=ax)
    ax.set_title('Correlation Between Regional Markets (2025)')
    return fig

# Trading volume chart--------------------------------------------------------------------------
def trading_volume(data, region):
    region_data = data.xs(region)
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(region_data.index, region_data['Volume'])
    ax.set_title(f"{region} Trading Volume (2025)")
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    return fig

# Price trend with moving averages-------------------------------------------------------------
def price_trends(data, region):
    region_data = data[region]
    df = pd.DataFrame({'Close': region_data})
    df['MA30'] = df['Close'].rolling(30).mean()
    df['MA90'] = df['Close'].rolling(90).mean()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['Close'], label='Close', alpha=0.8)
    ax.plot(df.index, df['MA30'], label='30-Day MA', linestyle='--')
    ax.plot(df.index, df['MA90'], label='90-Day MA', linestyle='--')
    ax.set_title(f'{region} - Price Trend with Moving Averages (2025)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.grid(True)
    return fig

# Run full regional analysis------------------------------------------------------------------
def run_region_analysis():
    data = get_region_performance()
    close_data = prepare_data(data)

    normalized = normalized_performance(close_data)
    volatility = annualized_volatility(close_data)
    corr_matrix = correlation_matrix(close_data)

    return {
        'data': data,
        'close': close_data,
        'normalized': normalized,
        'volatility': volatility,
        'correlation': corr_matrix
    }

