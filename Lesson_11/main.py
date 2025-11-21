#sk_3c19c43bf1696a81ea1ca79e1bc01ee0e116ce012cd9ae41
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="sk_3c19c43bf1696a81ea1ca79e1bc01ee0e116ce012cd9ae41"
)

for voice in client.voices.search(include_total_count=True).voices:
    print(voice.voice_id, voice.name)

audio = client.text_to_speech.convert(
    text="Я запізнився на пару через відсутність світла.",
    voice_id="9BWtsMINqrJLrRacOk9x",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

with open("audio.mp3", "wb") as f:
    for a in audio:
        f.write(a)