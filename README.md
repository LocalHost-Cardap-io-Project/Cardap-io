# Cardap-io

O [Cardap-io](#) disponibiliza uma API REST que permite o acesso aos contatos, produtos e vendas do sistema.


Recursos disponíveis para acesso via API:
* [**Contatos**](#reference/recursos/contatos)
* [**Produtos**](#reference/recursos/produtos)
* [**Serviços**](#reference/recursos/servicos)
* [**Recebimentos**](#reference/recursos/recebimentos)
* [**Pagamentos**](#reference/recursos/pagamentos)
* [**Vendas**](#reference/recursos/vendas)
* [**Usuários**](#reference/recursos/usuarios)

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
