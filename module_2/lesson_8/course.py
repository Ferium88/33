import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime("%d.%m.%Y")

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={"data_req":today})
soup = BeautifulSoup(response.content, features="xml")

def get_currency(currency_id):
    valute = soup.find("Valute", ID=currency_id)

    valute_value = valute.Value.text
    valute_name = valute.Name.text

    valute_info = {'name': valute_name, 'value': valute_value}

    return valute_info




# currency_id = input("Введите айди вадюты: ")

# print(get_currency("R01010").get('name'), get_currency("R01010").get('value'))