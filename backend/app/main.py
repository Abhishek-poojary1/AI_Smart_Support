from fastapi import FastAPI
from app.routes import upload, chat

app = FastAPI(title="AI Smart Support Agent")

app.include_router(upload.router, prefix="/upload")
app.include_router(chat.router, prefix="/chat")

@app.get("/")
def health():
    return {"status": "running"}
