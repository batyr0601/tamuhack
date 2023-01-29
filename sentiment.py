import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import webscraper

sid = SentimentIntensityAnalyzer()

keywords = ["economy", "gdp", "growth", "gain", "loss"]
link = "https://seekingalpha.com/market-outlook/economy?page="

scraper = webscraper.Scraper(keywords, link)
titles = scraper.getTitles(10)

average = []

for header in titles:
    average.append(sid.polarity_scores(header)['compound'])

print(sum(average) / len(average)) 