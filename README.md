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

:warning: Antes de rodar a aplicação, é necessario ter uma chave json para se conectar ao banco de dados do firebase. Para saber como consegui-la, acesse a documentação do Firebase [aqui](https://firebase.google.com/docs/firestore/quickstart).

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

|Método|Rota| Funcionalidade| Acesso |
|:-------:|:-----:|:------:|:------:|
|GET | /consultar | Consulta todos os comunicados existentes no banco de dados.| Público |
|GET |  /consultar/{id} | Consulta um comunicado pelo seu id| Público |
|GET | /consultar/cpf/{cpf} | Consulta um comunicado pelo seu CPF| Público |
|POST | /registrar | Registra um novo comunicado no banco de dados. | Público |
| PUT | /consultar/atualizar/{id} | Atualiza os dados de um comunicado.| Público |
| DELETE | /consultar/deletar/{cpf} |  Apagar um comunicado do banco de dados| Público |















