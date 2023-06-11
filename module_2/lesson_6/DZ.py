valute_from = str(input("Введите конвертируемую валюту: ")).upper()
valute_to = str(input("Введите валюту в которую конвертируем: ")).upper()
amount = int(input("Введите сумму конвертируемой валюты: "))

ID_list = {"USD": 69.33, "EUR": 75.4}

def course (valute_from, valute_to, amount):
    if valute_from == "RUR" and valute_to == "USD":
        rez = (amount * ID_list.get("USD"))
        print(rez)
    elif valute_from == "RUR" and valute_to == "EUR":
        rez = (amount * ID_list.get("EUR"))
        print(rez)
    elif valute_from == "EUR" and valute_to == "RUR":
        rez = (amount / ID_list.get("EUR"))
        print(rez)
    elif valute_from == "USD" and valute_to == "RUR":
        rez = (amount / ID_list.get("USD"))
        print(rez)

course(valute_from, valute_to, amount)