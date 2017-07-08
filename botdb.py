from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random  # удалить потом перед merge

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
        return '<Event: {} {}}>'.format(self.id, self.is_user_active)


class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True)
    user_list_id = Column(Integer)
    event_id = Column(Integer)
    goal_name = Column(String(500))
    status = Column(String(1))

    def __init__(self, user_list_id=None, event_id=None, goal_name=None, status=None):
        self.user_list_id = user_list_id
        self.event_id = event_id
        self.goal_name = goal_name
        self.status = status

    def __repr__(self):
        return '<{}, {}, {}, {}, {}>'.format(
            self.id, self.user_list_id, self.event_id, self.goal_name, self.status)


class List(Base):
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True)
    goal_id = Column(Integer)
    user_id = Column(Integer)

    def __init__(self, goal_id=None, user_id=None):
        self.goal_id = goal_id
        self.user_id = user_id

    def __repr__(self):
        return '<{}, {}, {}>'.format(self.id, self.goal_id, self.user_id)


# class UserList(Base):
#     __tablename__ = 'userlist'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer)
#     list_id = Column(Integer)

#     def __init__(self, user_id=None, list_id=None):
#         self.user_id = user_id
#         self.list_id = list_id

#     def __repr__(self):
#         return '<User ID: %s, List ID: %d>' % (self.user_id, self.list_id)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50))
    telegram_id = Column(Integer)

    def __init__(self, telegram_id=None, user_name=None):
        self.telegram_id = telegram_id
        self.user_name = user_name

    def __repr__(self):
        return '<{}, {}>'.format(self.id, self.user_name, self.telegram_id)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    goal = Goal(random.randint(1, 100), 0, 'Это ваша цель номер 1', 'A')  # удалить потом перед merge
    db_session.add(goal)  # удалить потом перед merge
    db_session.commit()  # удалить потом перед merge
    print("База данных успешно создана")
