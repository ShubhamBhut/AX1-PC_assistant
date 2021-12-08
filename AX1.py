import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import sys
import os

pyautogui.FAILSAFE = False

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+10)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishing():
   hour = int(datetime.datetime.now().hour)   
   if hour < 10:
      speak("Bonjour sir")

   elif hour >= 10 and hour < 15:
      speak("Bonne apremidi sir")

   elif hour >= 15 and hour < 19:
      speak("Bonne soar sir")

   elif hour >= 19:
      speak("Bonne nui sir")


def listener():

   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("I am listening sire...")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"You said: {query}\n")  

   except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
   return query   

if  __name__ == "__main__":
   wishing()
   listener()
   while True:
      input1 = listener().lower()

      if "open youtube" in input1:
         webbrowser.open("youtube.com")

      elif "open whatsapp" in input1:
         webbrowser.open("web.whatsapp.com")

      elif "close this" in input1:
         pyautogui.click(1919, 0)

      elif "who" and "you" in input1:
         speak("I am AX1, an assistant under development") 

      elif "play" and "million" in input1:
         webbrowser.open("https://youtu.be/5rm-TDPjYIo")

      elif "open my drive" in input1:
         webbrowser.open("D://")
            
      elif 'the time' in input1:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

      elif 'open code' in input1:
         codepath = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)