import speech_recognition as sr
import random

recognizer = sr.Recognizer()

film = [
    "Аватар",
    "Мстители Финал",
    "Форсаж",
    "Гарри Поттер"
]

while True:
    with sr.Microphone(device_index=1) as sourse:
        print("Скажите что-нибудь...")

        speech = recognizer.listen(sourse)

        speech_to_text = recognizer.recognize_google(speech, language="ru_RU")

        print(f"Вы сказали: {speech_to_text}")

        if speech_to_text.lower() == "фильм":
            print("Советую посмотреть фильм " + random.choice(film))