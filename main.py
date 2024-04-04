import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
from gtts import gTTS
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

# retrieving sapi5 from pyttsx3
engine = pyttsx3.init('sapi5')
# getting voices 
voices = engine.getProperty('voices')
#voices[0]--male   voices[1]--female
engine.setProperty('voice', voices[1].id)


asname =("Sony one point o")

#using engine to assist
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Inotation or Welcome lines
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("Good Morning Dear!")
        speak("Good Morning Dear!")
        
        time.sleep(0.8)

    elif hour>= 12 and hour<18:
        print("Good Afternoon Dear!")
        speak("Good Afternoon  Dear!")
        time.sleep(0.8)

    else:
        print("Good Evening Dear!")
        speak("Good Evening Dear !")
        time.sleep(0.8)

    
    print("I am your Assistant friend here to help you in many ways")
    speak("I am your Assistant friend") 
    time.sleep(1)
    speak( " here to help you in many ways")
    speak(asname)

#defining username
def username():
    print("Welcome Friend"+" What should i call you friend")
    speak("Welcome Friend")
    speak(" What should i call you friend")
    uname = takeCommand()
    
    columns = shutil.get_terminal_size().columns
    print("-----------------------------".center(columns))
    print("Welcome ", uname.center(columns))
    print("-----------------------------".center(columns))
    speak("Welcome "  + uname)
    print("How can i Help you, dear")
    speak("How can i Help you, dear")

    return uname

#taking command from user using microphone  
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-IN')   
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query
# function for sending email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


# the main function program starts from here
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    name=username()
    
    while True:
        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Here you go to Youtube\n")
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            break

        elif 'open google' in query:
            print("Here you go to Google\n")
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
            break

        elif 'open stack overflow' in query:
            print("Here you go to Stack Over flow.Happy coding")
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")
            break

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir, it must be from system dir"
            music_dir = "C:\\Users\\ekshi\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
            break

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(" the time is "+strTime)
            speak(f" the time is {strTime}")

        elif 'email to ' in query:
            try:
                speak("what should i send")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)            # for sending gmail, you must allow less secure apps in settings of gmail
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        
        elif "calculate" in query:

            app_id = 'CFHY6R-HPUYBDSA8L'
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        
        # for retreving news
        elif 'news' in query:

            try:
                #the user must generate their own api key using https://newsapi.com
                api_key="b61419f3e8c44a59b223fe7105c2fd8d"
                main_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
                news= requests.get(main_url).json()
                data = news["articles"]

                
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                news_article=[]

                for item in data:
                    news_article.append(item['title'] )
                for i in range(7):
                    print(i+1,news_article[i+1])
                    speak(news_article[i+1])
                    
                    
            except Exception as e:

                print(str(e))

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "ce44e642fe7c09526ccd29be3b46719f"
            
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?&q={city_name}&units=imperial&appid={api_key}")
            
            x = response.json()

            if x['cod'] != '404':
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                speak(" Temperature (in kelvin unit) = " +str(current_temperature)+" atmospheric pressure (in hPa unit) ="+str(current_pressure) +" humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

            else:
                speak(" City Not Found ")

        # general and funny instructions and commands
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            print("I am fine, Thank you"+ " What about you")
            speak("What about you ")
            

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            name = query

        elif "change name" in query:
            speak("What would you like to call me ")
            asname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            print("My friends call me", asname)
            speak("My friends call me")
            speak(asname)
            

        elif 'stop' in query or 'exit' in query:
            print("Thanks for giving me your time")
            speak("Thanks for giving me your time")
            exit(1)

        elif "who made you" in query or "who created you" in query:
            print("I have been created by You.")
            speak("I have been created by You.")

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "who am i" in query:
            speak("If you talk then definitely you are human.")

        elif "why you came to world" in query:
            speak("Thanks to you, and further It's a secret")

        elif 'what is love' in query:
            speak("It is sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Ekshith and his friends")

        elif 'for what reason you are created' in query:
            speak("I was created as a project by Mister Ekshith and his friends")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                    0,
                                                    "Location of wallpaper",
                                                    0)
            speak("Background changed successfully")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                break

        elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop me from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
            break

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Sony Camera ", "img.jpg")
            break

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
            break

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
            break

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            break

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak(" Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            para=file.read()
            print(para)
            speak(para)

        
                    
        elif "hey " in query:
            speak("hello friend"+ name)

        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Your Account Id'
                auth_token = '6787e7b8aeaf64cea6e92461b0ff8624'
                client = Client(account_sid, auth_token)

                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )

                print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you ")
            speak(name)

        # Most asked question from Google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("No  it is not possible" )
            time.sleep(0.5)
            speak(", but i may be your best friend")

        elif "how are you" in query:
            speak("I'm fine")
        
        elif "what is" in query or "who is" in query:
            # Use the same API key
            # that we used earlier
            client = wolframalpha.Client('AUQY6R-HQUXKAUV8K')
            res = client.query(query)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        # elif "" in query:
            # Command go here
           
