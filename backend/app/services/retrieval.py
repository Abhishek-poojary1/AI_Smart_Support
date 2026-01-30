import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

VECTOR_STORE_PATH = "vector_store"

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://host.docker.internal:11434"
)



def get_db():
    if not os.path.exists(VECTOR_STORE_PATH):
        return None

    return FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


def retrieve(query: str):
    db = get_db()
    if db is None:
        return []

    return db.similarity_search(query, k=5)
