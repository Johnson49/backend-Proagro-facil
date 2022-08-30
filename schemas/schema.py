from pydantic import BaseModel
from  datetime import date
from typing import Union

class SchemaComunidadoDePerda(BaseModel):
    nome: str
    email: str
    cpf: str
    tipoDaLavoura: str
    dataDaColheita: str
    eventoOcorrido: str
    latitude: str
    longitude: str
