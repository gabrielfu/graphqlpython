import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

POSTGRES_DB_URI = os.environ.get("POSTGRES_DB_URI", "postgresql://user:123456@localhost:5432/imdb_db")
FIXTURE_MOVIES_PATH = os.environ.get("FIXTURE_MOVIES_PATH", "../data/imdb/movies.parquet")
FIXTURE_ACTORS_PATH = os.environ.get("FIXTURE_ACTORS_PATH", "../data/imdb/actors.parquet")
FIXTURE_ASSOCIATION_PATH = os.environ.get("FIXTURE_ASSOCIATION_PATH", "../data/imdb/actor_movie.parquet")

engine = create_engine(POSTGRES_DB_URI, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import ActorModel, MovieModel

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    actors = {}
    for _, row in pd.read_parquet(FIXTURE_ACTORS_PATH).iterrows():
        item = ActorModel(**row.to_dict())
        actors[item.id] = item

    movies = {}
    for _, row in pd.read_parquet(FIXTURE_MOVIES_PATH).iterrows():
        item = MovieModel(**row.to_dict())
        movies[item.id] = item

    for _, (movie_id, actor_id) in pd.read_parquet(FIXTURE_ASSOCIATION_PATH).iterrows():
        movies[movie_id].actors.append(actors[actor_id])

    for item in actors.values():
        db_session.add(item)

    for item in movies.values():
        db_session.add(item)

    db_session.commit()