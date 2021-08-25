from math import trunc
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis sir. how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query} \n")

    except Exception as e:
        print("say that again please")
        return "None"
    return query
def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo
    server.starttls
    server.login("youremail@gmail.com", "your password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close

if __name__ == "__main__":
    wishMe()
    if 1:
            query = takecommand().lower()

            if 'wikipedia' in query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentances=1)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            
            elif "open google" in query:
                webbrowser.open("google.com")

            
            elif "open stackoverflow" in query:
                webbrowser.open("stackoverflow.com")

            elif "play music" in query:
                music_dir = "D:\\songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "the time" in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f" sir, time is {strtime}")

            elif "open code" in query:
                CodePath = "C:\\Users\\Gera Ji\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(CodePath)

            elif "email to harry" in query:
                try:
                    speak("what should i send")
                    content = takecommand()
                    to = "parthgera25@gmail.com"
                    sendemail(to, content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry parth bhai i cant send email")
                    
                




       

    




