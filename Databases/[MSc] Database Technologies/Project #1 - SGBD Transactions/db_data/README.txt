## APLICAÇÃO
> 3 tipos de clientes (hospital, polícia e restantes entidades)
* Hospital ("/hospital_client"): executar "hospital_main.py"
* Polícia ("/police_client"): executar "police_main.py"
* Entidade ("/entity_client"): executar "entidade_main.py"

## BASE DE DADOS
> usar o conteúdo da pasta "/db_data"

> descarregar os dados (https://github.com/centraldedados/sinistralidade.git) e executar "unidecode_distritos.py" seguido de "parser.py". OU então usar os dados já processados da pasta "dados_processados".

> para criar a base de dados, tabelas, utilizadores e respetivos privilégios, executar "create_db.sql"

> no computador que der host à base de dados, correr o programa "server.py" para tratar dos pedidos dos clientes

## CONFIGURAÇÃO ADICIONAL
> os endereços ip poderão necessitar de um ajuste (nomeadamente, nos ficheiros "client.py" que estão nas pastas dos 3 tipos de clientes)