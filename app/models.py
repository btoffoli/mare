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

    login           = Column(String(48))
    email           = Column(String)
    name            = Column(String(128))
    identify_doc    = Column(String(28))

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


class Equipment(AbstractModel, Base):    
    __tablename__ = 'equipament'

    prefix_identify = Column(String)

    nickname        = Column(String(64))

    client_id       = Column(ForeignKey('client.id'),
                           nullable=False,
                           index=True)
    client          = relationship(Client)    



class DataEvent(AbstractModel, Base):
    __tablename__       = 'data_event'

    """Hydrodynamic"""
    magnitude           = Column(Float(precision=2))

    corrent_direction   = Column(Integer)

    significant_height  = Column(Float(precision=2))

    peak_period         = Column(Float(precision=2))

    peak_direction      = Column(Integer)

    datetime            = Column(DateTime(timezone=True), default=func.now())
    status_gps          = Column(String(1))

    """meteorology"""
    """Verificar se precisa registrar demais unidades ou se armazena em uma unidade apenas e convete-se sob demanda"""
    speed               = Column(Float(precision=1))

    wind_direction      = Column(Float(precision=1))


    #Incluir "from geoalchemy2.types import Geometry" na migration gerada
    location            = Column(Geometry('Point', srid=4326))



    equipment_id        = Column(ForeignKey('equipment.id'),
                          nullable=False,
                           index=True)
    equipment           = relationship(Equipment)

