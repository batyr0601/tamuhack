import requests
from bs4 import BeautifulSoup 

titles=[]
keywords = ["economy", "employment", "inflation"];

class scraper:

    def getTitles(pages):
        for page in range(1, pages):
            r = requests.get(f"https://seekingalpha.com/market-outlook?page={page}")

        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup('a', attrs = {'class':'iX-r'}) 

        for row in table:
            index = 0
            found = False
            while not found and index < len(keywords):
                if (keywords[index] in row.get_text().lower()):
                    titles.append(row.get_text())
                    found = True

    print(getTitles(5))
