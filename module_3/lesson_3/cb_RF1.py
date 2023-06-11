import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
soup = BeautifulSoup(response.content, features="xml")


def get_course(course_id):
    return soup.find("Valute", ID=course_id).Value.text
