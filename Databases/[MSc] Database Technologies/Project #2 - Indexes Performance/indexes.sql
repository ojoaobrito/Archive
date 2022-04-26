--TO USE SCRIPT
--psql -U postgres postgres -f indexes.sql

\c acidentes_db;

--BTREE
CREATE INDEX idx_acidentes_meios_terrestres_btree ON Acidentes(NumMeiosTerrestres,NumMeiosAereos);
CREATE INDEX idx_acidentes_operacionais_terrestres_btree ON Acidentes USING btree(NumOperacionaisTerrestres);

--HASH
CREATE INDEX idx_acidentes_id_hash ON Acidentes USING hash(IdAcidente);
CREATE INDEX idx_acidentes_concelhos_hash ON Acidentes USING hash(Concelho);

--BRIN
CREATE INDEX idx_acidentes_natureza_brin ON Acidentes USING brin(Natureza) WHERE IdAcidente > 100 and IdAcidente < 20000;
CREATE INDEX idx_acidentes_id_brin ON Acidentes USING brin(IdAcidente);
