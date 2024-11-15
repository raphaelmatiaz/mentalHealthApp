from pydantic import BaseModel, Field, RootModel

class Comment(BaseModel):
    id: str = Field(alias="_id")
    content: str
    author: str
    category_id: int


class CategoryComments(RootModel):
    root: list[Comment]
