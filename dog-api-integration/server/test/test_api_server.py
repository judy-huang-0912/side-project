import unittest
import requests

class TestDogAPI(unittest.TestCase):
    def test_dog_images(self):
        # 設定測試用的 URL
        url = "http://127.0.0.1:8000/dog?limit=3"

        # 發送 GET 請求
        response = requests.get(url)

        # 確認請求成功（HTTP 狀態碼 200）
        self.assertEqual(response.status_code, 200)

        # 解析 JSON 響應
        data = response.json()

        # 確認返回的圖片數量是否為 3
        self.assertEqual(len(data), 2)

        # 可以進一步確認返回的每張圖片的格式或其他屬性，視情況而定
        for image in data:
            self.assertIn("url", image)
            self.assertIn("width", image)
            self.assertIn("height", image)

if __name__ == "__main__":
    unittest.main()


