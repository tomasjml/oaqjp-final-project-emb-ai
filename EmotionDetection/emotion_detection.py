import json
import requests


def return_as_json(raw):
    try:
        return json.dumps(raw, indent=2)
    except TypeError as e:
        print(f"Error converting to JSON: {e}")
        return None


def transform_emotion_response(response):
    list_of_emotions = []
    for emotion in response["emotionPredictions"]:
        list_of_emotions.append(emotion["emotion"])
    return list_of_emotions


def print_as_json(raw):
    json_data = return_as_json(raw)
    if json_data:
        print(json_data)
    else:
        print("Failed to convert data to JSON format.")

def get_dominant_emotions(emotions):
    if not emotions:
        return None

    dominant_emotion = max(emotions, key=lambda x: x['joy'])
    return {
        'anger': dominant_emotion['anger'],
        'disgust': dominant_emotion['disgust'],
        'fear': dominant_emotion['fear'],
        'joy': dominant_emotion['joy'],
        'sadness': dominant_emotion['sadness'],
        'dominant_emotion': max(dominant_emotion, key=dominant_emotion.get)
    }

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {"raw_document": {"text": str(text_to_analyze)}}

    try:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        response_formatted = response.json()
        response_emotions = transform_emotion_response(response_formatted)
        return get_dominant_emotions(response_emotions)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None