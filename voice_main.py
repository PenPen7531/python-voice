import speech_recognition
import pyttsx3
import pyaudio
engine = pyttsx3.init()
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

        
