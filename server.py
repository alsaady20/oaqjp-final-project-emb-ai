"""Flask web app for emotion detection"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main HTML page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Handle emotion detection requests and return formatted result.
    """
    text_to_analyze = request.values.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted = (
        f"For the given statement, the system response is "
        f"'anger': {result['emotion_scores']['anger']}, "
        f"'disgust': {result['emotion_scores']['disgust']}, "
        f"'fear': {result['emotion_scores']['fear']}, "
        f"'joy': {result['emotion_scores']['joy']}, "
        f"and 'sadness': {result['emotion_scores']['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted

if __name__ == '__main__':
    app.run(debug=True, port=5000)
