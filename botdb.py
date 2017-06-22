from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///botdb.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()



class UserList(Base):
    __tablename__ = 'userlist'
    user_list_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    status = Column(String(1)) # Status: A | D

    def __repr__(self):
        return '<User List ID: %s, Status: %d>' % (self.user_list_id, self.status)


class Goal(Base):
    __tablename__ = 'goal'
    goal_id = Column(Integer, primary_key=True)
    user_list_id = Column(Integer)
    goal = Column(String(500))
    status = Column(String(1)) # Status: A | D

    def __repr__(self):
        return '<Goal ID: %s, Status: %d>' % (self.goal_id, self.status)


class Event(Base):
    __tablename__ = 'event'
    event_id = Column(Integer, primary_key=True)
    user_list_id = Column(Integer)
    event = Column(String(500))
    goal_id = Column(Integer)
    status = Column(String(1)) # Status: A | D

    def __repr__(self):
        return '<Event ID: %s, Status: %d>' % (self.event_id, self.status)


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(50))
    user_list_id = Column(Integer)
    goal_id = Column(Integer)
    event_id = Column(Integer)
    status = Column(String(1)) # if remove User from List set status to D for this List, Default = A

    def __repr__(self):
        return '<User ID: %s, Status: %d>' % (self.user_id, self.status)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("База данных успешно создана")