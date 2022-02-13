--exerc�cio 1
SELECT Nome, Categoria
FROM Empregado

--exerc�cio 2
SELECT *
FROM Empregado
WHERE Categoria='Programador'

--exerc�cio 3
SELECT Nome
FROM Empregado
WHERE Categoria='Programador'

--exerc�cio 4
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Colaborador' or Funcao='Coordenador'

--exerc�cio 5
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Colaborador'
INTERSECT
SELECT EmpNum
FROM Atribuicao
WHERE Funcao='Coordenador'

--exerc�cio 6
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

--exerc�cio 7
SELECT *
FROM Empregado, Departamento
WHERE Empregado.DepNum=Departamento.DepNum

--exerc�cio 8
SELECT Empregado.Nome, Departamento.Nome
FROM Empregado, Departamento
WHERE Empregado.DepNum=Departamento.DepNum

--exerc�cio 9
SELECT distinct A.EmpNum
FROM Atribuicao A, Atribuicao B
WHERE A.ProjNum <> B.ProjNum --"<>" siginifica "diferente"
and A.EmpNum = B.EmpNum
