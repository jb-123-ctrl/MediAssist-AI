from rag.document_loader import load_documents
from rag.text_splitter import split_documents
from rag.vector_store import create_vector_store

# Build vector database only once
documents = load_documents()
chunks = split_documents(documents)
db = create_vector_store(chunks)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

def retrieve_context(question):
    """
    Retrieve the most relevant chunks for the user's question.
    """
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown")
        if source not in sources:
            sources.append(source)

    return context, sources