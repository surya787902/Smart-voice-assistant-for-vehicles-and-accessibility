import librosa
import numpy as np
import pickle

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

def save_user_features(username, features):
    with open(f"users/{username}.pkl", "wb") as f:
        pickle.dump(features, f)

def load_user_features(username):
    try:
        with open(f"users/{username}.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None
      
