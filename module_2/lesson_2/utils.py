import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BASE_FILES_PATH = r"/module_2/lesson_2/extra"


def get_random_photo():
    random_img_number = random.randint(1, 9)
    random_img = open(fr"{BASE_FILES_PATH}\{random_img_number}.jpg", "rb")
    return random_img


def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button1 = KeyboardButton("/cats")
    button2 = KeyboardButton("/poem")
    button3 = KeyboardButton("/sticker")
    button4 = KeyboardButton("/music")
    button5 = KeyboardButton("/play")
    button6 = KeyboardButton("/game")

    keyboard.add(button1, button2, button3, button4, button5, button6)
    return keyboard


def poem_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Перейти:", url="https://stihi.ru/")

    keyboard.add(button)
    return keyboard

def get_play():
    vid = ["Экшен", "РПГ", "Гонки", "Интерактивное кино", "Приключение", "Выживание"]
    randon_play = random.choice(vid)
    return randon_play

def get_play_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button1 = KeyboardButton("/Экшен")
    button2 = KeyboardButton("/poem")
    button3 = KeyboardButton("/sticker")
    button4 = KeyboardButton("/music")
    button5 = KeyboardButton("/play")
    button6 = KeyboardButton("/game")

    keyboard.add(button1)
    return keyboard
