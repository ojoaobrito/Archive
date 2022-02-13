--exercicio 14
SELECT TOP 1 E.Nome
FROM Atribuicao A, Empregado E
WHERE A.EmpNum=E.EmpNum
GROUP BY E.nome
ORDER BY COUNT(*) DESC

--exercicio 14 feito de uma forma mais poderosa
SELECT nome, NGroup
FROM (SELECT nome, COUNT(*) AS NGroup
     FROM Atribuicao
     GROUP BY nome) AS X
WHERE NGroup > 1

--exercicio 15
SELECT TOP 1 D.nome
FROM (SELECT D.nome, COUNT(D.categoria)
     FROM Departamento D
     GROUP BY D.nome
     ORDER BY COUNT(D.categoria) DESC) AS X