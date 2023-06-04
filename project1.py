import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import smtplib
import random
import phonenumbers
import time
import pyautogui
import subprocess as sp
from PIL import Image
from phonenumbers import timezone,geocoder,carrier
# installed pyaudio for proceeding a code to play and record audio
import speech_recognition as sr
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(voices)
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
# print(volume)
engine.setProperty('volume', 100)


def speak(audio):
 engine.say(audio)
 # run and wait method, it processes the voice commands.
 engine.runAndWait()


def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour >= 0 and hour < 12:
      speak("good morning")
   elif hour >= 12 and hour < 18:
      speak("good afternoon")
   else:
      speak("good night")

   speak("hello i am aviatrices, plase tell me how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("listeninig......")
       r.pause_threshold = 1
       audio = r.listen(source)
    try:
       print("recognizing....")
       query = r.recognize_google(audio, language='en-in')
       print(f"user said:{query}\n")

    except Exception as e:
       print("say that again...")
       return "none"
    return query


def sendmail(to,content):
   server=smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login('shelkeaaditee45@gmail.com','password')
   server.sendmail('shelkeaaditee45@gmail.com',to ,content)
   server.close()

def closeapp () :
  speak("closing")
  if "youtube" in query:
      sp.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application")


# if __name__=="__main__":
wishme()
while True:
 query = takecommand().lower()
 time.sleep(2)


 

 if 'wikipedia' in query:
    speak('searching wikipedia....')
    query = query.replace("wikepedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)
    print(results)
    time.sleep(2)
      
 elif "open youtube" in query:
   webbrowser.open("youtube.com")
   #speak("what would you like to play")
   #command1 = takecommand()
   #pywhatkit.playonyt(command1)

 elif "open whatsapp" in query:
   webbrowser.open("whatsapp.com")
 elif "play music" in query:
 
      
     music_dir='D:\music2'
     songs=os.listdir(music_dir)
   
     d=random.choice(songs)

     print(songs)
     os.startfile(os.path.join(music_dir,d))

 elif "online music" in query:
   speak("which song would you like to play")
   command=takecommand()   
   pywhatkit.playonyt(command)
   time.sleep(3)


 elif "phone number details" in query:
  speak("enter a phone number")
  number=input("enter your no. with +: ")
  phone=phonenumbers.parse(number)
  time=timezone.time_zones_for_number(phone)
  car=carrier.name_for_number(phone,"en")
  reg=geocoder.description_for_number(phone,"en")
  speak(phone)
  speak(f"the number is of  {car} company")
  #speak(car )
  speak(f"the number is belongs to {reg}")
  #speak(reg)
  speak(time)

 elif "email to customer" in query:
    try:
       speak("what should i say")
       content=takecommand()
       
       to=input("enter a email id who u want to send a email :")
       sendmail(to,content)
       speak("email has been sent ")
    except Exception as e:
       print(e)
       speak("sorry we canot send a email")
 

 elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
                speak("By what name do you want to save the screenshot?")
                name = takecommand()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")
 