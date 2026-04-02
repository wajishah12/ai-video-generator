import sys
from openai import OpenAI

client = OpenAI()

with open(sys.argv[1], 'r') as f:
    script = f.read()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=script,
)

response.stream_to_file("hindi_audio.mp3")
