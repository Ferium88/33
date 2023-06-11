class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price =price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, int):
            return self.price + other
        elif isinstance(other, Item):
            return self.price + other.price

    def __radd__(self, other):
        if isinstance(other, int):
            return self.price + other
        elif isinstance(other, Item):
            return self.price + other.price


item1 = Item('Видеокарта', 15_000, 0.8)
item2 = Item('Процессор',20_000, 0.2)
item3 = Item('Оперативка',8_000, 0.2)

total_sum = item1 + item2
print(total_sum)

