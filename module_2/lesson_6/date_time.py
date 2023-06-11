from datetime import datetime

print(datetime.now().date()) # вывести только дату
print(datetime.now().date().month) # вывести только месяц
print(datetime.now().time().hour) # вывести только часы

my_str = "17/01/2002"
str_to_date = datetime.strptime(my_str, "%d/%m/%Y")
print(str_to_date.year)

date_to_str = datetime.now().strftime("%d/%m/%Y")

