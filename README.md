# Backend do programa Proagro Fácil

> Status do Projeto: :heavy_check_mark: Concluído.

## Informações gerais
Backend do sistema de comunicação de perda do programa Proagro fácil. Frontend [aqui](https://github.com/Johnson49/frontend-Proagro-facil).

## Tecnologias 
> O projeto é criado com:

* Python 3.8+
* Fast API
* Firebase
* Uvicorn

## Setup: 
> Para rodar este projeto, clone localmente e depois instale as dependências com um gerenciador de sua preferência.

```python
$ git clone https://github.com/Johnson49/backend-Proagro-facil
$ cd backend-Proagro-facil
$ pip install -r requirements
$ uvicorn main:app --reload
```  

## Deploy da Aplicação 
> https://api-proagro-facil.herokuapp.com

## Documentação da API 
> https://api-proagro-facil.herokuapp.com/docs

## EndPoints

> As rotas são compostas pelo endereço base (https://api-proagro-facil.herokuapp.com) mais o recurso que você deseja acessa.

|Request|URL| Detalhes|
|:-------:|:-----:|:------:|
|GET | /consultar | consulta todos os comunicados existentes no banco de dados.|
|GET |  /consultar/{id} | consulta um comunicado pelo seu id|
|GET | /consultar/cpf/{cpf} | consulta um comunicado pelo seu CPF|
|POST | /registrar | registra um novo comunicado no banco de dados. |
| PUT | /consultar/atualizar/{id} | atualiza os dados de um comunicado.|
| DELETE | /consultar/deletar/{cpf} |  apagar um comunicado do banco de dados|















