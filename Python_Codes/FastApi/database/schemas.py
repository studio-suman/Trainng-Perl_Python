from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    useremail: str
    valid: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str


class ItemBase(BaseModel):
    title: str
    description: str
    owner_id: int


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    owner_id: int
    title: str
    description: str
    class Config:
        orm_mode = True