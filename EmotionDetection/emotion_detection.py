import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {"text": text_to_analyze}
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Convert response to JSON
        response_dict = response.json()

        try:
            emotions = response_dict['emotionPredictions'][0]['emotion']
        except (KeyError, IndexError):
            return {"message": "No emotions detected"}

        emotion_scores = {
            "anger": emotions.get('anger', 0),
            "disgust": emotions.get('disgust', 0),
            "fear": emotions.get('fear', 0),
            "joy": emotions.get('joy', 0),
            "sadness": emotions.get('sadness', 0)
        }

        # Determine the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the final output in the required format
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

    else:
        return f"Error: {response.status_code}"

