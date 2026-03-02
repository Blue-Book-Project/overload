from groq import Groq
from .base import BaseAIEngine
from config.settings import settings

class GroqEngine(BaseAIEngine):
    
    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )
    
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=4096
        )
        return response.choices[0].message.content