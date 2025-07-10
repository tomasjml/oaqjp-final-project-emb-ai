import json
from dataclasses import dataclass, asdict
from typing import Optional

import requests


def to_dict():
    return __dict__().copy()

@dataclass
class EmotionResponse:
    anger: Optional[float] = None
    disgust: Optional[float] = None
    fear: Optional[float] = None
    joy: Optional[float] = None
    sadness: Optional[float] = None
    dominant_emotion: Optional[str] = None

    def to_dict(self):
        return asdict(self)


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
        return EmotionResponse()
    dominant_emotion = max(emotions, key=lambda x: x.get("joy", 0))
    fields = ["anger", "disgust", "fear", "joy", "sadness"]
    dom = max(fields, key=lambda f: dominant_emotion.get(f, float('-inf')))
    return EmotionResponse(
        anger=dominant_emotion.get("anger"),
        disgust=dominant_emotion.get("disgust"),
        fear=dominant_emotion.get("fear"),
        joy=dominant_emotion.get("joy"),
        sadness=dominant_emotion.get("sadness"),
        dominant_emotion=dom
    )


# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {"raw_document": {"text": str(text_to_analyze)}}
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 400:
        return EmotionResponse().to_dict()

    response_emotions = transform_emotion_response(response.json())
    result = get_dominant_emotions(response_emotions)
    return result.to_dict()