import asyncio
from clients.gemini_client import GeminiClient
from clients.openrouter_client import OpenRouterClient
from schemas import ChatMessage

async def main():
    """client = GeminiClient()"""
    client = OpenRouterClient()
    messages = [
        ChatMessage(
            role = "user",
            content = "Cual es la capital de Argentina?. Responde en 10 oraciones."
        )
    ]
    
    print("=== Respuesta normal ===")
    response = await client.generate(messages)
    print(response.text)
    
    print("\n=== Respuesta streaming ===")
    async for token in client.stream(messages):
        print(token, end="", flush="True")
    
    print()
    
if __name__ == "__main__":
    asyncio.run(main())
    