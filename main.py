import requests
from bs4 import BeautifulSoup

response = requests.get("https://easytransacts.com/")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.body)