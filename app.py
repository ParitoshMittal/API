from flask import Flask, request, jsonify, send_file
import os
import random
import time

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\parit\OneDrive\Desktop\Code\API\Upload'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to get a random image from the 'Images' folder
def get_random_image():
    images_folder = r'C:\Users\parit\OneDrive\Desktop\Code\API\Images'
    images = os.listdir(images_folder)
    random_image = random.choice(images)
    return os.path.join(images_folder, random_image)

# Create a list to store uploaded image paths
uploaded_images = []

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the uploaded file to the UPLOAD_FOLDER
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Add the uploaded file path to the list
        uploaded_images.append(file_path)
        return jsonify({'message': 'File uploaded successfully'})

@app.route('/recive', methods=['POST'])
def random_image():
    
    # Get a random image from the 'Images' folder
    random_image_path = get_random_image()

    # Return the random image
    return send_file(random_image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
