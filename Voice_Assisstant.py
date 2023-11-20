import speech_recognition as sr
import pyttsx3
import datetime
import shutil
import os
import wikipedia 
import webbrowser
import smtplib
import openai
import winshell
import ctypes
import time
import subprocess
from ecapture import ecapture as ec
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Anmol"
bot_name = "mac"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    #bot_name =("Mac")
    speak("I am your Assistant")
    speak(bot_name)
	    
def username():
	speak("What should i call you sir")
 
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    username()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            playsound("C:\\Users\\getan\\Desktop\\codes\\harrypotter.mp3")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'who made you' in query:
            speak("I Have been created by Anmol")
        
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
            
        elif "who i am" in query:
            speak("If you talk then definitely your human")
        
        elif 'open my project presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\getan\\Desktop\\PROJECT_PPT.pptx"
            os.startfile(power)
            
        elif "who are you" in query:
            speak("I am your Chat gpt integrated virtual assistant created by Anmol")
        
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Anmol ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"C:\\Users\\getan\\Desktop\\walpapers\\52268.jpg",0)
            speak("Background changed successfully")
        
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
            
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "mac Camera ", "img.jpg")
            
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
            
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Note.txt', 'w')
            file.write(note)
        
        elif "show note" in query:
            speak("Showing Notes")
            file = open("Note.txt", "r")
            print(file.read())
            speak(file.read(6))