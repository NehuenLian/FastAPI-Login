from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class UserLogin(UserBase):
    username: str
    password: str

class UserCreate(UserBase):
    username: str
    password: str

class User(UserBase):
    id: int
    role: str

    model_config = {
        "from_attributes": True
    }