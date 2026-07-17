from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates

from app.predict import predict_image

import shutil

from fastapi.staticfiles import StaticFiles

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
