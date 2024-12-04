''' 
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    This function receives text input from the user, analyzes the emotions using 
    the emotion_detector function, and returns a formatted response with emotion scores.
    """
    # Retrieve the text input from the query string
    text_to_anlayze = request.args.get('textToAnalyze')

    # Get the emotion scores from the emotion detector
    response = emotion_detector(text_to_anlayze)

    # Extract individual emotion scores
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # If no dominant emotion is detected, return a message to try again
    if dominant_emotion is None:
        return "Please try again!"

    # Return a formatted responses with emotion scores
    return f"For the given statement, the system response is 'anger': {anger_score}, \
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and \
    'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    This function renders the index page of the Emotion Detector application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
