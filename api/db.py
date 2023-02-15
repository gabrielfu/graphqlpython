import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

POSTGRES_DB_URI = os.environ.get("POSTGRES_DB_URI", "postgresql://user:123456@localhost:5432/imdb_db")
FIXTURE_NAME_PATH = os.environ.get("FIXTURE_NAME_PATH", "../data/imdb/name.csv")
FIXTURE_TITLE_PATH = os.environ.get("FIXTURE_TITLE_PATH", "../data/imdb/title.csv")

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
    from models import NameModel, TitleModel

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def add_fixture(Model, row):
        db_session.add(Model(**row))

    for _, row in pd.read_csv(FIXTURE_NAME_PATH).iterrows():
        add_fixture(NameModel, row)

    for _, row in pd.read_csv(FIXTURE_TITLE_PATH).iterrows():
        add_fixture(TitleModel, row)

    db_session.commit()