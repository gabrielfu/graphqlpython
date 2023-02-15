import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

POSTGRES_DB_URI = os.environ.get("POSTGRES_DB_URI", "postgresql://user:123456@localhost:5432/imdb_db")
FIXTURE_MOVIES_PATH = os.environ.get("FIXTURE_MOVIES_PATH", "../data/imdb/movies.csv")
FIXTURE_ACTORS_PATH = os.environ.get("FIXTURE_ACTORS_PATH", "../data/imdb/actors.csv")
FIXTURE_ASSOCIATION_PATH = os.environ.get("FIXTURE_ASSOCIATION_PATH", "../data/imdb/actor_movie.csv")

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
    with open(FIXTURE_ACTORS_PATH, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            item = ActorModel(**row)
            actors[item.id] = item

    movies = {}
    with open(FIXTURE_MOVIES_PATH, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            item = MovieModel(**row)
            movies[item.id] = item

    with open(FIXTURE_ASSOCIATION_PATH, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["movie_id"]].actors.append(actors[row["actor_id"]])

    for item in actors.values():
        db_session.add(item)

    for item in movies.values():
        db_session.add(item)

    db_session.commit()