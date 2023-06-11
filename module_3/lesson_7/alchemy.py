from tkinter import *
import random


window = Tk()
window.geometry('600x600')

class Steam:
    __instanse = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file=r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\aroma.png').subsample(4, 4)

    def __add__(self, other):
        pass

class Dust:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file=r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\free-icon-dust-2396941.png').subsample(4, 4)

class Clay:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file =r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\free-icon-pottery-7942410.png').subsample(4, 4)

class Wind:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file=r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()

class Earth:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file=r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Clay()

class Fire:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file=r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()

class Water:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instanse:
            cls.__instanse = super().__new__(cls)
            return cls.__instanse

    image = PhotoImage(file=r'C:\Users\PC\Max.Edic.PycharmProjects\module_3\lesson_7\free-icon-water-drop-4246703.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()


canvas = Canvas(width=600, height=600)
canvas.pack()

elements = [Earth(), Water(), Wind(), Fire()]
for elem in elements:
    canvas.create_image(random.randint(50, 500), random.randint(50, 500), image=elem.image)

def move(event):
    image_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(image_ids) == 2:
        image_id_1, image_id_2, = image_ids[0], image_ids[1]
        elem_1 = elements[image_id_1 - 1]
        elem_2 = elements[image_id_2 - 1]

        new_elem = elem_1 + elem_2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)

    canvas.coords(image_ids, event.x, event.y)

window.bind('<B1-Motion>', move)

window.mainloop()





