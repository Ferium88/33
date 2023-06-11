# my_list = [1, 1, 2, 3, 4, 4] # в множестве не повтрояються элементы
# my_set = set(my_list)
# print(my_set)

my_set = {1, 2, 3, 4, 5}
my_set_2 = {4, 5, 6, 7, 8}
print(my_set.intersection(my_set_2)) # пересечение множеств
print(my_set.union(my_set_2))