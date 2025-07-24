# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import openai, os
from dotenv import load_dotenv

load_dotenv() # Load OPENAI_API_KEY from .env

app = FastAPI()

# Enable CORS (during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, set this to your domain
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the React frontend build from the root URL
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="static")

class SummarizeRequest(BaseModel):
    text: str
    type: str # 'paragraph' or 'bullet'

class SummaryResponse(BaseModel):
    summary: str

@app.post("/api/summarize", response_model=SummaryResponse)
async def summarize(req: SummarizeRequest):
    text = req.text
    summary_type = req.type

    # Build the prompt based on the summary type
    if summary_type == "bullet":
        prompt = f"Summarize the following text into concise bullet points:\n\n{text}"
    else:
        prompt = f"Summarize the following text into a concise paragraph:\n\n{text}"

    # Load the API key securely from environment
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Call OpenAI Completion API (e.g. text-davinci-003)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()

    return SummaryResponse(summary=summary)
    if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

