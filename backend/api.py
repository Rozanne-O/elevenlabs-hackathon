from fastapi import FastAPI3 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cohere
from elevenlabs import generate, set_api_key
import openai

app = FastAPI()

origins = ['http://localhost:3000/']


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AUDIOS_PATH = "frontend/src/audios/"
AUDIO_PATH = "/audios/"

@app.get("/voice/{query}")
async def voice_over(query: str):
    set_api_key("95aef95748c1b54c5237ec67685ab53a")

    audio_path = f'{AUDIOS_PATH}{query[:4]}.mp3'
    file_path = f'{AUDIO_PATH}{query[:4]}.mp3'

    audio = generate(
        text=query,
        voice='Bella',  # premade voice
        model="eleven_monolingual_v1"
    )

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return file_path

    except Exception as e:
        print(e)

        return ""
    
@app.get("/voice/{query}")
async def voice_over(query: str):
    set_api_key("95aef95748c1b54c5237ec67685ab53a")

    audio_path = f'{AUDIOS_PATH}{query[:4]}.mp3'
    file_path = f'{AUDIO_PATH}{query[:4]}.mp3'

    audio = generate(
        text=query,
        voice='Bella',  # premade voice
        model="eleven_monolingual_v1"
    )

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return file_path

    except Exception as e:
        print(e)

        return ""
    
@app.get("/chat/chatgpt/{query}")
def chat_chatgpt(query: str):
    openai.api_key = "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"   

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query}
            ]
        )

        return response['choices'][0]['message']['content']

    except Exception as e:
        print(e)

        return ""
    

    