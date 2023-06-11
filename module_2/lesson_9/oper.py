age = 18

# if age >= 18:   # 1 вариант
#     is_allow = "Можно"
# else:
#     is_allow = "Нельзя"
#
# print((is_allow))

# is_allow = "Можно" if age >= 18 else 'Нельзя'  # 2 вариант
# print(is_allow)

citizenship = "Казахстан"
is_allow = "Можно" if age >= 18 and citizenship == "РФ" else "Нельзя"
print(is_allow)