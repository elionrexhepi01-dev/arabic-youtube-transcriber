import os
import sys

# Suppress Hugging Face symlink warnings
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Add NVIDIA DLL directories directly to the system PATH so CTranslate2 can locate them
site_packages = os.path.dirname(sys.executable) + r"\Lib\site-packages"
cublas_bin = os.path.join(site_packages, "nvidia", "cublas", "bin")
cudnn_bin = os.path.join(site_packages, "nvidia", "cudnn", "bin")
os.environ["PATH"] = cublas_bin + os.pathsep + cudnn_bin + os.pathsep + os.environ["PATH"]

from faster_whisper import WhisperModel

# Switch to the large-v3 model for maximum transcription accuracy
model_size = "large-v3"

model = WhisperModel(model_size, device="cuda", compute_type="float16")

segments, info = model.transcribe("lesson1.wav", language="ar", task="transcribe")

# Save output with timestamps to a text file
with open("lesson1.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        line = f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}"
        print(line)
        f.write(line + "\n")

print("Transcription complete!")