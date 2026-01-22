import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import streamlit as st

# Commodity tickers----------------------------------------------------------------
commodities = {
    'Gold': 'GC=F',
    'Crude oil (WTI)': 'CL=F',
    'Brent oil': 'BZ=F',
    'Natural Gas': 'NG=F',
    'Silver': 'SI=F',
    'Copper': 'HG=F',
    'Corn': 'ZC=F',
    'Wheat': 'ZW=F',
    'Bitcoin': 'BTC-USD',
    'USD Dollar Index': 'DX-Y.NYB'
}

# Fetch commodity data from yfinance (only 2025), cached--------------------------------
@st.cache_data(show_spinner=False)
def get_commodities():
    start = dt.date(2025, 1, 1)
    end = dt.date(2025, 12, 31)

    data = {}
    for name, ticker in commodities.items():
        df = yf.download(ticker, start=start, end=end, auto_adjust=True)
        df.columns = df.columns.droplevel(1) if isinstance(df.columns, pd.MultiIndex) else df.columns
        df['Ticker'] = ticker
        df['Name'] = name
        data[name] = df
    return pd.concat(data)

# Compute returns, volatility, and trend------------------------------------------------
def compute_summary(data):
    summary = []

    for name in commodities.keys():
        df = data.loc[name]
        df['Return'] = df['Close'].pct_change()

        one_year = df['Close'].iloc[-1] / df['Close'].iloc[0] - 1
        one_month = df['Close'].pct_change(21).iloc[-1]
        three_month = df['Close'].pct_change(63).iloc[-1]
        six_month = df['Close'].pct_change(126).iloc[-1]

        volatility = df['Return'].std() * np.sqrt(252)

        df['MA50'] = df['Close'].rolling(50).mean()
        df['MA200'] = df['Close'].rolling(200).mean()
        trend = "Uptrend" if df['MA50'].iloc[-1] > df['MA200'].iloc[-1] else "Downtrend"

        summary.append([
            name,
            f"{one_month:.2%}",
            f"{three_month:.2%}",
            f"{six_month:.2%}",
            f"{one_year:.2%}",
            f"{volatility:.2%}",
            trend
        ])

    columns = ["Commodity", "1M Return", "3M Return", "6M Return", "1Y Return", "Volatility", "Trend"]
    return pd.DataFrame(summary, columns=columns)

# Commodity correlation heatmap---------------------------------------------------------
def commodity_correlation(data, figsize=(12, 8)):
    pivoted = data.reset_index().pivot(index="Date", columns="Name", values="Close")
    corr = pivoted.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=figsize)
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=.7,
        mask=mask,
        cbar_kws={"shrink": .8}
    )
    plt.title("Commodity Correlation Heatmap (2025)")
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()
    return corr

# Price charts---------------------------------------------------------------------------
def plot_price(data):
    for name in commodities.keys():
        df = data.loc[name]
        plt.figure(figsize=(12, 5))
        plt.plot(df.index, df['Close'])
        plt.title(f"{name} - Price Chart (2025)")
        plt.ylabel("Price")
        plt.grid(True)
        plt.show()

# Normalized price comparison-----------------------------------------------------------
def plot_normalized(data):
    pivoted = data.reset_index().pivot(index="Date", columns="Name", values="Close")
    norm = (pivoted / pivoted.apply(lambda x: x.dropna().iloc[0])) * 100

    plt.figure(figsize=(12, 6))
    for name in commodities.keys():
        plt.plot(norm.index, norm[name], label=name)
    plt.title("Normalized Comparison (Indexed to 100, 2025)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Moving averages / trend signals-------------------------------------------------------
def plot_moving_averages(data):
    for name in commodities.keys():
        df = data.loc[name]
        df['MA50'] = df['Close'].rolling(50).mean()
        df['MA200'] = df['Close'].rolling(200).mean()

        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['Close'], label="Close Price")
        plt.plot(df.index, df['MA50'], label="50-day MA")
        plt.plot(df.index, df['MA200'], label="200-day MA")
        plt.tit

