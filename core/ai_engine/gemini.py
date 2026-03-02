from google import genai
from .base import BaseAIEngine
from config.settings import settings

class GeminiEngine(BaseAIEngine):
    
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )
    
    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text