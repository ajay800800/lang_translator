# # backend/voice_transcriber.py
# import torch
# from transformers import WhisperProcessor, WhisperForConditionalGeneration
# import torchaudio

# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# model_id = f"ai4bharat/indic-wav2vec-{lang}"

# processor = WhisperProcessor.from_pretrained(MODEL_NAME)
# model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME).to(DEVICE)

# def transcribe_audio(file_path: str):
#     # Load and resample audio to 16000 Hz
#     waveform, sample_rate = torchaudio.load(file_path)
#     if sample_rate != 16000:
#         resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
#         waveform = resampler(waveform)

#     # Mono
#     if waveform.shape[0] > 1:
#         waveform = torch.mean(waveform, dim=0, keepdim=True)

#     input_features = processor(
#         waveform.squeeze(), sampling_rate=16000, return_tensors="pt"
#     ).input_features.to(DEVICE)

#     predicted_ids = model.generate(input_features)
#     transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

#     return transcription
# voice_transcriber.py
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import soundfile as sf

LANG = "hi"
MODEL_ID = f"ai4bharat/indic-wav2vec-{LANG}"

processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
model.eval()

def transcribe_audio(file_path):
    audio, sr = sf.read(file_path)
    if sr != 16000:
        raise ValueError("Audio must be 16 kHz WAV")
    input_values = processor(audio, sampling_rate=sr, return_tensors="pt").input_values
    with torch.no_grad():
        logits = model(input_values).logits
    pred_ids = torch.argmax(logits, dim=-1)
    return processor.decode(pred_ids[0])
