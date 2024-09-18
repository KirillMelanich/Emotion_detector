"""
This module implements a Flask web application that uses
emotion detection on input text via the Watson NLP library.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page with the input form."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Process the input text and return the emotion detection result.
    
    This route expects a GET request with 'textToAnalyze' as a query parameter.
    It uses the Watson NLP 'emotion_detector' to analyze the text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        if isinstance(result, dict):
            if result.get("dominant_emotion") is None:
                return "Invalid text! Please try again!"
            response = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, "
                f"'joy': {result['joy']}, "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
            return response
        return "Error in processing the emotion detection."

    return "Invalid text! Please try again!."


if __name__ == "__main__":
    app.run(debug=True, port=5000)
