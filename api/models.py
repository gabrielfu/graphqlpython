from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.db import Base

class NameModel(Base):
    __tablename__ = "name"
    __table_args__ = {'extend_existing': True}
    nconst = Column(String, primary_key=True)
    primaryName = Column(String)
    birthYear = Column(Integer, nullable=True)
    deathYear = Column(Integer, nullable=True)

class TitleModel(Base):
    __tablename__ = 'title'
    __table_args__ = {'extend_existing': True}
    tconst = Column(String, primary_key=True)
    primaryTitle = Column(String)
    startYear = Column(Integer)
    runtimeMinutes = Column(Integer)
    region = Column(String)
    directors = relationship(NameModel, uselist=True)
    writers = relationship(NameModel, uselist=True)
