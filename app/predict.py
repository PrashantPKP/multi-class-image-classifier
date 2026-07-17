import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model once when application starts
model = tf.keras.models.load_model("models/intel_image_classification_model.keras")

CLASS_NAMES = [
    "buildings",
    "forest",
    "glacier",
    "mountain",
    "sea",
    "street"
]

def predict_image(img_path):

    img = image.load_img(
        img_path,
        target_size=(168, 168)  # Replace with your training size
    )

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    predicted_class = CLASS_NAMES[np.argmax(prediction)]

    confidence = np.max(prediction)

    return predicted_class, confidence