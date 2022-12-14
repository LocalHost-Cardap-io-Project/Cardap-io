# Cardap-io

O [Cardap-io](https://rodd369.pythonanywhere.com/swagger/) disponibiliza uma API REST que permite o acesso e registro de restaurantes, menus, categorias, produtos/pratos.


Recursos disponíveis para acesso via API:
* [**Registro como Cliente**](#reference/recursos/cliente)
* [**Registro como Estabelecimento**](#reference/recursos/estabelecimento)
* [**Login**](#reference/recursos/login)
* [**Logout**](#reference/recursos/logout)

Recursos Dashboard Estabelecimento:
* [**Menus**](#reference/recursos/menus)
* [**Categorias**](#reference/recursos/categorias)
* [**Produtos**](#reference/recursos/produtos)

## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |


## Respostas

| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `401` | Dados de acesso inválidos.|
| `404` | Registro pesquisado não encontrado (Not found).|
| `405` | Método não implementado.|
| `410` | Registro pesquisado foi apagado do sistema e não esta mais disponível.|
| `422` | Dados informados estão fora do escopo definido para o campo.|
| `429` | Número máximo de requisições atingido. (*aguarde alguns segundos e tente novamente*)|

# Recursos

## Registro Cliente (POST) [api/v1/signup/client/]

+ Request (application/json)

  + Body
  
        {
          "username": "string",
          "email": "string",
          "password":"string",
          "password2": "string"
        }
        
+ Response 201 (application/json)

  + Body
  
        {
          "user": {
              "username": "string",
              "email": "string",
              "is_client": true
          },
          "token": "string",
          "message": "Client account created succesfuly."
        }

## Registro Restaurante (POST) [api/v1/signup/organization/]

+ Request (application/json)

  + Body
  
        {
          "username": "string",
          "organizations": {"oganization":"string"},
          "email": "string",
          "password":"string",
          "password2": "string"
        }
        
+ Response 201 (application/json)

  + Body
  
        {
          "user": {
              "username": "string",
              "email": "string",
              "is_client": false
          },
          "token": "string",
          "message": "Organization account created succesfuly."
        }
        
## Login (POST) [api/v1/login/]

+ Request (application/json)

  + Body
  
        {
          "username": "string",
          "password": "string"
        }
        
+ Response 201 (application/json)

  + Body
  
        {
          "token": "string",
          "user_id": 0,
          "is_client": true
        }
        
## Logout (POST) [api/v1/logout/]

+ No parameters

