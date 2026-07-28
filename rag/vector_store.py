from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embeddings


def create_vector_store(chunks):

    embeddings = get_embeddings()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    return db
