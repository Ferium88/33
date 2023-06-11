class User:
    def __init__(self, health, damage, type_of_attack):
        self.health = health
        self.damage = damage
        self.type_of_attack = type_of_attack
    def __str__(self):
        return f"HP = {self.health}, урон = {self.damage}, тип атаки = {self.type_of_attack}."

class Archer(User):
    def __init__(self, health=300, damage=50, type_of_attack="лук и стрелы"):
        super().__init__(health, damage, type_of_attack)

class Mag(User):
    def __init__(self, health=230, damage=90, type_of_attack="магия"):
        super().__init__(health, damage, type_of_attack)

class Warrior(User):
    def __init__(self, health=500, damage=70, type_of_attack="мечь"):
        super().__init__(health, damage, type_of_attack)