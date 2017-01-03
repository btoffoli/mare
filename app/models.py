from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

Base = declarative_base()


class AbstractModel:
    id      = Column(Integer, primary_key=True)
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), default=func.now())

class Client(AbstractModel, Base):
    __tablename__   = 'client'

    name            = Column(String)
    identify        = Column(String)

class User(AbstractModel, Base):
    __tablename__   = 'user'


    login           = Column(String)
    email           = Column(String)
    name            = Column(String)
    identify_doc    = Column(String)

    client_id       = Column(ForeignKey('client.id'),
                           nullable=False,
                           index=True)
    client          = relationship(Client)


class UserSession(AbstractModel, Base):
    __tablename__   = 'user_session'

    logout          = Column(DateTime(timezone=True))

    user_id         = Column(ForeignKey('user.id'),
                           nullable=False,
                           index=True)
    user            = relationship(User)


class DataEvent(AbstractModel, Base):
    __tablename__   = 'data_event'

    datetime        = Column(DateTime(timezone=True), default=func.now())
    status_gps      = Column(String(1))

    #Incluir "from geoalchemy2.types import Geometry" na migration gerada
    location        = Column(Geometry('Point', srid=4326))



    client_id       = Column(ForeignKey('client.id'),
                           nullable=False,
                           index=True)
    client          = relationship(Client)

