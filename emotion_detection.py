import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {"raw_document": {"text": str(text_to_analyze)}}

    try:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        formatted_response = response.json()
        print(response.status_code)
        print(formatted_response)
        return formatted_response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

print(emotion_detector("I love this new technology."))
