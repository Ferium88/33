from tkinter import *

window = Tk()
window.geometry("1000x800")

canvas = Canvas(window, width=1000, height=800, bg="white")
canvas.pack()

canvas.create_rectangle(200, 200, 500, 500, fill='lime')
canvas.create_polygon(200, 200, 350, 100, 500, 200, fill="orange")
canvas.create_polygon(200, 500, 350, 400, 500, 500, fill="red")
canvas.create_rectangle(250, 270, 450, 400, fill="blue")


class Real_House:
    window_house = 1
    different_colors = 4
    color_of_house = 'lime'

house = Real_House

class House:
    def __init__(self, window, different_colors, color_of_house):
        self.window = window
        self.different_colors = different_colors
        self.color_of_house = color_of_house
    def __str__(self):
        return f"У дома {self.window} окон, дом имеет {self.different_colors} разных цвета, основной цвет дома - {self.color_of_house}."

my_house = House(1, 4, 'lime')

print(my_house)

window.mainloop()


















