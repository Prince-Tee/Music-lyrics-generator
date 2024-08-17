import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_lyrics(audio_data):
    # Use audio_data to create a prompt or use a pre-defined prompt
    prompt = "Generate lyrics based on this music."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()
