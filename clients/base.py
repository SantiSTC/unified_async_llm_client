from abc import ABC, abstractmethod
from schemas import ChatMessage, ModelResponse

class BaseLLMClient(ABC):
    @abstractmethod
    async def generate(self, messages: list[ChatMessage]) -> ModelResponse:
        """Genera una respuesta completa."""
        pass
    @abstractmethod
    async def stream(self, messages: list[ChatMessage]):
        """Devuelve la respuesta en streaming."""
        pass