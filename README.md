# 🎙️ Kokoro TTS - Gradio Text-to-Speech App

Kokoro TTS Simple Gradio UI is a local Gradio web app that converts custom text into realistic speech using the Kokoro ONNX model. Supports multiple voices, languages, speed control, and audio file downloads.

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/jdyson-alt4code/TTS-Kokoro-Gradio-Script.git]
cd kokoro-tts-simple-gradio-ui
```

### 2. Create and activate a virtual environment (recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Required Model Files

Download and place the following two files in the same directory as `gradiotts.py`:

- [kokoro-v1.0.onnx](https://github.com/nazdridoy/kokoro-tts/releases/download/v1.0.0/kokoro-v1.0.onnx)
- [voices-v1.0.bin](https://github.com/nazdridoy/kokoro-tts/releases/download/v1.0.0/voices-v1.0.bin)

---

## 🚀 Run the App

```bash
python gradiotts.py
```

The app will open in your browser at:

```
http://127.0.0.1:7860
```
## 📁 File Structure

```
kokoro-tts-simple-gradio-ui/
├── gradiotts.py
├── kokoro-v1.0.onnx
├── voices-v1.0.bin
├── outputs/
├── requirements.txt
└── README.md
```
