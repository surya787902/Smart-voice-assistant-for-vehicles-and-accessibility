import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (Speak clearly into the mic)")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        speak("Sorry, I could not understand.")
    except sr.RequestError:
        print("Could not request results. Please check your internet.")
        speak("Could not request results. Please check your internet.")

def main():
    speak("Welcome to the accessibility speech recognition tool.")
    while True:
        print("\nSay something or say 'exit' to quit:")
        command = listen()
        if command:
            if 'exit' in command.lower():
                speak("Goodbye!")
                break
            else:
                speak(f"You said {command}")

if __name__ == "__main__":
    main()
  
