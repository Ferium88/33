def palindrom(slovo):
    a = slovo[::-1]
    if a == slovo:
        print(True)
    else:
        print(False)
palindrom(input("Введите слово или символы: "))