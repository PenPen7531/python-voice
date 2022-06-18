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
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio=recognizer.listen(mic)
                answer=recognizer.recognize_google(audio)
                repeat=True
                while repeat:
                    if answer.lower()=="yes":
                        print("Great lets continue")
                        repeat=False
                        name=False
                    elif answer.lower()=="no":
                        repeat=False
                        print("Lets try again")
                        print("What is your name")
                    else:
                        print("Sorry. I didnt understand that.")
            elif len(text) == 2:
                repeat=True
                while repeat:
                    print(f"Is {text[0].capitalize()} {text[1].capitalize()} your name?")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio=recognizer.listen(mic)
                    answer=recognizer.recognize_google(audio)
                    if answer.lower()=="yes":
                        print("Great lets continue")
                        repeat=False
                        name=False
                    elif answer.lower()=="no":
                        repeat=False
                        print("Lets try again")
                        print("What is your name")
                    else:
                        print("Sorry. I didnt understand that.")
                
            else:
                print("Sorry I didnt get that.\nPlease try again.")
                print("What is your name?")
    except:
        recognizer=speech_recognition.Recognizer()
        continue

        
