from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retrieval import retrieve
from app.services.llm import generate_answer
from app.services.confidence import calculate_confidence

router = APIRouter()

CONFIDENCE_THRESHOLD = 0.5


class ChatRequest(BaseModel):
    query: str


@router.post("/")
def chat(request: ChatRequest):
    docs = retrieve(request.query)

    if not docs:
        return {
            
            "answer": "No documents are indexed yet. Please upload a document first.",
            "confidence": 0.0,
            "escalate_to_human": True
        }
                                                                                                                                                                                                                                                    
    context = "\n".join([d.page_content for d in docs])
    answer = generate_answer(context, request.query)

    safe_refusal = "i don't know" in answer.lower()

    confidence = calculate_confidence(
        docs_count=len(docs),
        safe_refusal=safe_refusal
    )

    return {
        "answer": answer,
        "confidence": round(confidence, 2),
        "escalate_to_human": confidence < CONFIDENCE_THRESHOLD
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
