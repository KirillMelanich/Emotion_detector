from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        if isinstance(result, dict) and 'dominant_emotion' in result:
            response = (f"For the given statement, the system response is "
                        f"'anger': {result['anger']}, "
                        f"'disgust': {result['disgust']}, "
                        f"'fear': {result['fear']}, "
                        f"'joy': {result['joy']}, "
                        f"'sadness': {result['sadness']}. "
                        f"The dominant emotion is {result['dominant_emotion']}.")
            return response
        else:
            return "Error in processing the emotion detection."
    else:
        return "No text provided for analysis."


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    