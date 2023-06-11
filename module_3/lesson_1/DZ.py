class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee
    def info(self):
        print(f'У {self.name} зарплата равна {self.salary}, работник {self.on_vacation}.')


employee1 = Employee('Данил', 200_000, 'в отпуске', True)
employee2 = Employee('Алина', 250_000, 'на работе', True)
employee3 = Employee('Андрей', 225_000, 'в отпуске', True)
employee4 = Employee('Максим', 250_000, 'на работе', True)
employee5 = Employee('Влад', 10_000, 'в отпуске', False)

my_list = []

my_list.append(employee1)
my_list.append(employee2)
my_list.append(employee3)
my_list.append(employee4)
my_list.append(employee5)

for employee in my_list:
    employee.info()

print(my_list)

for employee in my_list:
    if employee.is_good_employee == False:
        print(f'{employee.name} уволен(а).')
