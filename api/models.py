from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from db import Base


class ActorModel(Base):
    __tablename__ = "actor"
    id = Column(String, primary_key=True)
    primary_name = Column(String)
    birth_year = Column(Integer)


class MovieModel(Base):
    __tablename__ = 'movie'
    id = Column(String, primary_key=True)
    primary_title = Column(String)
    start_year = Column(Integer)
    runtime_minutes = Column(Integer)
    region = Column(String)
    average_rating = Column(Float)
    num_votes = Column(Integer)
    actor_id = Column(String, ForeignKey("actor.id"))
    actors = relationship(ActorModel, backref=backref("actor", uselist=True, cascade="delete,all"))
