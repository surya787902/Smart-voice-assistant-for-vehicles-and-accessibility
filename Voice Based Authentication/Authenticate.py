import sounddevice as sd
from scipy.io.wavfile import write
from utils import extract_features, load_user_features
import numpy as np

def record_voice(filename, duration=5, fs=44100):
    print("Speak for authentication...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Recording complete.")

def authenticate_user():
    username = input("Enter username to authenticate: ")
    stored_features = load_user_features(username)
    if stored_features is None:
        print("User not found.")
        return

    filename = f"{username}_auth.wav"
    record_voice(filename)
    new_features = extract_features(filename)

    similarity = np.linalg.norm(stored_features - new_features)
    print(f"Similarity score: {similarity:.2f}")

    if similarity < 30:  # Adjust threshold as needed
        print("Authentication successful!")
    else:
        print("Authentication failed!")

if __name__ == "__main__":
    authenticate_user()
  
