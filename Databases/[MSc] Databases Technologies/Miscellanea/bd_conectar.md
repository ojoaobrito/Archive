## ESTABELECER LIGAÇÃO À BD (JÁ CRIADA) USANDO O SCRIPT PYTHON E FAZER QUERIES
-----------------------------------------------------------------------------------------------------------------------------
# PASSO 1 - instalar todos os módulos que sejam precisos (psycopg2, por exemplo)
pip3 install psycopg2

# PASSO 1.5 - se o comando resultar em erro, executar o seguinte comando e voltar ao PASSO 1
sudo apt-get install libpq-dev python-dev

# PASSO 2 - no ficheiro "query2db.cfg" colocar algo semelhante ao seguinte (user e pass à escolha, vamos criá-los de seguida)
[postgresql]
host=localhost
database=nome_bd
user=nome_user
password=pass_user

# PASSO 3 - no psql, criar (se ainda não estiver criado) um user para trabalhar com a BD
CREATE USER nome_user WITH PASSWORD 'pass_user';

# PASSO 4 - dar privilégios sober a BD ao user criado
GRANT ALL PRIVILEGES ON DATABASE nome_bd TO nome_user;

# PASSO 5 - estando na BD que queremos, dar privilégios ao user sobre as tabelas dessa BD
GRANT ALL PRIVILEGES ON TABLE nome_tabela TO nome_user;

# PASSO 6 - fora do psql e com o script python, ligar à BD e executar queries, como no seguinte exemplo
python3 query2db.py -q "SELECT * FROM nome_tabela;"
-----------------------------------------------------------------------------------------------------------------------------