from gtts import gTTS
import os

Mytext = input("Enter text you want : ")
language = "en"
output = gTTS(text=Mytext, lang=language, slow=False)
output.save("Output.mp3")
os.system("start Output.mp3")
