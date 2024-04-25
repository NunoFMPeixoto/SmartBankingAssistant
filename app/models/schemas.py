from pydantic import BaseModel

class Phrase(BaseModel):
    text: str


class IntentionRequest(BaseModel):
    phrase: str
    model: str
    provider: str
    similarity_search_method: str