import cowsay

# Python text-to-speech lib/module
import pyttsx3

# To initialize the lib from text to speech
engine = pyttsx3.init()

# text/ material to be used
this = input("What's this? ")
cowsay.cow(this)

engine.say(this)
engine.runAndWait()
