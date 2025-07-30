from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransToolkit.processor import IndicProcessor

app = Flask(__name__)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load IndicTrans2 model
MODEL_NAME = "ai4bharat/indictrans2-indic-en-dist-200M"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME, trust_remote_code=True).to(DEVICE)
ip = IndicProcessor(inference=True)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(force=True)
    text = data.get("text", "")
    src = data.get("src", "hin_Deva")
    tgt = data.get("tgt", "eng_Latn")

    # Preprocess + Translate
    batch = ip.preprocess_batch([text], src_lang=src, tgt_lang=tgt)
    inputs = tokenizer(batch, padding=True, return_tensors="pt").to(DEVICE)
    outputs = model.generate(
    **inputs,
    max_length=256,
    use_cache=False,
    num_beams=5
)

    decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    translated = ip.postprocess_batch(decoded, lang=tgt)[0]

    return jsonify({"translated": translated})


if __name__ == "__main__":
    app.run(port=6001)
