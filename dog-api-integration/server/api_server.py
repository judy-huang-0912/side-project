from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import random
from fastapi.responses import JSONResponse


app = FastAPI()

# 設置允許的使用者來源
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 讀取 CSV 檔並轉換為字典列表
def read_images_from_csv():
    df = pd.read_csv("dog_images.csv")
    images = df.to_dict(orient='records')
    return images

# 隨機選取指定數量的照片
@app.get("/dog")
def get_dog_images(limit: int = 1):
    images = read_images_from_csv()
    selected_images = random.sample(images, limit)
    return selected_images

#開新的API
@app.post("/upload/")
async def upload_file(files: list[UploadFile] = File(...)):
    file_paths = []

    for file in files:
        print(file.filename)
        file_paths.append(file.filename)
    return JSONResponse(content={"file_paths": file_paths})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
#直接執行這個 Python 檔案時，會啟動伺服器，讓網頁開始運行。
