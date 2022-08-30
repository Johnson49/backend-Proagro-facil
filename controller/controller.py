from fastapi import APIRouter, status
from schemas import SchemaComunidadoDePerda
from service import (   consultar, 
                        consultar_id, 
                        consultar_cpf, 
                        registrar,
                        atualizar,
                        excluir
                        )

router = APIRouter()

@router.get("/consultar")
def consulta_todos_os_comunicados_do_banco_de_dados():
    "Atráves desta rota, será possivel consultar todos os comunicados existentes no banco de dados."
    return consultar()


@router.get("/consultar/{id}")
def consulta_comunicado_pelo_id_no_banco_de_dados(id: str):
    "Atráves desta rota, será possivel consultar um comunicado pelo seu id."
    return consultar_id(id)

@router.get("/consultar/cpf/{cpf}")
def consulta_comunicados_pelo_cpf_no_banco_de_dados(cpf: str):
    "Atráves desta rota, será possivel consultar um comunicado pelo seu cpf."
    return consultar_cpf(cpf)


@router.post("/registrar", status_code=status.HTTP_201_CREATED)
def registra_um_novo_comunicado_no_banco_de_dados(schema: SchemaComunidadoDePerda):
    "Atráves desta rota, será possivel registrar um novo comunicado no banco de dados."
    return registrar(schema)


@router.put("/consultar/atualizar/{id}", status_code=status.HTTP_200_OK)
def atualiza_os_dados_de_um_comunicado_no_banco_de_dados(id: str, schema: SchemaComunidadoDePerda):
    "Atráves desta rota, será possivel atualizar os dados de um comunicado."
    return atualizar(id, schema)


@router.delete("/consultar/deletar/{cpf}", status_code=status.HTTP_200_OK)
def deleta_um_comunidado_do_banco_de_dados(cpf: str):
    "Atráves desta rota, será possivel apagar um comunicado do banco de dados."
    return excluir(cpf)
