from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base, sessionmaker

path = f"mysql+pymysql://root:root@3.39.210.241:3306/art_path_prod"

engine = create_engine(path, echo=False)

db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    session: Session = db_session()
    try:
        yield session
    finally:
        session.close()
