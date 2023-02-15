from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Table
from db import Base


actor_movie_association = Table(
    "actor_movie",
    Base.metadata,
    Column("actor_id", ForeignKey("actor.id"), primary_key=True),
    Column("movie_id", ForeignKey("movie.id"), primary_key=True),
)


class ActorModel(Base):
    __tablename__ = "actor"

    id = Column(String, primary_key=True)
    primary_name = Column(String)
    birth_year = Column(Integer)
    movies = relationship("MovieModel", secondary=actor_movie_association, back_populates="actors")


class MovieModel(Base):
    __tablename__ = "movie"

    id = Column(String, primary_key=True)
    primary_title = Column(String)
    start_year = Column(Integer)
    runtime_minutes = Column(Integer)
    region = Column(String)
    average_rating = Column(Float)
    num_votes = Column(Integer)
    actors = relationship("ActorModel", secondary=actor_movie_association, back_populates="movies")
