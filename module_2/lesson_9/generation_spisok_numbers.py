# my_list = [i if i % 3 == 0 else i ** 2 for i in range(1000) if i % 5 == 0]

# print(my_list)

my_dict = {i: len(i) for i in ['orange', 'green', 'blue'] if len(i) != 5}
print(my_dict)