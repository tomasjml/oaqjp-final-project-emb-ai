from EmotionDetection.emotion_detection import emotion_detector, print_as_json

sentence_1 = "I love this new technology."
print(f"Sentence 1: {sentence_1}")
emotions_1 = emotion_detector(sentence_1)
print_as_json(emotions_1)

sentence_2 = "I hate working long hours"
print(f"Sentence 2: {sentence_2}")
emotions_2 = emotion_detector(sentence_2)
print_as_json(emotions_2)