import pyttsx3

engine = pyttsx3.init()

def speak(rep):
    engine.say(rep)
    engine.runAndWait()





