--TO USE SCRIPT
--psql -U postgres postgres -f queries.sql

\c acidentes_db;

--QUERY 1 - BTREE
EXPLAIN ANALYZE SELECT * FROM Acidentes WHERE NumMeiosTerrestres > 1 AND NumMeiosTerrestres < 4 AND NumMeiosAereos > 1 AND NumMeiosAereos < 3;

--QUERY 2 - BTREE
EXPLAIN ANALYZE SELECT * FROM Acidentes WHERE NumOperacionaisTerrestres < 3;

--QUERY 3 - HASH
EXPLAIN ANALYZE SELECT * FROM Acidentes WHERE IdAcidente = 406700;

--QUERY 4 - HASH
EXPLAIN ANALYZE SELECT * FROM Acidentes WHERE Concelho = 'covilha';

--QUERY 5 - BRIN
EXPLAIN ANALYZE SELECT Natureza FROM Acidentes WHERE IdAcidente > 100 and IdAcidente < 20000;

--QUERY 6 - BRIN
EXPLAIN ANALYZE SELECT IdAcidente FROM Acidentes WHERE NumOperacionaisTerrestres < 2;