from sqlalchemy import  Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)