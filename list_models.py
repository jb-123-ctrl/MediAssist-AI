from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("=" * 80)

for model in client.models.list():

    print(model.name)

    try:
        print(model.supported_actions)
    except:
        pass

    print("=" * 80)