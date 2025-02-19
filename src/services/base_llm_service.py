from abc import ABC, abstractmethod


class BaseLLMService(ABC):
    """Abstract Base Class for LLM services"""

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate response from LLM"""
        pass

    @abstractmethod
    def get_embeddings(self, text: str):
        """Retrieve text embeddings"""
        pass
