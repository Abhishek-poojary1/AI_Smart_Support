from langchain_ollama import ChatOllama



llm = ChatOllama(
    model="llama3",
    base_url="http://host.docker.internal:11434",
    temperature=0
)
def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are an AI support assistant.

Answer ONLY using the context below.
If the answer is not present, say:
"I don't know. This document does not mention it."

Context:
{context}

Question:
{question}
"""
    return llm.invoke(prompt).content.strip()


# def llm_confidence_check(context: str, answer: str) -> bool:
#     prompt = f"""
# Is the following answer fully supported by the given context?
# Answer ONLY YES or NO.

# Context:
# {context}

# Answer:
# {answer}
# """
#     result = llm.invoke(prompt).content.strip().upper()
#     return "YES" in result
def calculate_confidence(docs_count: int, safe_refusal: bool) -> float:
    # Safe refusal is GOOD behavior
    if safe_refusal:
        return 0.7

    if docs_count >= 4:
        return 0.85
    if docs_count >= 2:
        return 0.7
    if docs_count == 1:
        return 0.55

    return 0.3
