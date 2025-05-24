import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Error connecting to the recognition service.")
        return ""

def handle_command(command):
    if "open browser" in command:
        speak("Opening browser")
        webbrowser.open("https://www.google.com")
    elif "go to youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "scroll down" in command:
        speak("Scrolling down")
        pyautogui.scroll(-1000)
    elif "scroll up" in command:
        speak("Scrolling up")
        pyautogui.scroll(1000)
    elif "close tab" in command:
        speak("Closing tab")
        pyautogui.hotkey('ctrl', 'w')
    elif "go back" in command:
        speak("Going back")
        pyautogui.hotkey('alt', 'left')
    elif "exit" in command or "quit" in command:
        speak("Exiting navigation system.")
        return False
    else:
        speak("Command not recognized.")
    return True

def main():
    speak("Voice navigation system started. Awaiting your command.")
    while True:
        command = listen()
        if command:
            if not handle_command(command):
                break

if __name__ == "__main__":
    main()
  
