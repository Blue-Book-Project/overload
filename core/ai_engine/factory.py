from config.settings import settings

def get_ai_engine():
    provider = settings.AI_PROVIDER.lower()
    
    if provider == "claude":
        from .claude import ClaudeEngine
        return ClaudeEngine()
    
    elif provider == "gpt":
        from .gpt import GPTEngine
        return GPTEngine()
    
    elif provider == "gemini":
        from .gemini import GeminiEngine
        return GeminiEngine()

    elif provider == "groq":
        from .groq_engine import GroqEngine
        return GroqEngine()
    
    else:
        raise ValueError(f"Unknown AI provider: {provider}")