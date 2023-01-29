import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as dt
from scipy.stats import norm

yf.pdr_override()

tickers = ['AAPL', 'AMZN', 'GOOG', 'MSFT']

# pull data from yahoo finance for the tickers array
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2022, 1, 1)
data = web.get_data_yahoo(tickers, start, end)['Close']

weights = np.array([.25, .03, .37, .35])

# Set an initial investment level
initial_investment = 1000000

# Download closing prices
data = web.get_data_yahoo(tickers, start=start, end=end)['Close']

#From the closing prices, calculate periodic returns
returns = data.pct_change()

avg_rets = returns.mean()

cov_matrix = returns.cov()
cov_matrix

port_mean = avg_rets.dot(weights)

# Calculate portfolio standard deviation
port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

# Calculate mean of investment
mean_investment = (1+port_mean) * initial_investment

# Calculate standard deviation of investmnet
stdev_investment = initial_investment * port_stdev

returns.tail()

conf_level1 = 0.1

cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

var_1d1 = initial_investment - cutoff1
var_1d1

var_array = []
num_days = int(265)

for x in range(1, num_days+1):    
    var_array.append(np.round(var_1d1 * np.sqrt(x),2))
    print(str(x) + " day VaR @ 95% confidence: " + str(np.round(var_1d1 * np.sqrt(x),2)))

# Build plot
plt.xlabel("Day #")
plt.ylabel("Max portfolio loss (USD)")
plt.title("Max portfolio loss (VaR) over 15-day period")
plt.plot(var_array, "r")
