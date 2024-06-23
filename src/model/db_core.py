from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base, sessionmaker

import src.config as c

path = f"mysql+pymysql://{c.MYSQL_USER}:{c.MYSQL_PASSWORD}@{c.MYSQL_HOST}:{c.MYSQL_PORT}/{c.MYSQL_DATABASE}"

engine = create_engine(path, echo=False)

db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    session: Session = db_session()
    try:
        yield session
    finally:
        session.close()
