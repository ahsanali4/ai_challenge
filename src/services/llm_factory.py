from .openai_llm_service import OpenAIChatLLM


def get_llm_service(provider: str = "openai"):
    """Returns the appropriate LLM service based on provider selection"""
    if provider == "openai":
        return OpenAIChatLLM()
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
