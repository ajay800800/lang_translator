
# 🇮🇳 AI4Bharat Multilingual Assistant – Offline Setup

This project enables local usage of AI4Bharat models for **Indic language translation** (text → English) and **speech transcription** (voice → English), using HuggingFace models with a Flask backend and React frontend.

---

## 📦 Project Structure

```
ai4bharat-server/
├── backend/             # Flask API server
│   ├── app.py
│   ├── translator.py
│   ├── voice_transcriber.py
│   └── requirements.txt
├── frontend/            # React UI
│   ├── public/
│   ├── src/
│   └── package.json
```

---

## 🔧 Requirements

- Python ≥ 3.9
- Node.js ≥ 18
- pip + virtualenv (recommended)
- Git

---

## 🚀 Backend Setup (Flask)

```bash
# Clone the repository
git clone https://github.com/YOUR_USER/ai4bharat-server.git
cd ai4bharat-server/backend

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
# ➜ Server runs on http://localhost:6001
```

### ✅ API Endpoints

| Route         | Method | Description                          |
|---------------|--------|--------------------------------------|
| `/translate`  | POST   | Translate given text to English      |
| `/transcribe` | POST   | Convert spoken audio (.wav) to English |

---

## 🧠 Models Used

| Model Name | Task             | Hugging Face Link |
|------------|------------------|-------------------|
| `ai4bharat/indictrans2-indic-en-dist-200M` | Text → English | [IndicTrans2](https://huggingface.co/ai4bharat/indictrans2-indic-en-dist-200M) |
| `ai4bharat/indic-whisper-large-v2`         | Speech → English | (Gated) Requires HF token |

If Whisper download fails, authenticate:
```bash
huggingface-cli login
```

---

## 🌐 Frontend Setup (React)

```bash
# Open a new terminal
cd ../frontend
npm install
npm start
# ➜ React UI runs at http://localhost:3078
```

---

## 🎤 Example Usage

### Translate text
```bash
curl -X POST http://localhost:6001/translate   -H "Content-Type: application/json"   -d '{ "text": "नमस्ते" }'
```

### Transcribe audio
```bash
curl -X POST http://localhost:6001/transcribe   -F audio=@sample.wav
```

---

## ⚠️ Notes

- Audio file must be `.wav` format (mono, 16kHz recommended)
- If you get certificate/auth errors, make sure the HuggingFace model access is not restricted

---

## 🤝 Credits

- [AI4Bharat](https://ai4bharat.org)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [IndicTrans2 Paper](https://arxiv.org/abs/2304.09104)

---
