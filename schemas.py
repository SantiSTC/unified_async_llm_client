from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    content: str
    
class ModelResponse(BaseModel):
    text: str