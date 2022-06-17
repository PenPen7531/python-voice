import speech_recognition
import pyttsx3
import pyaudio

recognizer=speech_recognition.Recognizer()

print("Hello! What is your name")
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
                print(f"Is {text[0].capitalize()} your name?")
                answer=input("Yes/No: ")
                if answer.lower()=="yes":
                    print("Great lets continue")
                    name=False
                elif answer.lower()=="no":
                    print("Lets try again")
                    print("What is your name")
            elif len(text) == 2:
                print(f"Is {text[0].capitalize()} {text[1].capitalize()} your name?")
                answer=input("Yes/No: ")
                if answer.lower()=="yes":
                    print("Great lets continue")
                    name=False
                elif answer.lower()=="no":
                    print("Lets try again")
                    print("What is your name")
                
            else:
                print("Sorry I didnt get that.\nPlease try again.")
    except:
        recognizer=speech_recognition.Recognizer()
        continue

        
