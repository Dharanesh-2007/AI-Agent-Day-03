import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("MODEL")
API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def banner(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)