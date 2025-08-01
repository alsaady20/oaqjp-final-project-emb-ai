class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am very happy and joyful today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I hate working long hours.")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        result = emotion_detector("I feel really down and depressed.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am scared of the dark and the noises outside.")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_disgust(self):
        result = emotion_detector("That meal was disgusting and made me sick.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

unittest.main()