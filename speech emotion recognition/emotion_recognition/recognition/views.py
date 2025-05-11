import os
import librosa
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import joblib

# Load the trained model
model = joblib.load('emotion_recognition_model.joblib')

# Feature extraction function
def extract_features(file_path):
    audio, sr = librosa.load(file_path, duration=3, offset=0.5)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

# Emotion prediction function
def get_emotion_from_filename(file_name):
    emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'ps', 'sad', 'surprise']
    for emotion in emotions:
        if emotion in file_name.lower():
            return emotion
    return None

# Handle file upload and emotion prediction
def upload_file(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        audio_file = request.FILES['audio_file']
        fs = FileSystemStorage()
        file_path = fs.save(audio_file.name, audio_file)
        file_url = fs.url(file_path)

        # Extract features from the uploaded audio file
        features = extract_features(file_path)
        prediction = model.predict([features])
        emotion = prediction[0]

        # Render the result in the template
        return render(request, 'result.html', {'emotion': emotion, 'file_url': file_url})

    return render(request, 'index.html')

