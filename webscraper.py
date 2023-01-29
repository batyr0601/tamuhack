import requests
from bs4 import BeautifulSoup 

titles=[]
keywords = ["economy", "gdp", "growth", "gain", "loss"]
link = "https://seekingalpha.com/market-outlook?page="

class Scraper:
    def __init__(self, keywords, link) -> None:
        self.titles = []
        self.keywords = keywords
        self.link = link
    
    def getTitles(self, pages):
        for page in range(1, pages):
            r = requests.get(f"{self.link}{page}")
            
            soup = BeautifulSoup(r.content, 'html5lib')
            table = soup('a', attrs = {'class':'iX-r'}) 
            for row in table:
                index = 0
                found = False
                while not found and index < len(keywords):
                    text = row.get_text().lower()
                    if (self.keywords[index] in text):
                        self.titles.append(text)
                        found = True
                    index += 1
        return self.titles

scraper = Scraper(keywords, link)

print(scraper.getTitles(10))