from pydub import AudioSegment

def process_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    # Here you can add processing logic, e.g., extracting features
    return audio
