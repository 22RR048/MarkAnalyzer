from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import os
import tempfile
import pandas as pd
import requests

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = './uploads'
GEMINI_API_URL = "https://api.gemini.com/v1/image-process"  # Replace with the actual Gemini endpoint


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust path if necessary

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file extensions
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'csv', 'xls', 'xlsx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def home():
    return render_template('index.html')  # Assumes index.html is in the "templates" folder

@app.route('/file-upload', methods=['POST'])
def handle_file_upload():
    if 'fileUpload' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['fileUpload']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    try:
        # Save the file to the upload folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Perform OCR if the uploaded file is an image
        if file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            return jsonify({'message': 'File uploaded and processed successfully!', 'extracted_text': text}), 200
        else:
            return jsonify({'message': 'File uploaded successfully! But no text extraction was performed.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/extract-text', methods=['POST'])
def extract_text():
    image_file = request.files.get('image')

    if not image_file:
        return jsonify({"error": "No image file provided"}), 400

    if not allowed_file(image_file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        # Save image temporarily for API usage
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = os.path.join(temp_dir, image_file.filename)
            image_file.save(temp_path)

            # Send the image to the Gemini API
            with open(temp_path, 'rb') as img_file:
                files = {'image': img_file}
                headers = {'Authorization': f'Bearer {GEMINI_API_KEY}'}
                response = requests.post(GEMINI_API_URL, files=files, headers=headers)

            # Handle Gemini API response
            if response.status_code == 200:
                result = response.json()  # Assuming the API returns JSON
                return jsonify({'message': 'File processed successfully by Gemini!', 'result': result}), 200
            else:
                return jsonify({'error': 'Failed to process image by Gemini API', 'details': response.text}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-schedule', methods=['POST'])
def generate_schedule_with_gemini():
    marks_file = request.files.get('marksFile')

    if not marks_file:
        return jsonify({"error": "No marks file provided"}), 400

    if not allowed_file(marks_file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        # Save marks file temporarily
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, marks_file.filename)
            marks_file.save(file_path)

            # Read marks file (CSV or Excel)
            if file_path.endswith('.csv'):
                marks_data = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                marks_data = pd.read_excel(file_path)
            else:
                return jsonify({"error": "Invalid file format. Please upload CSV or Excel."}), 400

            # Convert marks data to JSON format
            marks_dict = marks_data.to_dict(orient='records')

            # Call Gemini API with the marks data
            headers = {'Authorization': f'Bearer {os.environ.get('GEMINI_API_KEY')}', 'Content-Type': 'application/json'}
            response = requests.post(GEMINI_API_URL, json={"marks": marks_dict}, headers=headers)

            # Handle Gemini API response
            if response.status_code == 200:
                gemini_schedule = response.json()  # Assuming it returns JSON
                return jsonify({"message": "Study schedule generated successfully!", "schedule": gemini_schedule}), 200
            else:
                return jsonify({"error": "Failed to generate schedule with Gemini API", "details": response.text}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)