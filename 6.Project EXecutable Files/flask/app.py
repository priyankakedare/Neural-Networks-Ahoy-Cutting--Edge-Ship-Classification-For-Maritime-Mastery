from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the trained model
model = load_model('vgg16-ship-classification (2).h5')

# Mock classification classes (replace with actual model and classes)
classes = ['Cargo Ship', 'Carrier Ship', 'Cruise Ship', 'Military Ship', 'Tanker Ship']

def preprocess_image(image):
    image = image.resize((224, 224))
    img_array = np.asarray(image)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            image = Image.open(io.BytesIO(file.read()))
            processed_image = preprocess_image(image)

            # Perform prediction using the loaded model
            prediction = model.predict(processed_image)
            predicted_label = classes[np.argmax(prediction)]
            
            return render_template('prediction.html', prediction=predicted_label)

    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=False)
