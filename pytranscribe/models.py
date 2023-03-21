from django.db import models


def transcribe(filepath):
    import whisper
    print("Step 1")
    model = whisper.load_model("base")

    print("Step 2")
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(filepath)
    audio = whisper.pad_or_trim(audio)

    print("Step 3")
    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    print("Step 4")
    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    print("Step 5")
    # decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    tokenizer = whisper.tokenizer.get_tokenizer(
        multilingual=True,
        language="ja",
        task="transcribe")
    text = tokenizer.decode(result.tokens)
    return text
