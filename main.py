import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0  and hour < 12 :
        speak("Good Morning !")
    elif hour >= 12  and hour < 18 :
        speak("Good Afternoon !")
    else :
        speak("Good Evening !")


def takeCommand():
    # This Function will allow your Jarvis to take microphone input from the user 
    # and returns a string output.

    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except:
        print("Sorry please say it again ")
        return "None"
    return query
    

if __name__ == "__main__":
    wishme()
    takeCommand()

