# main.py
# This is a placeholder for the TalentMatch_AI_Recruitment application.

from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI()

@app.get("/")
def root():
    return {"message": "TalentMatch AI is live!"}

@app.post("/upload-resume/")
async def upload_resume(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

@app.get("/match")
def match_candidate(job_title: str):
    # Placeholder logic
    return {"job_title": job_title, "matched_candidate": "Jane Doe (example)"}
