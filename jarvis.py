Dimport pyttsx3
import datetime
import wikipedia
import smtplib
import speech_recognition as sr
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is ")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current day is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12 :
        speak("Good Morning")
    elif hour >= 12 and hour<18 :
        speak("Good Afternoon")
    elif hour >= 18 and hour<24 :
        speak("Good Evening")
    else :
        speak("Good night sir")
    speak("I am Jarvis, how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recogninzing")
            query = r.recognize_google(audio,language = 'en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again please ....")
            return "None"
        return query
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result )
        elif 'offline' in query:
            speak("Good bye Sir")
            quit()
