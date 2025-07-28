from dotenv import load_dotenv
import os

def load_settings():
    load_dotenv()

def get_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")
