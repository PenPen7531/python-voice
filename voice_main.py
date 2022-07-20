from operator import truediv
import speech_recognition
import pyttsx3
import pyaudio
engine = pyttsx3.init()
from models.tasks import Task
from models.log import Logs

engine.setProperty("rate",150)
recognizer=speech_recognition.Recognizer()

engine.say("Hello! What is your name")

print("Hello! What is your name?")
engine.runAndWait()
name=True
while name:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio=recognizer.listen(mic)
            text=recognizer.recognize_google(audio)
            text=text.lower()
            text=text.split()
            if len(text) == 1:
                engine.say(f"Is {text[0].capitalize()} your name?")
                print(f"Is {text[0].capitalize()} your name?")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio=recognizer.listen(mic)
                answer=recognizer.recognize_google(audio)
                repeat=True
                while repeat:
                    if answer.lower()=="yes":
                        print("Great lets continue")
                        engine.say("Great lets continue")
                        repeat=False
                        name=False
                    elif answer.lower()=="no":
                        repeat=False
                        print("Lets try again")
                        print("What is your name")
                        engine.say("Lets try again")
                        engine.say("What is your name")
                    else:
                        print("Sorry. I didnt understand that.")
                        engine.say("Sorry. I didnt understand that.")
            elif len(text) == 2:
                repeat=True
                while repeat:
                    print(f"Is {text[0].capitalize()} {text[1].capitalize()} your name?")
                    engine.say(f"Is {text[0].capitalize()} {text[1].capitalize()} your name?")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio=recognizer.listen(mic)
                    answer=recognizer.recognize_google(audio)
                    if answer.lower()=="yes":
                        print("Great lets continue")
                        engine.say("Great lets continue")
                        repeat=False
                        name=False
                    elif answer.lower()=="no":
                        repeat=False
                        print("Lets try again")
                        print("What is your name")
                        engine.say("Lets try again")
                        engine.say("What is your name")
                    else:
                        print("Sorry. I didnt understand that.")
                        engine.say("Sorry. I didnt understand that.")
                
            else:
                print("Sorry I didnt get that.\nPlease try again.")
                print("What is your name?")
                engine.say("Sorry I didnt get that.\nPlease try again.")
                engine.say("What is your name?")
    except:
        recognizer=speech_recognition.Recognizer()
        continue
    program=True
    engine.say("What task would you like to perform.\n\t1) Set Task\n\t2) Voice Calculator")
    print("What task would you like to perform.\n\t1) Set Task\n\t2) Voice Calculator")
    engine.runAndWait()
    while program:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio=recognizer.listen(mic)
            text=recognizer.recognize_google(audio)
            text=text.lower()
            if text == "set task":
                task=True
                while task:
                    print("Setting task.\nWhich task would you like to set.")
                    engine.say("Setting task.Which task would you like to set.")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio=recognizer.listen(mic)
                    text=recognizer.recognize_google(audio)
                    text=text.lower()
                    engine.say(f"Setting task {text}. Is this correct?")
                    print(f"Setting task: {text}. Is this correct")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio=recognizer.listen(mic)
                    response=recognizer.recognize_google(audio)
                    response=text.lower()
                    if response=="yes":
                        print("Adding task")
                        engine.say("Adding task.")
                        log=Logs(text[0])
                        log.add_task(Task(response, "Jan 31"))
                        task=False
                    elif response=="no":
                        engine.say("Please try again")
                        print("Please Try again")
                    else:
                        print("Sorry I didn't get that. Please try again")
                        engine.say("Sorry I didn't get that. Please try again")
                repeat=True
                while repeat:
                    engine.say("Would you like to perform another task?")
                    print("Would you like to perform another task")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio=recognizer.listen(mic)
                    text=recognizer.recognize_google(audio)
                    text=text.lower()
                    if text=="yes":
                        repeat=False
                    elif text=="no":
                        repeat=False
                        prgram=False
                        print("Shutting down program")
                        engine.say("Shutting down program")
                        engine.runAndWait()
                        exit()
                    else:
                        print("Sorry I did not understand that. Please try again.")
                        engine.say("Sorry, I did not understand that. Please try again")
