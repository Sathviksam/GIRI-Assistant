import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# === Configuration ===
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
VSCODE_PATH = r"C:\Users\sathv\AppData\Local\Programs\Microsoft VS Code\Code.exe"  # Change if different

# === Initialize TTS engine ===
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

def talk(text):
    print("🎙️ SAM:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice).lower().strip()
        print("🗣️ You said:", command)
        return command
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
    except sr.RequestError:
        talk("Network issue with Google service.")
    return ""

def run_sam():
    command = take_command()
    if not command:
        return

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)
        return

    elif "time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {current_time} ⏰")
        return

    elif "who is uday" in command:
        talk("Uday, known as uday_codes on Instagram, is a coding content creator. "
             "He teaches Python projects in Telugu and runs udaycodes.in 💻")
        return

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")
        return

    elif "joke" in command:
        talk(pyjokes.get_joke())
        return

    elif "open chrome" in command:
        if os.path.exists(CHROME_PATH):
            talk("Opening Chrome 🚀")
            os.startfile(CHROME_PATH)
        else:
            talk("Chrome path not found ")
        return

    elif "open code" in command or "vs code" in command:
        if os.path.exists(VSCODE_PATH):
            talk("Opening VS Code 💻")
            os.startfile(VSCODE_PATH)
        else:
            talk("VS Code path not found ")
        return

    elif any(word in command for word in ["bye", "exit", "stop", "quit", "see you"]):
        talk("Bye! Take care ")
        sys.exit()

    # If nothing matched
    talk("I heard you, but I don’t understand that yet 😅")

# === Start Assistant ===
if __name__ == '__main__':
    talk("Yo! I'm SAM – your personal voice assistant 💡")
    while True:
        command = take_command()
        response = handle_command(command)
        talk(response)
