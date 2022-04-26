/*
    sudo -u postgres psql -f create_db.sql
*/

DROP DATABASE dados_acidentes;
DROP USER policia;
DROP USER hospital;
DROP USER entidade;
DROP USER super;

CREATE DATABASE dados_acidentes;

ALTER DATABASE dados_acidentes SET datestyle TO "ISO, DMY";

\c dados_acidentes

CREATE TABLE Distritos(
    IdDistrito serial PRIMARY KEY,
    Nome varchar( 80 ) NOT NULL
);

CREATE TABLE Concelhos(
    IdConcelho serial PRIMARY KEY,
    Nome varchar( 80 ) NOT NULL,
    IdDistrito integer REFERENCES Distritos( IdDistrito ) NOT NULL
);

CREATE TABLE Vias(
    IdVia serial PRIMARY KEY,
    Nome varchar( 80 ) NOT NULL,
    IdConcelho integer REFERENCES Concelhos( IdConcelho ) NOT NULL,
    Tipo varchar( 80 )
);

CREATE TABLE Acidentes(
    IdAcidente serial PRIMARY KEY,
    DataHora timestamp NOT NULL,
    IdVia integer REFERENCES Vias( IdVia ) NOT NULL,
    Natureza varchar( 80 ),
    Km integer,
    Mortos integer NOT NULL,
    FeridosGraves integer NOT NULL
);

/*
\d Distritos
\d Concelhos
\d Vias
\d Acidentes
*/

\copy Distritos from '/Users/joaobrito/Desktop/BD1/Bk_01_DadosUploaded/dados_processados/distritos.csv' DELIMITER '$' CSV HEADER;

\copy Concelhos from '/Users/joaobrito/Desktop/BD1/Bk_01_DadosUploaded/dados_processados/concelhos.csv' DELIMITER '$' CSV HEADER;

\copy Vias from '/Users/joaobrito/Desktop/BD1/Bk_01_DadosUploaded/dados_processados/vias.csv' DELIMITER '$' CSV HEADER;

\copy Acidentes from '/Users/joaobrito/Desktop/BD1/Bk_01_DadosUploaded/dados_processados/acidentes.csv' DELIMITER '$' CSV HEADER;

/* Policia */
CREATE USER policia WITH PASSWORD 'policia12345';
GRANT SELECT ON Distritos TO policia;
GRANT SELECT, INSERT ON Concelhos TO policia;
GRANT SELECT, INSERT, UPDATE ON Vias TO policia;
GRANT INSERT, UPDATE, SELECT ON Acidentes TO policia;

/* Hospital */
CREATE USER hospital WITH PASSWORD 'hospital12345';
GRANT SELECT ON Distritos TO hospital;
GRANT SELECT, INSERT ON Concelhos TO hospital;
GRANT SELECT ON Vias TO hospital;
GRANT UPDATE(Mortos), UPDATE(FeridosGraves), SELECT ON Acidentes TO hospital;

/* Entidade */
CREATE USER entidade WITH PASSWORD 'entidade12345';
GRANT SELECT ON Distritos TO entidade;
GRANT SELECT, INSERT ON Concelhos TO entidade;
GRANT SELECT ON Vias TO entidade;
GRANT SELECT ON Acidentes TO entidade;

/* Super User */
CREATE USER super WITH PASSWORD 'super12345';
GRANT ALL PRIVILEGES ON Distritos TO super;
GRANT ALL PRIVILEGES ON Concelhos TO super;
GRANT ALL PRIVILEGES ON Vias TO super;
GRANT ALL PRIVILEGES ON Acidentes TO super;

