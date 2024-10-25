from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import random
import sqlite3
from fastapi.responses import JSONResponse


app = FastAPI()
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
def read_images_from_sqlite(limit: int = 1):
    connection = sqlite3.connect("images.db")
    query = f"SELECT * FROM images LIMIT {limit};"  # 使用 LIMIT 限制查詢結果數量
    df = pd.read_sql_query(query, connection)
    connection.close()
    images = df.to_dict(orient='records')
    return images

@app.get("/dog")
def get_dog_images(limit: int = 1):
    images = read_images_from_sqlite(limit)
    return images


@app.post("/upload/")
async def upload_file(files: list[UploadFile] = File(...)):
    file_paths = []

    for file in files:
        print(file.filename)
        file_paths.append(file.filename)
    return JSONResponse(content={"file_paths": file_paths})
