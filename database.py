from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'sqlite:///./db.sqlite3'


engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread': False},
                       echo=True)


Session = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass


def get_db():
    try:
        db_session = Session()
        yield db_session
    except Exception as e:
        db_session.rollback()
        raise e
    finally:
        db_session.close()
