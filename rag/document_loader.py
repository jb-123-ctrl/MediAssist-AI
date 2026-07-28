from langchain_community.document_loaders import TextLoader


def load_documents():

    loader = TextLoader(
        "data/medical_docs/healthcare_knowledge.txt",
        encoding="utf-8"
    )

    return loader.load()
