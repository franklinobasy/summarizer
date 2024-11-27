from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
    adapter_id: str
