from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import random

app = FastAPI()

# 設置允許的源（你可以根據需要修改這個列表）
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 讀取 CSV 檔案並轉換為字典列表
def read_images_from_csv():
    df = pd.read_csv("dog_images.csv")
    images = df.to_dict(orient='records')
    return images

@app.get("/dog")
def get_dog_images(limit: int = 1):
    images = read_images_from_csv()
    # 隨機選取指定數量的照片
    selected_images = random.sample(images, limit)
    return selected_images

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
