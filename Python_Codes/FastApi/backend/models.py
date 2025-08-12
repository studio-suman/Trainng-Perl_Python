from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, relationship, Session
from ..database.database import Base

class User(Base):
    __tablename__ = "Users_Table"
    Id = Column(Integer, primary_key=True, index=True)
    User_Name = Column(String)  
    User_Email = Column(String)
    Valid = Column(String)
    Hashed_password = Column(String)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("Users_Table.Id"))
    owner = relationship("User", back_populates="items")


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column("Title", String, index=True)   # DB column Title, Python attr title
    image = Column("Image", String)
    genre = Column("Genre", String)
    rating = Column("Rating", Float)              
