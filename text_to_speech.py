from gtts import gTTS
import os

text = "Hello, this is a test of to speech test."

tts = gTTS(text=text, lang='en')
tts.save("speech.wav")