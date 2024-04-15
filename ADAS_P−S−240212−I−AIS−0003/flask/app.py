import os
from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO

app = Flask(__name__)

# Load models
Stage_1_model = YOLO("https://colab.research.google.com/drive/162MQbm5ZvcGGc-qMltoKcBQFaqR8LDfd?usp=sharing.pt")

# Function to predict damage details
def report(img_path):

    # Checking for Damage or Non-Damage
    s1_pred = Stage_1_model.predict(img_path)

    if not os.path.exists('predictions'):
        os.makedirs('predictions')
    
    prediction_image_path = os.path.join('predictions', f"prediction_{secure_filename(img_path)}")

    # Process results list
    for result in s1_pred:
        result.save(filename = prediction_image_path)
    
    return prediction_image_path

@app.route("/")
def homepage():
    # Render the template
    return render_template("app.html")

@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['file']

    if file:
        # Ensure the UPLOAD_FOLDER exists, create it if it doesn't
        if not os.path.exists('uploaded-files'):
            os.makedirs('uploaded-files')
            
        file_path = os.path.join('uploaded-files', secure_filename(file.filename))
        file.save(file_path)

        # Call the report function to predict damage details
        prediction_image_path = report(file_path)

        # Construct response JSON data
        response_data = {
                "prediction_image_url": prediction_image_path
        }

        return jsonify(response_data), 200
        
    else:
        return jsonify("Invalid file format"), 400

@app.route('/predictions/<path:filename>')
def get_prediction_image(filename):
    return send_from_directory('predictions', filename)

if __name__ == "__main__":
    app.run()