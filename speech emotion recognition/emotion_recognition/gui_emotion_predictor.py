import tkinter as tk
from tkinter import filedialog, messagebox
import librosa
import numpy as np
import joblib
import os

# Load the model
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'emotion_recognition_model.joblib')


def extract_features(file_path):
    audio, sr = librosa.load(file_path, duration=3, offset=0.5)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def predict_emotion(file_path):
    try:
        model = joblib.load(MODEL_PATH)
        features = extract_features(file_path)
        prediction = model.predict([features])
        return prediction[0]
    except Exception as e:
        return f"Error: {str(e)}"

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        emotion = predict_emotion(file_path)
        result_label.config(text=f"Predicted Emotion: {emotion}")

# GUI
root = tk.Tk()
root.title("Speech Emotion Recognition")
root.geometry("400x200")

label = tk.Label(root, text="Click below to choose a WAV file for emotion prediction.", wraplength=350, font=("Arial", 12))
label.pack(pady=20)

browse_button = tk.Button(root, text="Browse Audio File", command=browse_file, font=("Arial", 10))
browse_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()
