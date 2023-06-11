class Tank:
    def __init__(self, name, armor, damage):
        self.name = name
        self.armor = armor
        self.damage = damage

    def __str__(self):
        return self.name

    def shoot(self, enemy):
        print(f'Есть попадание по врагу {enemy} ')
        enemy.health_down()

    def health_down(self, damage):
        print(f'Есть пробитие, по нам попали на {damage} урона.')
        self.armor -= damage


class T34(Tank):
    pass

class KV2(Tank):
    pass

t34 = T34('t34', 900, 180)
kv2 = KV2('kv2', 1500, 500)

t34.shoot(kv2)
kv2.shoot(t34)








































