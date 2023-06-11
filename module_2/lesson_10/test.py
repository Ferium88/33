
class Pet:
    def __init__(self, has_tail, legs, name, ears):
        self.has_tail = has_tail
        self.legs = legs
        self.name = name
        self.ears = ears

    def __str__(self):
        return f"У {self.name} {self.legs} ноги и {'есть хвост' if self.has_tail else 'хвоста нет'}." \
            f"У него {'есть ушки' if self.ears else 'нет ушек'}."

    def sound(self):
        pass

# class Dog(Pet):
#     def __init__(self, legs, name, ears):
#         super().__init__(name=name, legs=legs, ears=ears, has_tail=True)
#
# dog = Dog(4, 'Чарли', True)
#
# print(dog)
#
# class Cat(Pet):
#     def __init__(self, has_tail, legs, name):
#         super().__init__(has_tail=has_tail, legs=legs, name=name, ears=True)
#
# cat = Cat(True, 4, 'Барсик')
#
# print(cat)



