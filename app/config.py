from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from threading import currentThread
from datetime import datetime

class __DBConfig:

    def __init__(self):
        self.__sessionFactory = sessionmaker(bind=self.poolEngine)
        #TODO verificar threadsafe qnd não houver mais GLI
        self.__sessions = {}

    @property
    def url(self):
        return 'postgresql://geocontrol:geo007@localhost:25433/mare'

    @property
    def schema(self):
        return 'public'

    @property
    def poolEngine(self):
        return create_engine(self.url, pool_size=20, max_overflow=0)

    @property
    def sessionFactory(self):
        if not self.__sessionFactory:
            self.__sessionFactory = sessionmaker(bind=self.poolEngine)
        return self.__sessionFactory


    def session(self):
        currentSessionTuple = self.__sessions.get(currentThread())
        if not currentSessionTuple:
            currentSessionTuple  =  self.__sessions[currentThread()] = (datetime.now(), self.sessionFactory())
        return currentSessionTuple[1]




dbConfig = __DBConfig()