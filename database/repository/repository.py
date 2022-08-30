from ..config import database
from schemas import SchemaComunidadoDePerda



class Repository:
    def criar(self, schema: SchemaComunidadoDePerda):
        model = {
            "nome": schema.nome,
            "email": schema.email,
            "cpf": schema.cpf,
            "tipoDaLavoura": schema.tipoDaLavoura,
            "dataDaColheita": schema.dataDaColheita,
            "eventoOcorrido": schema.eventoOcorrido,
            "latitude": schema.latitude,
            "longitude": schema.longitude
        }
        
        database.collection("ComunicadosDePerda").document(model["cpf"]).set(model)

    def consultar(self):
        docs = database.collection(u'ComunicadosDePerda').stream()
        lista = []
        for doc in docs:
            lista.append({"id": doc.id, "dados": doc.to_dict() })

        return lista

    def consultarPorID(self, id: str):
        doc = database.collection(u'ComunicadosDePerda').document(id).get()
        if doc.exists:
            return {"id":doc.id, "dados": doc.to_dict()}

        return "Documento não existe no banco de dados."

    def consultarPorCpf(self, cpf: str):
        docs = database.collection(u'ComunicadosDePerda').where(
            u'cpf', u'==', cpf).stream()
        lista = []
        for doc in docs:
            lista.append({"id": doc.id, "dados": doc.to_dict()})

        return lista

    def consultarIDPeloCPF(self, cpf: str):
        docs = database.collection(u'ComunicadosDePerda').where(
            u'cpf', u'==', cpf).stream()
        lista = []
        for doc in docs:
            lista.append( doc.id )

        return lista
        

    def atualizar(self, id: str, schema: SchemaComunidadoDePerda):
        model = {
            "nome": schema.nome,
            "email": schema.email,
            "cpf": schema.cpf,
            "tipoDaLavoura": schema.tipoDaLavoura,
            "dataDaColheita": schema.dataDaColheita,
            "eventoOcorrido": schema.eventoOcorrido,
            "latitude": schema.latitude,
            "longitude": schema.longitude
        }
        database.collection(u'ComunicadosDePerda').document(id).set(model)
     

    def excluir(self, id: str):
        database.collection(u'ComunicadosDePerda').document(id).delete()
