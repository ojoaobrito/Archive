--TO USE SCRIP
--psql -U postgres postgres -f create_db.sql

-- DELETE PREVIOUS INSTANCES OF THE DATABASE AND ITS USERS
DROP DATABASE acidentes_db;

DROP USER user_acidentes_db;
CREATE USER user_acidentes_db WITH PASSWORD 'user123';

-- CREATE DATABASE
CREATE DATABASE acidentes_db;
\c acidentes_db

-- CREATE TABLE WITH RAW INFORMATION
CREATE TABLE Acidentes(
    IdAcidente bigserial PRIMARY KEY,
    DataOcorrencia varchar(40),
    DataFecho varchar(40),
    Natureza varchar( 200 ),
    EstadoOcorrencia varchar( 200 ),
    Distrito varchar( 20 ),
    Concelho varchar( 500 ),
    Freguesia varchar( 500 ),      
    Localidade varchar( 500 ),
    Latitude double precision,
    Longitude double precision,
    NumMeiosTerrestres integer,
    NumOperacionaisTerrestres integer,
    NumMeiosAereos integer,
    NumOperacionaisAereos integer
);

GRANT ALL PRIVILEGES ON DATABASE acidentes_db TO user_acidentes;

-- COPY DATA FROM 1GB OF DATA CSV
\copy Acidentes from 'dados.csv' DELIMITER '$' CSV HEADER;

/*
-- POSTGIS 
CREATE EXTENSION postgis;
SELECT AddGeometryColumn('acidentes', 'geom', 4326, 'POINT', 2); 
UPDATE acidentes SET geom = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326);*/