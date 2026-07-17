from openai import AsyncOpenAI
from clients.base import BaseLLMClient
from schemas import ChatMessage, ModelResponse
from config import OPENROUTER_API_KEY


class OpenRouterClient(BaseLLMClient):
    def __init__(self, model: str = "deepseek/deepseek-chat-v3-0324"):
        self.client = AsyncOpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )
        self.model = model

    async def generate(self, messages: list[ChatMessage]) -> ModelResponse:
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": message.role,
                        "content": message.content,
                    }
                    for message in messages
                ],
            )

            return ModelResponse(
                text=response.choices[0].message.content
            )

        except Exception as e:
            return ModelResponse(text=f"Error: {e}")

    async def stream(self, messages: list[ChatMessage]):
        try:
            stream = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": message.role,
                        "content": message.content,
                    }
                    for message in messages
                ],
                stream=True,
            )

            async for chunk in stream:
                delta = chunk.choices[0].delta.content

                if delta:
                    yield delta

        except Exception as e:
            yield f"Error: {e}"