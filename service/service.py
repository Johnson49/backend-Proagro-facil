from database import Repository
from schemas import SchemaComunidadoDePerda


def consultar():
    consulta = Repository().consultar()
    return consulta

def consultar_id(id: str):
    consulta = Repository().consultarPorID(id)
    return consulta

def consultar_cpf(cpf: str):
    consulta = Repository().consultarPorCpf(cpf)
    return consulta

def registrar(schema: SchemaComunidadoDePerda):
    Repository().criar(schema)

def atualizar(id: str, schema: SchemaComunidadoDePerda):
    Repository().atualizar(id, schema)

def excluir(cpf:str):
    Repository().excluir(cpf)