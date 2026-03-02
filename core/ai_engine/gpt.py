from openai import OpenAI
from .base import BaseAIEngine
from config.settings import settings

class GPTEngine(BaseAIEngine):
    
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
    
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=4096
        )
        return response.choices[0].message.content