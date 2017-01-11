from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, funcfilter
from sqlalchemy.orm import sessionmaker

from db.localizador_db import Leitura

engine = create_engine('postgresql://geocontrol:geo007@localhost:25432/azimute')
Session = sessionmaker(bind=engine)

#Session.configure()

sessao = Session()

l = sessao.query(Leitura, func.ST_X(Leitura.localizacao).label('longitude')).last()

print('%f' % l.longitude)

l = sessao.query(Leitura)
