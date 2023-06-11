import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?date_req=28/01/2023")
soup = BeautifulSoup(response.content, features="xml")

def get_courese(currency_id):
    australian_dollar = soup.find("Valute", ID=currency_id)

    currency_value = australian_dollar.Value.text
    currency_nominal = australian_dollar.Nominal.text
    currency_name = australian_dollar.Name.text

    print(f"({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.")

currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    get_courese(currency['ID'])
