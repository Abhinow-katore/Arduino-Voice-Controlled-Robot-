import pyttsx3  #pyttsx3 is a text-to-speech conversion library in Python
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import MyAlarm
import smtplib  # send mail to any Internet machine with an SMTP or ESMTP listener daemon
engine = pyttsx3.init('sapi5') # nsss, espeak
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good moring")
    elif hour>=12 and hour<18:
        speak("good after noon sir")
    """else:
        speak("good evening")  
    speak("hello abhinav what can i do for you")
"""
def takeCommand():
    #it takse microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # for voice recognition.
        print(f"User said: {query}\n")  #our query will be printed.

    except Exception as e:
        # print(e)    
        print("mic is on...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


'''email sending part commented, ue to risk of less secure app'''
"""def sendEmail(to, content):
    server smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login('shicnhan@gmail.com', 'himawari')
    server.sendEmail('shicnhan@gmail.com', to, content)
    server.close()"""

    

if __name__ == "__main__":
        print(" hello sir, i am lavaris ?")
        speak("hello sir, i am laavaarees")
        wishMe()
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"just a time verification its {strTime}")
        speak("what can i do for you")
        while True:
            query = takeCommand().lower()
            if 'nothing' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)     
            elif 'open youtube' in query:
                speak("what do you want to see on youtube")
                query = takeCommand().lower()
                webbrowser.open("https://www.youtube.com/results?search_query=" + query)
                speak("Opening youtube, hope you got your video ")
 
            elif 'on youtube' in query:
                speak("opening" + query)
                query = takeCommand().lower()
                webbrowser.open("https://www.youtube.com/results?search_query=" + query) 

            elif 'open google' in query:
                speak("what do you want to see on google")
                query = takeCommand().lower()
                webbrowser.open("google.com/?#q=" + query)
                speak("Opening youtube, hope you got your result")
            elif 'open github' in query:
                webbrowser.open("github.com")    
            elif 'play music' in query:
                music_dir = 'C:\\Users\\91957\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif 'open visual code' in query:
                codepath = "C:\\Users\\91957\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'ok bye' in query:
                speak("have a nice day sir")
                quit()
            elif 'how are you' in query:
                speak("I an fine sir, and you sir")
                
            elif 'left' in query: 
                speak("turning left")
            elif 'right' in query: 
                speak("turning right")
            elif 'forward' in query: 
                speak("going forward")
            elif 'backwrd' in query:
                speak("going backward")
            elif 'face' in query:
                speak("face detector camera is opening")
                codepath = "C:\\Users\\91957\\OneDrive\\Desktop\\OPENCV\\trackin.py"
                os.startfile(codepath)
            #alarm

            elif 'alarm' in query:
                speak("at which time do you want to set alarm")
                # speak("for example, set alarm 12:16 am")
                query = takeCommand().lower()           
                # query = query.replace("set alarm ", "")
                query = query.replace(".","")
                query = query.upper()
                import MyAlarm
                MyAlarm.alarm(query)
            elif "information" in query:
                speak("you need information related to which topic? ")
                print("you need information related to which topic? ")

                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source,1.2)
                    print("listening...")
                    audio = r.listen(source)
                    infor = r.recognize_google(audio)
                speak("searching {} in wikipedia".format(infor))
                assist = inflow()
                assist.get_info(infor)
           




