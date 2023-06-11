import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Время работы функции '{func_name}' состовило {total_time}".format(
            func_name=func.__name__, total_time=time.time() - start
        ))
        return result
    return wrapper

@timer
def get_list_by_defolt(val):
    my_list = []
    for i in range(val):
        my_list.append(i)

    return my_list

@timer
def get_list_by_comp(val):
    return [i for i in range(val)]

get_list_by_comp(10 ** 6 * 15)
get_list_by_defolt(10 ** 6 * 15)