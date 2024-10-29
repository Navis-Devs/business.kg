from bs4 import BeautifulSoup
import requests

url = "https://www.mashina.kg/search/all/?region=all"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='list-item list-label')

for quote in quotes:
    a_tag = quote.find('a')
    if a_tag and 'href' in a_tag.attrs:
        link = f"https://www.mashina.kg{a_tag['href']}"
        print(f"Зашел по ссылке: {link}")

        item_response = requests.get(link)
        item_soup = BeautifulSoup(item_response.text, 'lxml')
