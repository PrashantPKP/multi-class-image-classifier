# 🖼️ Intel Image Classification Web Application

## 📌 Overview

This project is an end-to-end Deep Learning Image Classification Web Application built using **TensorFlow, FastAPI, HTML, CSS, JavaScript, and Docker**.

The application allows users to upload an image through a web interface and receive a predicted scene category along with the model confidence score.

The model was trained using **Transfer Learning** on the Intel Image Classification dataset and deployed as a production-ready web application.

---

## 🚀 Features

* Upload images directly from the browser
* Real-time image preview
* Deep Learning image classification
* Confidence score prediction
* FastAPI backend API
* Responsive web interface
* Docker containerization
* Error handling and loading indicators
* Production-ready project structure

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
HTML/CSS/JavaScript
 │
 ▼
FastAPI Backend
 │
 ▼
predict.py
 │
 ▼
TensorFlow Model (.keras)
 │
 ▼
Prediction + Confidence
 │
 ▼
JSON Response
 │
 ▼
Frontend Display
```

---

## 📂 Project Structure

```text
intel-image-classification/
│
├── app/
│   ├── main.py
│   ├── predict.py
│
├── models/
│   └── intel_image_classification_model.keras
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

## 🧠 Model Information

### Classes

The model predicts the following scene categories:

* Buildings
* Forest
* Glacier
* Mountain
* Sea
* Street

### Model Type

* Transfer Learning
* TensorFlow / Keras
* Saved as `.keras` model

---

## 🛠️ Tech Stack

### Machine Learning

* TensorFlow
* NumPy
* Pillow

### Backend

* FastAPI
* Uvicorn

### Frontend

* HTML5
* CSS3
* JavaScript

### Deployment

* Docker
* WSL2

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/intel-image-classification.git

cd intel-image-classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t intel-image-classifier .
```

### Run Docker Container

```bash
docker run -p 8000:8000 intel-image-classifier
```

Open:

```text
http://localhost:8000
```

---

## 🔌 API Endpoint

### Predict Image

```http
POST /api/predict
```

### Request

Multipart Form Data:

```text
file = image.jpg
```

### Response

```json
{
    "prediction": "forest",
    "confidence": 0.9999,
    "image_path": "/uploads/forest.jpg"
}
```

---

## ⚙️ Requirements

```text
fastapi==0.122.0
uvicorn==0.38.0
tensorflow==2.21.0
Jinja2==3.1.6
python-multipart==0.0.20
numpy==2.2.5
pillow==11.2.1
```

---

## 🎯 Future Improvements

* Cloud Deployment (Render/AWS/Azure)
* Authentication System
* Batch Image Prediction
* Model Monitoring
* CI/CD Pipeline
* GPU Deployment
* Kubernetes Deployment

---

## 👨‍💻 Author

**Sudhanshu Narayane**

* GitHub: https://github.com/Sido-dev
* LinkedIn: https://linkedin.com/in/sid101110

---

## ⭐ If you found this project useful, consider giving it a star.
