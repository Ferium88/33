import requests
from bs4 import BeautifulSoup

#name = "максим"
#print(name.capitalize())
#print(name.lower())
#print(name.upper())# изменение регистра

user_currency = input("Введит первые буквы валюты, которая вас интересует: ").capitalize()
currency_date = input("Введите дату в формате день/месяц/год: ")

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={"date_req": currency_date})
soup = BeautifulSoup(response.content, features="xml")

currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    currency_value = currency.Value.text
    currency_nominal = currency.Nominal.text
    currency_name = currency.Name.text

    if currency_name.startswith(user_currency):
        print(f"({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.")