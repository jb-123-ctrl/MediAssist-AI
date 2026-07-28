from rag.retriever import retrieve_context


def build_prompt(user_question):

    context, sources = retrieve_context(user_question)

    prompt = f"""
You are MediAssist AI, an educational healthcare assistant.

Use the medical context below whenever it is relevant.
If the answer is not present in the retrieved context,
state that clearly instead of inventing facts.

Medical Information

{context}

Question

{user_question}
"""

    return prompt, sources