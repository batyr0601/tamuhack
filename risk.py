import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as dt
from scipy.stats import norm

def process_input(tickers, weights, weeks):
    yf.pdr_override()

    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.today()
    data = web.get_data_yahoo(tickers, start, end)['Close']

    tickers = np.array(tickers)
    weights = np.array(weights)

    return tickers, weights, data

def calculate_var(weights, data, weeks, initial_investment):
    returns = data.pct_change()

    avg_rets = returns.mean()

    print(returns)

    cov_matrix = returns.cov()

    port_mean = avg_rets.dot(weights)

    # Calculate portfolio standard deviation
    port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

    # Calculate mean of investment
    mean_investment = (1+port_mean) * initial_investment

    # Calculate standard deviation of investmnet
    stdev_investment = initial_investment * port_stdev

    returns.tail()

    conf_level1 = 0.05

    cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

    var_1d1 = initial_investment - cutoff1

    var_array = []
    num_days = int(7 * weeks)
    
    # print(num_days)

    for x in range(1, num_days+1):    
        var_array.append(np.round(var_1d1 * np.sqrt(x),2))
        # print(str(x) + " day VaR @ 95% confidence: " + str(np.round(var_1d1 * np.sqrt(x),2)))

    return var_array

def cvar(tickers, initial_investment, data, weights, weeks, alpha=0.95):
    var = calculate_var(weights, data, weeks, initial_investment)
    returns = data.fillna(0.0)
    portfolio_returns = np.array(returns.iloc[-7 * weeks:].dot(weights))

    # Get back to a return rather than an absolute loss
    var_pct_loss = var / initial_investment
    
    return initial_investment * np.nanmean(portfolio_returns[portfolio_returns < var_pct_loss])

def plot_var(var_array, years):
    plt.xlabel("Day #")
    plt.ylabel("Max portfolio loss (USD)")
    plt.title("Max portfolio loss (VaR) over 15-day period")
    plt.plot(var_array, "r")
    plt.show()


tickers = ['AAPL', 'MSFT', 'AMZN']
weights = [0.35, 0.35, 0.3]

tickers, weights, data = process_input(tickers, weights, 50)

var_array = calculate_var(weights, data, 50, 100000)



