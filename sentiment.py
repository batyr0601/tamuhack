import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import webscraper
import metrics
import risk
import json
import requests

sid = SentimentIntensityAnalyzer()

keywords = ["economy", "gdp", "growth", "gain", "loss"]
link = "https://seekingalpha.com/market-outlook/economy?page="

scraper = webscraper.Scraper(keywords, link)
titles = scraper.getTitles(10)

average = []

for header in titles:
    average.append(sid.polarity_scores(header)['compound'] + 1)

total = 0

sentiment = (sum(average) / len(average)) - 1

# print(sentiment)
# print(scraper.getEconStats())
# print(metrics.get_from_last_month())

econStats = scraper.getEconStats()
metrics = metrics.get_from_last_month()

tickers = ['AAPL', 'MSFT', 'AMZN']
weights = [0.35, 0.35, 0.3]

tickers, weights, data = risk.process_input(tickers, weights, 50)

var_array = risk.calculate_var(weights, data, 50, 100000)

productivity = float(econStats['Output per hour, nonfarm business, percent change from previous quarter at annual rate, seasonally adjusted'][1:4])

# Input from API
tickers = {}
totalInvestment = 1000000

riskFactor = var_array[-1]/totalInvestment * abs(metrics[0])/2.5 * metrics[1]/3.5 * 100/(100-metrics[2]+5) * (100+productivity)/100 + sentiment/100
print(riskFactor)