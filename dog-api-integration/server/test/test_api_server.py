import unittest
import requests

class TestDogAPI(unittest.TestCase):
    def test_dog_images(self):
        url = "http://127.0.0.1:8000/dog?limit=3"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        for image in data:
            self.assertIn("url", image)
            self.assertIn("width", image)
            self.assertIn("height", image)
if __name__ == "__main__":
    unittest.main()


