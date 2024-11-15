from pydantic import BaseModel, Field, RootModel, field_validator

class Comment(BaseModel):
    id: str = Field(alias="_id")
    content: str
    author: str
    category_id: int

    @field_validator("id", mode="before")
    @classmethod
    def transform(cls, v):
        return str(v)
    

class CategoryComments(RootModel):
    root: list[Comment]
