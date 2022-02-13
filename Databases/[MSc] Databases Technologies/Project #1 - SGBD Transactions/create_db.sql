/* import data from within psql - "\i path_to_sql" */

DROP DATABASE massiva;

CREATE DATABASE massiva;

CREATE USER user_acidentes WITH PASSWORD 'user123';

\c massiva;

CREATE TABLE pessoa(
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(30),
    apelido VARCHAR(30),
    morada VARCHAR(30), 
    concelho VARCHAR(30), 
    distrito VARCHAR(30), 
    sexo VARCHAR(1), 
    telemovel INTEGER, 
    email VARCHAR(30), 
    cc INTEGER, 
    nif INTEGER, 
    pass VARCHAR(30)
);

GRANT ALL PRIVILEGES ON DATABASE massiva TO user123;