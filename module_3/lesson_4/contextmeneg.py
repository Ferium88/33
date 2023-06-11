import contextlib
# file = open('text.txt', 'w', encoding='utf-8')
# file.write('Веб по контекстному менеджеру')
# file.close()

# with open('text.txt', 'w', encoding='utf-8') as file:
#     file.write('Веб по контекстному менеджеру')

# @contextlib.contextmanager
# def reverse_str(string):
#     yield string[::-1]
# with reverse_str('hello') as reversed_string:
#     print(reversed_string)


@contextlib.contextmanager
def exc_handler(*args):
    try:
        yield
    except args:
        print("Ошибка, но мне всё равно")

my_list = [1, 2]

my_dict = {1: 1}

with exc_handler(IndexError, ValueError, KeyError):
    print(my_list.asd)
    my_list[4]
    my_list[2]
