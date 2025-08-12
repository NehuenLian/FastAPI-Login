from sqlalchemy import Column, Integer, String

from app.data_access.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)
    role = Column(String, default="user") # Default value
