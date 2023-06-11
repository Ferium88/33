from gtts import gTTS

f = open("text.txt", "r", encoding="utf-8")
text = f.read()
f.close()

tts = gTTS(text=text, lang="ru")
tts.save("bot.mp3")