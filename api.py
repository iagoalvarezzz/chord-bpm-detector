from fastapi import FastAPI, UploadFile
import tempfile, shutil, os
from chord_bpm_detector.analyze import analyze_audio

app = FastAPI(title="chord-bpm-detector API")

@app.get("/health")
def health():
  return {"status": "ok"}

@app.post("/analyze")
async def analyze_endpoint(file: UploadFile):
  suffix = os.path.splitext(file.filename or "")[1] or ".wav"
  with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
    shutil.copyfileobj(file.file, tmp)
    tmp_path = tmp.name
  try: 
    result = analyze_audio(tmp_path)
  finally: 
    os.remove(tmp_path)
  return result  
