--exercício 1
SELECT Nome, Categoria
FROM Empregado

--exercício 2
SELECT *
FROM Empregado
WHERE Categoria='Programador'

--exercício 3
SELECT Nome
FROM Empregado
WHERE Categoria='Programador'

--exercício 4
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Colaborador' or Funcao='Coordenador'

--exercício 5
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Colaborador'
INTERSECT
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Coordenador'

--exercício 6
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Coordenador'
EXCEPT
(SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Colaborador'
INTERSECT
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Coordenador')

--exercício 7
SELECT *
FROM Empregado, Departamento
WHERE Empregado.DepNum=Departamento.DepNum

--exercício 8
SELECT Empregado.Nome, Departamento.Nome
FROM Empregado, Departamento
WHERE Empregado.DepNum=Departamento.DepNum

--exercício 9
SELECT distinct A.EmpNum
FROM Atribuicao A, Atribuicao B
WHERE A.ProjNum <> B.ProjNum --"<>" siginifica "diferente"
and A.EmpNum = B.EmpNum
