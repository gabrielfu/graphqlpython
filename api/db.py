import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from typing import Dict

POSTGRES_DB_URI = os.environ.get("POSTGRES_DB_URI", "postgresql://user:123456@localhost:5432/imdb_db")
FIXTURE_MOVIES_PATH = os.environ.get("FIXTURE_MOVIES_PATH", "../data/imdb/movies.parquet")
FIXTURE_ACTORS_PATH = os.environ.get("FIXTURE_ACTORS_PATH", "../data/imdb/actors.parquet")

engine = create_engine(POSTGRES_DB_URI, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import ActorModel, MovieModel

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def add_fixture(Model, fields: Dict):
        db_session.add(Model(**fields))

    for _, row in pd.read_parquet(FIXTURE_ACTORS_PATH).iterrows():
        add_fixture(ActorModel, row.to_dict())

    for _, row in pd.read_parquet(FIXTURE_MOVIES_PATH).iterrows():
        add_fixture(MovieModel, row.to_dict())

    db_session.commit()