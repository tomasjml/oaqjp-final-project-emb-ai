"""Server module for the emotion detection API.

This module sets up a Flask web server that exposes an endpoint for detecting emotions in text.
"""

from flask import Flask, request, jsonify, make_response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def get_emotion_detection():
    """Handles GET requests for emotion detection.

    Expects a 'textToAnalyze' query parameter in the request.
    Returns a JSON response with emotion analysis or a 400 error if input is invalid.
    """
    # Retrieve the text to analyze from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    # Call the emotion detector function to analyze the text
    res = emotion_detector(text_to_analyze)
    # Check if the dominant emotion is present in the result
    if res.get("dominant_emotion") is None:
        # Return a 400 error if the input is invalid or no emotion detected
        return make_response("Invalid text! Please try again!\n", 400)
    # Return the emotion analysis as a JSON response
    return jsonify(res)

if __name__ == "__main__":
    # Start the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)
