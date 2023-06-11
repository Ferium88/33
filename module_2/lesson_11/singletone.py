class SingleTone:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name):
        self.name = name

a = A("Никита")
a1 = A("Миша")

print(a is a1)
