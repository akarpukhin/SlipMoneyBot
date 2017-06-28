from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///botdb.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    user_list_id = Column(Integer)
    is_user_active = Column(Boolean, default=True)

    def __repr__(self):
        return '<ID: %s, Is Active: %d>' % (self.id, self.is_user_active)


class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True)
    user_list_id = Column(Integer)
    event_id = Column(Integer)

    def __repr__(self):
        return '<ID: %s, Event ID: %d>' % (self.id, self.event_id)


class List(Base):
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)

    def __repr__(self):
        return '<ID: %s, Chat ID: %d>' % (self.id, self.chat_id)


class UserList(Base):
    __tablename__ = 'userlist'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    list_id = Column(Integer)

    def __init__(self, user_id=None, list_id=None):
        self.user_id = user_id
        self.list_id = list_id

    def __repr__(self):
        return '<User ID: %s, List ID: %d>' % (self.user_id, self.list_id)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)

    def __init__(self, telegram_id=None):
        self.telegram_id = telegram_id

    def __repr__(self):
        return '<ID: %s, Telegram ID: %d>' % (self.id, self.telegram_id)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("База данных успешно создана")
