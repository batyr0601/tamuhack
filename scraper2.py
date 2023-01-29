import requests
from bs4 import BeautifulSoup

url2 = 'https://www.bls.gov/'
response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the data
table = soup.find('div', {'id': 'latest-numbers'})
table = table.find_all('span', {'class': 'data'})

results = {}

for row in table:    
    results[row.attrs['title']] = row.get_text()


