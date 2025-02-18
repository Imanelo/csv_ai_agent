import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_MODEL = "meta-llama/llama-3.3-70b-instruct"  # Choose any model from OpenRouter
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    
settings = Settings()