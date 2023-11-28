import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import subprocess as sp
import os
import pyautogui as pag
import psutil as pu
import pyjokes as pj

engine = pyttsx3.init()

def say(ad):
    engine.say(ad)
    engine.runAndWait()

def time():
    t = dt.datetime.now().strftime("%I:%M:%S")
    say("The Time is")
    say(t)

def date():
    y = dt.datetime.now().year
    m = dt.datetime.now().month
    d = dt.datetime.now().day
    say("The Date is")
    say(d)
    say(m)
    say(y)

def greet():
    h = dt.datetime.now().hour
    if((h>=0)and(h<12)):
        say("Good Morning")
    elif((h>=12)and(h<18)):
        say("Good Afternoon")
    elif((h>=18)and(h<24)):
        say("Good Evening")
    say("My Name is Orion, What Can I Do For You?")

def recogcnd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        ad = r.listen(source)


    try:
        print("Recognizing..")
        q = r.recognize_google(ad, language = 'en-in')
        print(q)

    except Exception as e:
        print(e)
        say("Please Repeat")

        return "None"
    return q

def ss():
    img = pag.screenshot()
    img.save(r"C:\Users\apsbi\Pictures\Screenshots\ss.png")

def usage():
    cuse = str(pu.cpu_percent())
    say("CPU Is At"+cuse+"%")
    buse = pu.sensors_battery()
    percent = buse.percent
    mes = f"Battery Is At {percent}%"
    say(mes)

def joke():
    say(pj.get_joke())

if __name__ == "__main__":
    greet()
    while True:
        q = recogcnd().lower()
        
        if('time' in q):
            time()
        elif('date' in q):
            date()
        elif('wikipedia' in q):
            say("Searching..")
            q = q.replace("wikipedia","")
            res = wp.summary(q, sentences = 3)
            print(res)
            say(res)
        elif('search' in q):
            say("What Should I Search For?")
            ser = recogcnd().lower()
            surl = f"https://www.google.com/search?q={ser}"
            wb.open(surl)
        elif('website' in q):
            say("Which Website Should I Open?")
            ser = recogcnd().lower()
            url = ser+'.com'
            path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            sp.Popen([path,url])
        elif('logout' in q):
            os.system("C:\\Windows\\System32\\shutdown.exe -l")
        elif('shutdown' in q):
            os.system("C:\\Windows\\System32\\shutdown.exe /s /t 1")
        elif('restart' in q):
            os.system("C:\\Windows\\System32\\shutdown.exe /r /t 1")
        elif('play' in q):
            sdir = r'C:\Users\apsbi\Music'
            songs = [file for file in os.listdir(sdir) if file.endswith(('.mp3', '.wav', '.ogg'))]
            os.startfile(os.path.join(sdir, songs[0]))
        elif('remember' in q):
            say("What Should I Remeber?")
            rem = recogcnd()
            say("You Told Me to Remember That"+rem)
            rember = open('rem.txt', 'w')
            rember.write(rem)
            rember.close()
        elif('do you know' in q):
            rember = open('rem.txt', 'r')
            say("You Told Me to Remember That"+rember.read())
        elif('screenshot' in q):
            ss()
            say("Screenshot Taken")
        elif('usage' in q):
            usage()
        elif('joke' in q):
            joke()
        elif('stop' in q):
            quit()