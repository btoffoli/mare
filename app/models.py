from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Float, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

Base = declarative_base()


class AbstractModel:
    id      = Column(Integer, primary_key=True)
    created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated = Column(DateTime(timezone=True), server_default=func.now(), \
        onupdate=func.utc_timestamp(), nullable=False)

    def to_map(self):
        map_obj = {
            "id": self.id,
            "created": self.created,
            "updated": self.updated
        }
        return map_obj

    def __repr__(self):
        return "<class: %s - id: %d - identify: %d>" %(type(self), self.id, id(self))

class Client(AbstractModel, Base):
    __tablename__   = 'client'

    name            = Column(String, nullable=False)
    identify        = Column(String, nullable=False)

    def to_map(self):
        super_ref = super(Client, self)
        obj_map = super_ref.to_map()
        obj_map["name"] = self.name
        obj_map["idenfity"] = self.identify
        return obj_map




class User(AbstractModel, Base):
    __tablename__   = 'user'

    login           = Column(String(48), nullable=False)
    email           = Column(String(128), nullable=False)
    name            = Column(String(128), nullable=True)
    identify_doc    = Column(String(28), nullable=True)

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
    __tablename__ = 'equipment'

    prefix_identify = Column(String(48), nullable=False)

    nickname        = Column(String(64))

    client_id       = Column(ForeignKey('client.id'),
                           nullable=False,
                           index=True)
    client          = relationship(Client)


'''
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
'''

class TideGaugeEvent(AbstractModel, Base):
    __tablename__                   = 'tide_gauge_event'

    distance_from_water_level       = Column(Float(precision=2))
    pressure                        = Column(Integer)
    tide                            = Column(Float(precision=2))
    voltage                         = Column(Float(precision=2))
    event_time                      = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    equipment_id        = Column(ForeignKey('equipment.id'),
                          nullable=False,
                           index=True)
    equipment           = relationship(Equipment)


Index('idx_tide_gauge_event_time', TideGaugeEvent.event_time, TideGaugeEvent.equipment_id)