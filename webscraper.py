import requests
from bs4 import BeautifulSoup 

titles=[]
URL = 'https://www.bls.gov/'

class Scraper:
    def __init__(self, keywords, link) -> None:
        self.titles = []
        self.keywords = keywords
        self.link = link
    
    # Method to return titles of articles discussing the economic state
    def getTitles(self, pages):
        for page in range(1, pages):
            r = requests.get(f"{self.link}{page}")
            
            soup = BeautifulSoup(r.content, 'html5lib')
            table = soup('a', attrs = {'class':'iX-r'}) 
            for row in table:
                index = 0
                found = False
                while not found and index < len(self.keywords):
                    text = row.get_text().lower()
                    if (self.keywords[index] in text):
                        self.titles.append(text)
                        found = True
                    index += 1
        return self.titles

    
    # Method to return stats about the economic state of the US
    def getEconStats():
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing the data
        table = soup.find('div', {'id': 'latest-numbers'})
        table = table.find_all('span', {'class': 'data'})

        results = {}

        for row in table:    
            results[row.attrs['title']] = row.get_text()
        
        return results