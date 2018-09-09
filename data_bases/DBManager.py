from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBManager:
    __instance = None

    @staticmethod
    def instance():
        if DBManager.__instance is None:
            DBManager.__instance = DBManager()
        return DBManager.__instance

    def __init__(self):
        self.Base = declarative_base()

    def create(self):
        self.engine = create_engine('sqlite:///todolist.db', echo=True)
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


