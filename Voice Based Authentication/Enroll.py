import sounddevice as sd
from scipy.io.wavfile import write
from utils import extract_features, save_user_features

def record_voice(filename, duration=5, fs=44100):
    print("Recording... Speak now!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Recording complete.")

def enroll_user():
    username = input("Enter username for enrollment: ")
    filename = f"{username}_enroll.wav"
    record_voice(filename)
    features = extract_features(filename)
    save_user_features(username, features)
    print(f"User '{username}' enrolled successfully.")

if __name__ == "__main__":
    enroll_user()
  
