import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

    # 🌐 Websites
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startwith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # 💻 Apps
    elif "open notepad" in c.lower():
        os.system("notepad")
    elif "open calculator" in c.lower():
        subprocess.popen("calc.exe")
    elif "open chrome" in c.lower():
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "open vs code" in c.lower():
        os.startfile("C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")



if __name__== "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wale word "Jarvis"
        # Obtain audio from the mmicrophone
        r = sr.Recognizer()

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)


                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))