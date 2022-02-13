--exercicio 1
SELECT DepNum, Count(*) AS NEmps --"AS" (...) é para dar nome à coluna
FROM Empregado
GROUP BY DepNum

--exercicio 2
SELECT DepNum, Count(*) AS NProgramadores
FROM Empregado
WHERE Categoria='Programador'
GROUP BY DepNum

--exercicio 3
SELECT D.Nome AS 'Nome de Departamento', Count(*) AS 'Quantidade de Empregados'
FROM Departamento D, Empregado E
WHERE D.DepNum=E.DepNum
GROUP BY D.Nome

--exercicio 4
SELECT D.nome, AVG(Salario), MIN(Salario), MAX(Salario) 
FROM Departamento D, Empregado E
WHERE E.DepNum=D.DepNum
GROUP BY D.DepNum, D.Nome --nem todos os atributos precisam de estar no SELECT, mas, se estiverem no SELECT, têm de estar aqui

--exercicio à parte
SELECT EmpNum, Count(*)
FROM Atribuicao
GROUP BY EmpNum, ProjNum --como o empregado 3 tem 2 projetos, aparece 2 vezes (são as combinações dos 2 atributos)

--exercicio 5
SELECT D.Nome, AVG(Salario)
FROM Departamento D, Empregado E
WHERE E.DepNum=D.DepNum
GROUP BY D.Nome
ORDER BY AVG(SALARIO) DESC

--exercicio 6
SELECT D.Nome, Count(*)
FROM Departamento D, Empregado E
WHERE E.DepNum=D.DepNum
GROUP BY D.Nome
HAVING Count(*)>=2
ORDER BY Count(*) DESC

--exercicio 8
SELECT D.Nome
FROM Departamento D, Empregado E
WHERE E.DepNum=D.DepNum
GROUP BY D.Nome
HAVING SUM(Salario) > (SELECT Avg(Salario) From Empregado)

--exercicio 9 ERRADO!!!
SELECT D.Nome, AVG(Salario)
FROM Departamento D, Empregado E
WHERE E.DepNum=D.DepNum AND E.Categoria='Programador'
GROUP BY D.Nome

--exercicio 9
SELECT D.Nome, AVG(Salario)
FROM Departamento D, Empregado E
WHERE E.DepNum=D.DepNum AND E.EmpNum IN (SELECT DepNum FROM Empregado WHERE Categoria='Programador')
GROUP BY D.Nome

--exercicio 11
SELECT D.nome
FROM Departamento D, Empregados E
WHERE E.DepNum=D.DepNum
GROUP BY D.nome
HAVING SUM(Salario) > (SELECT AVG(Salario)
		     FROM Departamento D, Empregado E
		     WHERE E.DepNum=D.DepNum AND E.EmpNum IN (SELECT DepNum FROM Empregado WHERE Categoria='Programador'))