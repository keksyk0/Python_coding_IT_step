from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="sk_e5ec946848cb51784cc61cf88159b6903cb327f1a46545eb"
)

for voice in client.voices.search(include_total_count=True).voices:
    print(voice.voice_id, voice.name)

audio = client.text_to_speech.convert(
    text="Мені дуже сподобався предмет\"Штучний інтелект і великі дані - 2020\". Дякую за все, було дуже цікаво!",
    voice_id="9BWtsMINqrJLrRacOk9x",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

with open("audio.mp3", "wb") as f:
    for a in audio:
        f.write(a)
