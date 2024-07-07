import requests
import os
from dotenv import load_dotenv

# 載入 .env 文件中的環境變數
load_dotenv()

# 讀取環境變數
LINE_TOKEN = os.getenv('LINE_TOKEN')

def line_notify(msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + LINE_TOKEN
    }
    data = {
        'message': msg,
        "stickerPackageId": 6370,  # 貼圖包ID
        "stickerId": 11088018  # 貼圖ID
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Line Notify 成功")
    else:
        print(f"Line Notify 失敗: {response.status_code}, {response.text}")
