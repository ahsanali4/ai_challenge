from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

from .base_llm_service import BaseLLMService


class OpenAIChatLLM(BaseLLMService):
    """OpenAI-based LLM service"""

    def __init__(
        self, model: str = "gpt-4o-mini", embeddings_model: str = "text-embedding-3-small"
    ):
        self.llm = ChatOpenAI(model=model)
        self.embeddings = OpenAIEmbeddings(model=embeddings_model)

    def get_embeddings(self, text: str):
        """Retrieve text embeddings"""
        return self.embeddings.embed_documents([text])[0]

    def generate_response(self, prompt: str) -> str:
        """Generate response from OpenAI Chat Model"""
        response = self.llm.invoke(prompt)
        return response.content
