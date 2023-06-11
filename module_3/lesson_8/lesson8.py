import pprint # красиво выводит код

if __name__ == "__main__":

    goods = [
        {
            'name': 'Iphone 7',
            'brand': 'Apple',
            'price': 400,
        },
        {
            'name': 'Ipad',
            'brand': 'Apple',
            'price': 500,
        },
        {
            'name': 'Windows 7',
            'brand': 'Microsoft',
            'price': 200,
        }
    ]

    def on_price(item): # 1 способ
        return item['price']
    print(sorted(goods, key=lambda item: item['price'])) # 2 способ

    filtered_list = filter(lambda item: item['brand'] == 'Apple', goods) # фильтрация
    print(list(filtered_list))

    numbers_list = ['1', '2', '3', '4', '5'] # преобразование в числа
    print(numbers_list)
    mapped_list = list(map(int, numbers_list))
    print(mapped_list)


    names_list = ['Данил', 'Миша', 'Булат'] # совмещение имён и фамилий из разных списков
    surnames_list = ['Устюжин', 'Saprykin', 'Ибрагимов']
    persons_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list))
    print(persons_list)

    indexed_goods = []
    for index, item in enumerate(goods):
        indexed_goods.append({index: item})
    pprint.pprint(indexed_goods)

    names_list = ['Марсель', 'Максим', 'Алексей', 'Ксения']
    surnames_list = ['Тарапатин', 'Словягин', 'Щербаков']
    for name, surname in zip(names_list, surnames_list):
        print(name, surname)


    print(__name__)

