import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
soup = BeautifulSoup(response.content, features="xml")


def get_dollar_course():
    return soup.find("Valute", ID="R01235").Value.text
