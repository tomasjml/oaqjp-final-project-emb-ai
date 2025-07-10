from flask import Flask, request, jsonify, make_response

from EmotionDetection.emotion_detection import emotion_detector, EmotionResponse

app = Flask(__name__)

@app.route('/emotionDetector')
def get_emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    print(res)
    print(type(res))
    print(EmotionResponse.dominant_emotion)
    if res.get("dominant_emotion") is None:
        return make_response("Invalid text! Please try again!\n", 400)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
