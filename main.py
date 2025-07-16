
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from extract import extract_invoice

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/invoice")
async def process_invoice(file: UploadFile = File(...)):
    contents = await file.read()
    result = extract_invoice(contents)
    return result
