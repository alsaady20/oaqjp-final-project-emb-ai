import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=input_json, timeout=60)

    if response.status_code == 400:
        return {
            "emotion_scores": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None
            },
            "dominant_emotion": None
        }

    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    result = response.json()
    emotion_predictions = result.get("emotionPredictions", [])
    if not emotion_predictions:
        return {"error": "No emotion predictions found"}

    emotion_scores = emotion_predictions[0].get("emotion", {})
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "emotion_scores": emotion_scores,
        "dominant_emotion": dominant_emotion
    }
