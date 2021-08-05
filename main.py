import wikipedia  # pip install wikipedia

import webbrowser
import os
import getpass
from data import wishMe, speak, takeCommand, stark, mypass, get_email_info, datetime, chrome
if __name__ == "__main__":
    c = 0
    speak("WELCOME TO STARK INDUSTRIES ,  please enter Username and Password to get access of jarvis")
    while c != 3:
        print("Enter Your Username: ")
        name = str(input())
        # print("Enter Password: ")
        login_password = int(getpass.getpass(prompt='Enter Your Password :'))

        if name == stark and login_password == mypass:
            wishMe()
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=15)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.get(chrome).open_new("youtube.com")

                elif 'open google' in query:
                    webbrowser.get(chrome).open_new("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.get(chrome).open_new("stackoverflow.com")

                elif 'play music' in query:
                    mylist = 'F:\\WORKSPACE\\Python\\JARVIS\\MUSIC'
                    songs = os.listdir(mylist)
                    print(songs)
                    os.startfile(os.path.join(mylist, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'i want to send email' in query:
                    try:
                        get_email_info()
                    except Exception as e:
                        print(e)
                        speak("Sorry Mr.harsh. I am not able to send this email")
                elif 'who is your creator jarvis' in query:
                    speak(
                        "Mr.Harsh Is My Boss,He Created Me And I am There For Mr.Harsh 7 Days A week And 24 hours In A Day ....Thank you")
                elif 'jarvis go for sleep' in query:
                    speak(
                        "Okay sir ! it's always a great glad to watching you work...Bye")
                    quit()
        else:
            speak("Wrong Username or password")
            c = c+1
    speak("Unauthorized access......sorry you can't try for login again")
