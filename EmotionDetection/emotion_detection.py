import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    raw_data = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=raw_data, headers=headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        scores = formatted_response['emotionPredictions'][0]['emotion']
        max_k, max_v = max(scores.items(), key=lambda item: item[1])
        scores['dominant_emotion'] = max_k

    elif response.status_code == 400:
        scores = {key: None for key in ['joy', 'sadness', 'fear', 'disgust', 'anger', 'dominant_emotion']}

    return scores
