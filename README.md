# Backend do programa Proagro Fácil

Backend do sistema de comunicação de perda do programa Proagro fácil. Frontend [Aqui](https://github.com/Johnson49/frontend-Proagro-facil).


## Começando

### Clone o projeto

:warning: Antes de rodar a aplicação, é necessario ter uma chave json para se conectar ao banco de dados do firebase. Para saber como consegui-la, acesse a documentação do Firebase [aqui](https://firebase.google.com/docs/firestore/quickstart).

`git clone https://github.com/Johnson49/backend-Proagro-facil`

#### Adentre no diretório
`cd backend-Proagro-facil`

####  Instale as dependências

`pip install -r requirements `


##  Inicie o servidor 

`uvicorn main:app --reload`
  

## EndPoints

> As rotas são compostas pelo endereço base (http://localhost:8000) mais o recurso que você deseja acessa.

|Método|Rota| Funcionalidade| Acesso |
|:-------:|:-----:|:------:|:------:|
|GET | /consultar | Consulta todos os comunicados existentes no banco de dados.| Público |
|GET |  /consultar/{id} | Consulta um comunicado pelo seu id| Público |
|GET | /consultar/cpf/{cpf} | Consulta um comunicado pelo seu CPF| Público |
|POST | /registrar | Registra um novo comunicado no banco de dados. | Público |
| PUT | /consultar/atualizar/{id} | Atualiza os dados de um comunicado.| Público |
| DELETE | /consultar/deletar/{cpf} |  Apagar um comunicado do banco de dados| Público |















