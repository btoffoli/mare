import datetime

from config import dbConfig
from models import Client, User, Equipment, TideGaugeEvent
from datetime import datetime, timedelta
from sqlalchemy import func



class MareService:

    # TODO metodo inserirDispositivo, mapear tipo_dispositivo
    # TODO mapear dispositvo e item em instalacao implementar teste p/ verificar
    #

    @property
    def __sessao(self):
        return dbConfig.session()


    
    def get_by_id(self, classename, id):
        # build = "dbConfig.session().query(%s).get(id)" % classe
        # obj = eval(build)
        obj = dbConfig.session().query(eval(classename)).get(id)
        return obj

   
    def insert(self, classe, commit=False, **kwargs):
        build = "%s(**kwargs)" % classe
        # print(build)
        obj = eval(build)
        self.__sessao.add(obj)
        if commit:
            self.__sessao.commit()
        return obj

    def list(self, classe, limit=1000, offset=0, **kwargs):
        query_str = "dbConfig.session().query(%s).filter_by(**kwargs).limit(%d)" \
            % (classe, limit)
        if offset:
            query_str += ".offset(%d)" % offset        
        query_str += ".all()"
        objs   = eval(query_str)

        return objs



    # def inserirDispositivo(self, tipo, codigo, nome, commit=True):
    #     disp = self.obterDispositivoPorCodigo(codigo)
    #     if not disp:
    #         disp = Dispositivo(tipo_dispositivo=tipo, nome=nome, codigo=codigo)
    #         self.__sessao.add(disp)
    #         if commit:
    #             self.__sessao.commit()
    #     return disp

    # def inserirTipoDispositivo(self, codigo, nome, commit=True):
    #     tpDisp = self.obterTipoDispositivoPorCodigo(codigo)
    #     if not tpDisp:
    #         tpDisp = TipoDispositivo(nome=nome, codigo=codigo)
    #         self.__sessao.add(tpDisp)
    #         if commit:
    #             self.__sessao.commit()
    #     return tpDisp

    # def instalarDispositivoNoItem(self, item, dispositivo, data_instalacao=datetime.now(), commit=True):
    #     sessao = self.__sessao
    #     #verifiy if exists an instalation for this dispositivo
    #     #inst = sessao.query(Instalacao).query(Instalacao.dispositivo == dispositivo)
    #     #inst.data_desinstalacao = datetime.now()
    #     sessao.query(Instalacao).filter(Instalacao.dispositivo == dispositivo).update({Instalacao.data_desinstalacao: datetime.now()})
    #     inst = Instalacao(item=item, dispositivo=dispositivo, data_instalacao=data_instalacao)
    #     sessao.add(inst)
    #     if commit:
    #         sessao.commit()
    #     return inst

    # def inserirLeitura(self, codigoDispositivo, longitude, latitude, velocidade, precisao_localizacao, atributos=None, data_hora_leitura=datetime.now(), commit=True):
    #     sessao = self.__sessao
    #     disp = self.obterDispositivoPorCodigo(codigoDispositivo)
    #     if not disp:
    #         raise ValueError("There isn't device with code = %s" %codigoDispositivo)

    #     #find the installation
    #     inst = self.obterInstalacaoEmAbertoPeloDispositivo(disp)
    #     if not inst:
    #         raise ValueError("There isn't installation to device %s" %disp)

    #     leit = Leitura(instalacao=inst, itens=[inst.item.id], horario_leitura=data_hora_leitura, localizacao="SRID=4326;POINT(%f %f)" %(longitude, latitude), velocidade=velocidade, precisao_localizacao=precisao_localizacao, atributos=atributos)
    #     sessao.add(leit)

    #     if commit:
    #         sessao.commit()
    #     return leit


    # def inserirItem(self, nome, codigo, commit=True):
    #     sessao = dbConfig.session()

    #     it = self.obterItemPorCodigo(codigo)
    #     if not it:
    #         it = Item(nome=nome, codigo=codigo)
    #         sessao.add(it)
    #     #Verificar existencia do item, codigo e instalacao
    #     if commit:
    #         sessao.commit()
    #     return it

    # def obterInstalacaoEmAbertoPorItemEDispositivo(self, item, dispositivo):
    #     instalacao = None
    #     q = dbConfig.session().query(Instalacao).filter(Item == item, )
    #     itens = q.all()
    #     if itens:
    #         item = itens[0]
    #     return item

    # def obterItemPorNome(self, nome):
    #     item = None
    #     q = dbConfig.session().query(Item).filter(Item.nome==nome)
    #     itens = q.all()
    #     if itens:
    #         item = itens[0]
    #     return item

    # def obterItemPorCodigo(self, codigo):
    #     item = None
    #     q = dbConfig.session().query(Item).filter(Item.codigo == codigo)
    #     itens = q.all()
    #     if itens:
    #         item = itens[0]
    #     return item

    # def obterDispositivoPorNome(self, nome):
    #     dispositivo = None
    #     q = dbConfig.session().query(Dispositivo).filter(Dispositivo.nome == nome)
    #     dispositivos = q.all()
    #     if dispositivos:
    #         dispositivo = dispositivos[0]
    #     return dispositivo

    # def obterDispositivoPorCodigo(self, codigo):
    #     dispositivo = None
    #     q = dbConfig.session().query(Dispositivo).filter(Dispositivo.codigo == codigo)
    #     dispositivos = q.all()
    #     if dispositivos:
    #         dispositivo = dispositivos[0]
    #     return dispositivo

    # def obterTipoDispositivoPorCodigo(self, codigo):
    #     tpDisp = None
    #     q = dbConfig.session().query(TipoDispositivo).filter(TipoDispositivo.codigo == codigo)
    #     tipos = q.all()
    #     if tipos:
    #         tpDisp = tipos[0]
    #     return tpDisp

    # def obterInstalacaoEmAbertoPeloDispositivo(self, dispositivo):
    #     inst = None
    #     sessao = self.__sessao
    #     q = sessao.query(Instalacao).filter(Instalacao.dispositivo==dispositivo, Instalacao.data_desinstalacao==None)
    #     instalacoes = q.all()
    #     if instalacoes:
    #         inst = instalacoes[0]
    #     return inst

    # def listarLeiturasDeDispositivo(self, codigoDispositivo, data_inicio=None, data_fim=datetime.now()):
    #     sessao = self.__sessao
    #     _delta_max = 60*60
    #     _tempoDeLeiturasEmMin = 10
    #     if not data_inicio:
    #         data_inicio = data_fim.replace(minute=(data_fim.minute-10))
    #     delta = data_fim - data_inicio
    #     if delta.total_seconds() > _delta_max:
    #         raise ValueError("It isn't possible retrieve gps packets with more than %d seconds" %_delta_max)

    #     disp = self.obterDispositivoPorCodigo(codigoDispositivo)
    #     if not disp:
    #         raise ValueError("There isn't device with code = %s" % codigoDispositivo)

    #     # find the installation
    #     inst = self.obterInstalacaoEmAbertoPeloDispositivo(disp)
    #     if not inst:
    #         raise ValueError("There isn't installation to device %s" % disp)

    #     q = sessao\
    #         .query(Leitura,
    #                func.ST_X(Leitura.localizacao).label("longitude"),
    #                func.ST_Y(Leitura.localizacao).label("latitude"),
    #                func.ST_ASTEXT(Leitura.localizacao).label("wkt"))\
    #         .filter(Leitura.instalacao == inst, Leitura.horario_leitura >= data_inicio, Leitura.horario_leitura <= data_fim)\
    #         .order_by(Leitura.horario_leitura.asc())

    #     leituras = q.all()

    #     return leituras






    # def inserirItemEDispositivoComInstalacao(self, nomeItem, codigoItem, listaDispositivo, dataInstalacao=datetime.now):
    #     pass






