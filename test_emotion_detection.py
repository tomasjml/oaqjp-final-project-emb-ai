# Test Cases
# Statement	Dominant Emotion
# I am glad this happened	joy
# I am really mad about this	anger
# I feel disgusted just hearing about this	disgust
# I am so sad about this	sadness
# I am really afraid that this will happen	fear
import unittest
from EmotionDetection.emotion_detection import emotion_detector, print_as_json

class TestEmotionDetection(unittest.TestCase):
    def test_positive_emotion(self):
        sentence = "I am glad this happened"
        print(f"Testing: {sentence}")
        emotions = emotion_detector(sentence)
        print_as_json(emotions)
        self.assertIsNotNone(emotions)
        self.assertEqual(emotions['dominant_emotion'], 'joy')

    def test_negative_emotion(self):
        sentence = "I am really mad about this"
        print(f"Testing: {sentence}")
        emotions = emotion_detector(sentence)
        print_as_json(emotions)
        self.assertIsNotNone(emotions)
        self.assertEqual(emotions['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        sentence = "I feel disgusted just hearing about this"
        print(f"Testing: {sentence}")
        emotions = emotion_detector(sentence)
        print_as_json(emotions)
        self.assertIsNotNone(emotions)
        self.assertEqual(emotions['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        sentence = "I am so sad about this"
        print(f"Testing: {sentence}")
        emotions = emotion_detector(sentence)
        print_as_json(emotions)
        self.assertIsNotNone(emotions)
        self.assertEqual(emotions['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        sentence = "I am really afraid that this will happen"
        print(f"Testing: {sentence}")
        emotions = emotion_detector(sentence)
        print_as_json(emotions)
        self.assertIsNotNone(emotions)
        self.assertEqual(emotions['dominant_emotion'], 'fear')
