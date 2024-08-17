import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from .audio_processing import process_audio
from .lyrics_generation import generate_lyrics

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        # Process the file and generate lyrics
        audio_data = process_audio(file_path)
        lyrics = generate_lyrics(audio_data)
        
        return render_template('lyrics.html', lyrics=lyrics)
