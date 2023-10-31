import pyttsx3 #pip install pyttsx3
import requests
import pywikihow
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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

    speak("I am Jarvis. How may i suggest you today!!")

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
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
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
            webbrowser.open("google.com/search?q='mainepyaarkiya'")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

     #   elif 'open code' in query:
      #      codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       #     os.startfile(codePath)
        if 'your name' in query:
            speak('My name is Jarvis')
        if 'meet you' in query:
            speak("Nice to meet u too")
        if 'hello' in query:
            speak("Hii")
        if 'how are you' in query:
            speak("I am fine, What about you")
        if 'i am also fine' in query:
            speak("It's great")
        if 'how are u' in query:
            speak("I am fine, what about you")
        if 'nice' in query:
            speak("Thanks")
        if 'what can you do' in query:
            speak("I can do whatever the things you would like me to do. As i am not completed yet, there is some limitations for what i can do ")
        if 'what you can do' in query:
            speak("I can do whatever the things you would like me to do. As i am not completed yet, there is some limitations for what i can do ")
        if 'play song' in query:
            speak("Playing song")
        if '10 movies' in query:
            speak("It may depend on your movie taste. But for mine i will prefer you to watch The Godfather, Shawshank Redemption, Citizen Kane, Pulp Fiction, The Dark Knight, Schindler's List, The Lord of the Rings: The Return of the King, Casablanca, Gone with the Wind, Star Wars: Episode IV - A New Hope")
        if "what's going" in query:
            speak("Haha! Nothing Special")
        if 'play with me' in query:
            speak("I would love to play with u . But due to some restriction I can't. Sory")
        if 'want to play' in query:
                speak("I would love to play with u . But due to some restriction I can't. Sory")
        if 'sorry' in query:
             speak("It's ok")
        if 'who made you' in query:
            speak("Tanmay made me with the assisting of Hemanth")
        if 'your friend' in query:
            speak("My first and best friend is Tanmay. He made me ")
        if 'your best friend' in query:
            speak("My first and best friend is Tanmay. He made me ")
        if 'get lost' in query:
            speak("Sorry for the inconvenience")
        if 'are you robot' in query:
            speak("Ya!! What you think i should be. Hahaha")
        if 'Why you are robot' in query:
            speak("Ya!! What you think i should be. Hahaha")
        if 'really robot' in query:
            speak("Ya!! What you think i should be. Hahaha")
        if 'bye' in query:
            speak("Good Bye! See you soon")

        elif "activate how to do " in query:
            from pywikihow import search_wikihow
            speak("How to do mode is activated. Please tell me what you want to know")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif "how much power left" in query or "How much power we have" in query or "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak("Sir your system have (percentage) percent battery")

        elif 'email to tanmay' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sah.tanmay09@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")