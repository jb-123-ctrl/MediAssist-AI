CARDIAC = [
    "chest pain",
    "heart attack",
    "heart pain"
]

BREATHING = [
    "difficulty breathing",
    "can't breathe",
    "cannot breathe",
    "shortness of breath",
    "not breathing"
]

NEURO = [
    "stroke",
    "seizure",
    "unconscious",
    "passed out"
]

BLEEDING = [
    "heavy bleeding",
    "bleeding heavily",
    "severe burn"
]

POISON = [
    "poison",
    "poisoning",
    "overdose",
    "suicide",
    "suicidal"
]

EMERGENCY_KEYWORDS = (
    CARDIAC +
    BREATHING +
    NEURO +
    BLEEDING +
    POISON
)


def is_emergency(user_input):
    """
    Return True when an emergency symptom pattern is detected.
    """

    user_input = user_input.lower()
    return any(keyword in user_input for keyword in EMERGENCY_KEYWORDS)


EMERGENCY_MESSAGE = """
🚨 **Potential Medical Emergency**

The symptoms you described may require immediate medical attention.

- Call your local emergency services.
- Visit the nearest emergency department.
- Contact a qualified healthcare professional immediately.

This chatbot cannot diagnose or treat emergencies.
"""
