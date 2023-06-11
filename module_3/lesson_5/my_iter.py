import random


# my_list = [1,2,3,4,5]
# for i in my_list:
#     print(i)

# iterator = iter(my_list)
# for i in iter(my_list):
#     print(i)
#
# for i in iter(my_list):
#     print(i)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# print(next(iterator))


class RandomIterator:
    def __init__(self, limit):
        self.limit = limit
        self.__reloud = limit

    def __iter__(self):
        self.limit = self.__reloud
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(0, 100)

my_iter = RandomIterator(10)

for i in my_iter:
    print(i)

iter(my_iter)