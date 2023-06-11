from course import get_currency, today
from tkinter import*

window = Tk()
window.geometry("500x500")
window.resizable(width=False, height=False)


image_logo = PhotoImage(file=r"/module_2/lesson_8/logo.png")

label_logo = Label(window, image=image_logo)
label_logo.place(x=0, y=0)

label_title = Label(window, text="ЦБРФ", font="TimesNewRoman 36", bg="orange")
label_title.place(x=230, y=50)

label_currencies = Label(window, text=f"Курс на {today}:", font="TimesNewRoman 20", bg="orange")
label_currencies.place(x=100, y=160)

dollar_info = get_currency("R01235")

dollar_info_str = f"{dollar_info.get('name')} {dollar_info.get('value')}"

label_currency = Label(window, text=dollar_info_str, font="TimesNewRoman 16", bg="lime")
label_currency.place(x=50,y=210)

euro_info = get_currency("R01239")
euro_info_str = f"{euro_info.get('name')} {euro_info.get('value')}"

euro_label = Label(window, text=euro_info_str, font="TimesNewRoman 16", bg="lime")
euro_label.place(x=50,y=240)

yuan_info = get_currency("R01375")
yuan_info_str = f"{yuan_info.get('name')} {yuan_info.get('value')}"

yuan_label = Label(window, text=yuan_info_str, font="TimesNewRoman 16", bg="lime")
yuan_label.place(x=50,y=270)

entry = Entry(font="TimesNewRoman 16")
entry.place(x=50, y=400)

y = 30

def search():
    global y
    currency_id = entry.get()
    currency_info = get_currency(currency_id)
    currency_info_str = f"{currency_info.get('name')} {currency_info.get('value')}"
    currency_label = Label(window, text=currency_info_str, font="TimesNewRoman 16", bg="blue")
    currency_label.place(x=50, y=270 + y)

    y += 30

button = Button(text="Найти", font="TimesNewRoman 16", bg="lime", command=search)
button.place(x=335, y=390)

window.mainloop()