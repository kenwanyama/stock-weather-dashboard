import yfinance as yf
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import streamlit as st

sector_ETFS = {
	'Technology':'XLK',
	'Energy':'XLE',
	'Financials':'XLF',
	'Healthcare': 'XLV',
	'Consumer Discretionary':'XLY',
	'Industrials':'XLI',
	'Utilities':'XLU',
	'Materials':'XLB',
	'Real Estate':'XLRE',
	'Communication':'XLC'
	}
	
@st.cache_data(show_spinner=False)
def get_sector_performance():
	end = "2025-12-31"
	start = "2025-01-01"

	data = {}
	for sector, ticker in sector_ETFS.items():
		df = yf.download(ticker, start=start, end=end, auto_adjust=True)
		df.columns = df.columns.droplevel(1)
		df['Sector'] = sector
		data[sector] = df
	return pd.concat(data)

@st.cache_data(show_spinner=False)
def prepare_data(data):
	close_price = data['Close'].unstack(level=0)

	return close_price.pct_change().dropna()

def cumulative_sector_performance(data):
	cumulative = (1 + data).cumprod() * 100

	for i in cumulative.columns:
		plt.plot(cumulative.index, cumulative[i], label=i)
	plt.title('Cumulative Sector Performance')
	plt.legend()
	plt.grid(True)
	

def volatility(data):
	volatility = data.std() * (252 ** 0.5)

	volatility.sort_values(ascending=False).plot(kind='bar', figsize=(12,6))
	plt.title('Annualized Volatility by Sector')
	plt.ylabel('Volatility')
	plt.grid(axis='y')
	

def trend_analysis(data, sector):
	sector_trend = data.loc[sector]
	sector_trend['MA30'] = sector_trend['Close'].rolling(30).mean()
	sector_trend['MA90'] = sector_trend['Close'].rolling(90).mean()

	plt.plot(sector_trend['Close'], label='Close', alpha=0.7)
	plt.plot(sector_trend['MA30'], label='30-Day MA', linestyle='--')
	plt.plot(sector_trend['MA90'], label='90-Day MA', linestyle='--')
	plt.title(f'{sector} Trend Analysis')
	plt.legend()
	plt.grid(True)
	



