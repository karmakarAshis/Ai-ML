from google import genai
from dotenv import load_dotenv
import os

from gtts import gTTS
import io

# load env variable
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# client
client = genai.Client(api_key=api_key)

# note generator
def note_generator(images):

    prompt = """"summerize the picture in note format at max 100 words,
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text


def audio_transcription(text):

    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generator(images, difficulty):

    prompt = f"generate 4 quizes bassed on {difficulty}. make sure to add necessary markdown to differentiate different options add correct answer after the quiz"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text