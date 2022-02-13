--exercicio 1
SELECT COUNT(*)
FROM Empregado

--exercicio 2
SELECT COUNT(*)
FROM Empregado E
WHERE E.DepNum=2

--exercicio 3
SELECT COUNT(*)
FROM Empregado E
WHERE E.DepNum=(SELECT DepNum
				FROM Departamento
				WHERE Local='Covilh?')

--exercicio 4
SELECT Nome
FROM Departamento D

SELECT DepNum
FROM Empregado
--WHERE 

--exercicio 5
SELECT SUM(Salario)
FROM Empregado
WHERE DepNum=1

--exercicio 6
SELECT COUNT(DISTINCT Categoria)
FROM Empregado

--exercicio 8
SELECT MAX(Salario)
FROM Empregado

--exercicio 9       NOTA: NÃO DÁ PARA PÔR FUNÇÕES DE AGREGAÇÃO NA CLÁUSULA WHERE
SELECT Nome
FROM Empregado
WHERE Salario=(SELECT MIN(Salario) FROM Empregado)

--exercicio 10
SELECT AVG(Salario)
FROM Empregado
WHERE DepNum=1

--exercicio 11
SELECT Designacao
FROM Projecto
WHERE Fundos=(SELECT MAX(Fundos) FROM Projecto)

--exercicio 12
SELECT Nome
FROM Empregado E, Atribuicao A
WHERE (A.EmpNum=E.EmpNum) AND (A.ProjNum IN (SELECT ProjNum FROM Projecto WHERE Fundos=(SELECT MAX(Fundos) FROM Projecto)))

--exercicio 13
SELECT Nome
FROM Empregado E
WHERE Salario>(SELECT AVG(Salario) FROM Empregado WHERE DepNum=E.DepNum)
ORDER BY Nome DESC --a forma predefinida é a ascendente