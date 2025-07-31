import gradio as gr
import os
import soundfile as sf
from kokoro_onnx import Kokoro
import uuid

current_dir = os.path.dirname(os.path.abspath(__file__))
kokoro = Kokoro(
    os.path.join(current_dir, "kokoro-v1.0.onnx"),
    os.path.join(current_dir, "voices-v1.0.bin")
)
voices = list(kokoro.voices.keys())

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

languages = ["en-us", "ja-jp", "zh-cn", "es-es"]

def load_txt(file_path):
    if file_path is None:
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def synthesize_text(text, voice, speed, lang):
    if not text.strip():
        return "⚠️ Please enter some text.", None, None
    try:
        samples, rate = kokoro.create(text=text, voice=voice, speed=speed, lang=lang)
        filename = f"{uuid.uuid4().hex[:8]}_{voice.replace(' ', '_')}.wav"
        filepath = os.path.join(OUTPUT_DIR, filename)
        sf.write(filepath, samples, rate)
        return f"✅ Generated: `{filename}`", filepath, filepath
    except Exception as e:
        return f"❌ Error: {str(e)}", None, None

with gr.Blocks(title="Kokoro TTS", css="""
    .gradio-container { max-width: 900px; margin: 0 auto; }
    .gr-button { width: 100%; font-size: 1.1em; }
    .output-status-box { text-align: center; padding-top: 1em; font-size: 1em; }
""") as demo:
    gr.Markdown("""
    <div align="center">
        <h1>🎙️ Kokoro TTS</h1>
        <p style="font-size: 1.1em;">Convert your text into realistic speech. Supports multiple voices, languages, and audio downloads.</p>
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Accordion("📝 Input Settings", open=True):
                input_text = gr.Textbox(
                    label="Text Input",
                    placeholder="Enter or upload text...",
                    lines=5
                )

                text_file = gr.File(
                    file_types=[".txt"],
                    label="📄 Drag & Drop a Text File",
                    type="filepath"
                )

                voice_dropdown = gr.Dropdown(
                    choices=voices,
                    label="Voice",
                    value=voices[0]
                )

                lang_dropdown = gr.Dropdown(
                    choices=languages,
                    label="Language",
                    value="en-us"
                )

                speed_slider = gr.Slider(
                    minimum=0.5,
                    maximum=2.0,
                    value=1.0,
                    step=0.1,
                    label="Speed"
                )

                btn = gr.Button("🔊 Generate Audio", variant="primary")

        with gr.Column(scale=1):
            output_audio = gr.Audio(label="Preview Output", visible=True, type="filepath")
            output_file = gr.File(label="Download WAV", visible=False)

    output_status = gr.Markdown("", elem_classes="output-status-box")

    text_file.change(fn=load_txt, inputs=text_file, outputs=input_text)

    btn.click(
        fn=synthesize_text,
        inputs=[input_text, voice_dropdown, speed_slider, lang_dropdown],
        outputs=[output_status, output_file, output_audio]
    )

    gr.Markdown("<hr><p style='text-align:center;'>📁 All generated files are saved in the <code>outputs/</code> folder.</p>")

if __name__ == "__main__":
    demo.queue()
    demo.launch(server_name="127.0.0.1", server_port=7860, show_api=False)
