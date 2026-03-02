from abc import ABC, abstractmethod

class BaseAIEngine(ABC):
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass