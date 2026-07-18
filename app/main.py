from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from app.predict import predict_image
from fastapi.staticfiles import StaticFiles
import shutil
import requests
import uuid
import os

os.makedirs("uploads", exist_ok=True)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/upload")
async def upload_image(
    request: Request,
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction, confidence = predict_image(file_path)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": prediction,
            "confidence": f"{confidence:.4f}",
            "image_path": f"/uploads/{file.filename}"
        }
    )


@app.post("/api/predict")
async def api_predict(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction, confidence = predict_image(file_path)

    return {
        "prediction": prediction,
        "confidence": float(confidence),
        "image_path": f"/uploads/{file.filename}"
    }

@app.post("/api/predict-url")
async def predict_url(image_url: str):

    try:

        filename = f"uploads/{uuid.uuid4()}.jpg"

        response = requests.get(
            image_url,
            timeout=10
        )

        response.raise_for_status()

        print("Status:", response.status_code)
        print("Content-Type:", response.headers.get("content-type"))

        with open(filename, "wb") as f:
            f.write(response.content)

        prediction, confidence = predict_image(filename)

        return {
            "prediction": prediction,
            "confidence": float(confidence),
            "image_path": "/" + filename
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "error": str(e)
        }