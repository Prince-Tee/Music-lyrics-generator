import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("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")

def generate_lyrics(audio_data):
    # Use audio_data to create a prompt or use a pre-defined prompt
    prompt = "Generate lyrics based on this music."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()
