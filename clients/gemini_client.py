from google import genai
from schemas import ChatMessage, ModelResponse
from config import GEMINI_API_KEY
from clients.base import BaseLLMClient

class GeminiClient(BaseLLMClient):
    def __init__ (self, model: str = "gemini-3.5-flash"):
        self.client = genai.Client(api_key = GEMINI_API_KEY)
        self.model = model
        
    async def generate(self, messages: list[ChatMessage]) -> ModelResponse:
        try: 
            prompt = "\n".join(
                f"{message.role} {message.content}"
                for message in messages
            )
            response = await self.client.aio.models.generate_content(
                model = self.model, 
                contents = prompt,
            )
            return ModelResponse(text = response.text)
        
        except Exception as e:
            return ModelResponse(text = f"Error: {e}")
        
    async def stream(self, messages: list[ChatMessage]):
        try:
            prompt = "\n".join(
                f"{message.role}: {message.content}"
                for message in messages
            )
            stream = await self.client.aio.models.generate_content_stream(
                model = self.model,
                contents = prompt
            )
            async for chunk in stream:
                if chunk.text:
                    yield chunk.text
                
        except Exception as e:
            yield ModelResponse(text = f"Error: {e}")