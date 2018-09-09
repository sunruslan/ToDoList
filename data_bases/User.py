from sqlalchemy import Column, Integer, String
from data_bases.DBManager import DBManager


class User(DBManager.instance().Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    position = Column(String)
    email = Column(String)

    def __init__(self, name, surname, position, email):
        self.name = name
        self.surname = surname
        self.position = position
        self.email = email

    def __repr__(self):
        return "<User(id: {0}, name: {1})>".format(self.id, self.name)
