print("Loaded memory.py")


def initialize_memory(session_state):
    """Initialize conversation history."""

    if "messages" not in session_state:
        session_state.messages = []


def add_message(session_state, role, content):
    """Add one message to the conversation."""

    session_state.messages.append({
        "role": role,
        "content": content
    })


def get_chat_history(session_state):
    """Return chat history."""

    return session_state.get("messages", [])
