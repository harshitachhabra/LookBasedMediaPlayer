import cv2
import pyautogui as pu
import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import os
from time import ctime
import re
import webbrowser
import bs4
import requests 
import smtplib  
import uuid
import tkinter as tk
root=tk.Tk()
def respond_pause_play(string1):
    print(string1)
    tts1=gTTS(text=string1,lang='en')
    filename='Speech%s.mp3'%str(uuid.uuid4())
    tts1.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
        
def lookbased():
    cap = cv2.VideoCapture(0)
    faces_cascade=cv2.CascadeClassifier('put the link of harcascade file')
    k=0
    c=0
    z=0
    h=0
    while (True):
        ret, frame = cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=faces_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
        print(faces)
        if(len(faces)==0):
            k+=1
            if k==1:
                pu.press('space')
                respond_pause_play("your video is paused")
                c=1
                if c==1:
                      continue
        k=0 
         
        respond_pause_play("Your video is playing")
        for (x,y,w,h) in faces:
            print(x,y,w,h)
            c=x+100
            c1=y+100
            color=(255,0,0)
            strok=2
            hight=x+h
            wid=y+w
            cv2.rectangle(frame,(x,y),(hight,wid),color,strok)






        cv2.imshow('Capturing....', frame)
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio=r.listen(source,phrase_time_limit=5)
    data=""
    try:    
        import pyaudio
        data=r.recognize_google(audio,language='en-US')
        print("you said"+data)
    except sr.UnknownValueError:
       print("i cannot hear you")
    except sr.RequestError as e:
       print("Request Failed")

    return data



def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en')
    filename='Speech%s.mp3' %str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename) 
    os.remove(filename)
  
def voice_assistant(data):
    if "open youtube" in data.casefold():
        listening= True
        reg_ex= re.search('open youtube(.*)',data)
        url='https://www.youtube.com/'
        if reg_ex:
            sub=reg_ex.group(1)
            url=url+ 'r/'
        webbrowser.open(url)
        print('Done')
        respond('Done')
   
    if "media player" in data:
        lookbased()
      

        
    if "stop" in data:
        listening=False
        print('Listening Stopped')
        respond("see you")
    try:

        return listening
    except UnboundLocalError:
         print("timedout")
respond("What can i do for you")
listening=True
while listening==True:
    data=listen()
    listening=voice_assistant(data)

