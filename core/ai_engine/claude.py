import anthropic
from .base import BaseAIEngine
from config.settings import settings

class ClaudeEngine(BaseAIEngine):
    
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=settings.ANTHROPIC_API_KEY
        )
    
    def generate(self, prompt: str) -> str:
        message = self.client.messages.create(
            model="claude-opus-4-6",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content[0].text