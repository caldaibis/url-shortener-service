from datetime import datetime
from pydantic import BaseModel, ConfigDict, computed_field

class UrlRequest(BaseModel):
    url: str

class UrlResponse(BaseModel):
    original: str
    shortlink: str
    hits: int
    created_on: datetime
