from flask import Flask, request, jsonify, make_response

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def get_emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        res = make_response(jsonify(emotion_detector(text_to_analyze)))
        res.status_code = 400
        return res
    return jsonify(emotion_detector(text_to_analyze))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
