 import pyttsx3  # pip install pyttsx3

import datetime
import smtplib
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
from email.message import EmailMessage
email_address="Your email"
password_of_email="Your Password"
stark="jarvis"
mypass=7943
chrome ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
email_list = {
    'Neelu': 'sp.shah211976@gmail.com',
    'dishu': 'drsti3121@gmail.com',
    'vanshika': 'vanshikaagrawal1704@gmail.com',
    'astha': 'patelastha252@gmail.com',
    'parth': 'parthsarda07@gmail.com',
    'mansi': 'ramlavatmansi@gmail.com'
}



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning , Mr.harsh")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ,Mr.harsh")

    else:
        speak("Good Evening, Mr.harsh")

    speak("I am Jarvis. We Are Online And Ready")
 
def get_email_info():
    speak('To Whom you want to send email sir')
    name = takeCommand()
    receiver = email_list[name]
    print(receiver)
    speak('What is the subject of your email sir?')
    subject = takeCommand()
    speak("What should I say sir?")
    message = takeCommand()
    sendEmail(receiver, subject, message)
    speak("Mr.Harsh Your Email has been sent!")
    speak("Do You Want Send More Email sir ?")
    send_more = takeCommand()
    if 'yes' in send_more:
        get_email_info()
   
def sendEmail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_address, password_of_email)
    email = EmailMessage()
    email['From'] = email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()