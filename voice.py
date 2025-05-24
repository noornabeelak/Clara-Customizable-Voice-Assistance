import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import json
import requests
import pyaudio
import google.generativeai as genai
import re
from my_secrets import GEMINI_API_KEY

# Replace with your real Gemini API key


genai.configure(api_key=GEMINI_API_KEY)

# Create the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")



print('Loading your AI personal assistant')

# Search for Zira's voice
engine=pyttsx3.init('sapi5')
zira_voice = None
voices = engine.getProperty('voices')
for voice in voices:
    if 'ZIRA' in voice.id.upper():
        zira_voice = voice.id
        break

if zira_voice:
    engine.setProperty('voice', zira_voice)
else:
    print("Zira voice not found. Falling back to default.")
    engine.setProperty('voice', voices[0].id)  # Default voice


# voices=engine.getProperty('voices')
# engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Hi, I'm Clara . How can I assist you today?")



if __name__=='__main__':


    while True:
        #speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if any(greet in statement.lower() for greet in ['hey Clara ', 'hi', 'hello']):
            speak("Sure, please ask your question.")
            question = takeCommand()
            if question and question != "None":
                try:
                    # Instruct Gemini to answer concisely
                    prompt = f"Answer concisely and clearly. Question: {question}"
                    response = model.generate_content(prompt)
                    answer = response.text
                    clean_answer = re.sub(r'[*_`]', '', answer)
                    print("Gemini: ", clean_answer)
                    speak(clean_answer)
                except Exception as e:
                    speak("Sorry, I couldn't get an answer from Gemini.")
                    print("Gemini Error:", e)
            else:
                speak("Sorry, I couldn't hear your question clearly.")



        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Clara is shutting down,Good bye')
            print('your personal assistant Clara is shutting down,Good bye')
            break

        


        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Clara your persoanl assistant. I am programmed to help you')


        elif "who made you" in statement or "who created you" in statement or "who built you" in statement:
            speak("I was built by Noor Nabeela K")
            print("I was built by Noor Nabeela K")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            search_query = '+'.join(statement.split())  # Converts spaces to '+' for URL
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open_new_tab(url)
            speak(f"Here are the search results for {statement}")
            time.sleep(5)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)











