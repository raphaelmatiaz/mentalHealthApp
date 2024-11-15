from pydantic import BaseModel, Field, RootModel, field_validator

class Comment(BaseModel):
    id: str = Field(alias="_id")
    content: str
    author: str
    category_id: int


class Comments(RootModel):
    root: list[Comment]
