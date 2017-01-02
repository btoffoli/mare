from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class AbstractModel:
    id      = Column(Integer, primary_key=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now())

class Client(AbstractModel, Base):
    __tablename__   = 'client'

    name            = Column(String)

class User(AbstractModel, Base):
    __tablename__   = 'user'

    login           = Column(String)
    email           = Column(String)
    name            = Column(String)
    identify_doc    = Column(String)

    client          = relationship(Client)


class UserSession(AbstractModel, Base):
    __tablename__   = 'user_session'

    logout = Column(DateTime)
    user            = relationship(User)

