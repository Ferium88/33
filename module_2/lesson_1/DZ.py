action = (input("Выражение(+) или Дискриминант(-): "))
if action == "+":
    number1 = int(input("Введите первое число: " ))
    number2 = int(input("Введите второе число: "))
    znak = str(input("Введите действие: "))
    if znak.lower() in ("+", "cложение", "сумма"):
        ravno = number1 + number2
        print(f"Сумма чисел {number1} и {number2} равна {ravno}.")
    elif znak.lower() in ("-", "разность", "вычитание"):
        ravno = number1 - number2
        print(f"Разность чисел {number1} и {number2} равна {ravno}.")
    elif znak.lower() in (":", "частное", "деление"):
        ravno = number1 / number2
        print(f"Частное чисел {number1} и {number2} равна {ravno}.")
    elif znak.lower() in ("*", "произведение", "умножение"):
        ravno = number1 * number2
        print(f"Произведение чисел {number1} и {number2} равна {ravno}.")
elif action == "-":
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    c = int(input("Введите число C: "))
    ravno = b**2 - (4*a*c)
    print(f"Дискриминант равен {ravno}.")
