from pydantic import BaseModel, RootModel
from typing import List
from datetime import datetime

class Comment(BaseModel):
    phrase_id: int
    author: str
    content: str

class PhraseComments(RootModel):
    comments: List[Comment]

