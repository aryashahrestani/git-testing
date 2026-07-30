import pyttsx3

def sound_hacker():
    for i in range(3):
        e = pyttsx3.init()
        e.setProperty("rate",110)
        e.say("Hacked By Zero Team")
        e.runAndWait()

sound_hacker()
