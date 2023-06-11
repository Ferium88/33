def func(a,b, *args, **kwargs):
    print(a,b)
    print(args)
    print(kwargs)
func(10,20,30,40,50,60,70, "Макс", "Дамир", "Рома", "Миша", name="Ксюша", name_2="Тарас")