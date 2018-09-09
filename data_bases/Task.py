from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from data_bases.DBManager import DBManager


class Task(DBManager.Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creator_name = Column(String)
    creator_id = Column(Integer, ForeignKey('users.id'))
    executor_name = Column(String)
    executor_id = Column(Integer, ForeignKey('users.id'))
    deadline = Column(DateTime)
    status = Column(Integer)
    date = Column(DateTime)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Task(id: {0}, name: {1})>".format(self.id, self.name)

