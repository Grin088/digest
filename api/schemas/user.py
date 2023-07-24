from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True
