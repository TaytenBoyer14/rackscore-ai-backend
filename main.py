from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "RackScore AI Backend Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Fake scoring logic (we'll improve later)
    gross_score = random.randint(120, 190)
    deductions = random.randint(0, 15)
    net_score = gross_score - deductions

    return {
        "gross_score": gross_score,
        "deductions": deductions,
        "net_score": net_score
    }
