--Frequência de 2017 (4.2 alínea a) "Liste os fornecedores (CodFor) que forneceram todas as peças vermelhas"
Select Distinct CodFor
From Fornecimento F
Where Not Exists ( Select Distinct CodPec
				   From Peca
				   Where Cor='vermelha'
				   Except ( Select Distinct CodPec
						    From Fornecimento
							Where F.CodFor=CodFor ))

--Frequência de 2017 (4.2 alínea b) "Liste os códigos (CodPec) e as quantidades totais (Qtd) fornecidas de cada peça vermelha"
Select P.CodPec, SUM(F.Qtd)
From Peca P, Fornecimento F
Where F.CodPec=P.CodPec AND P.cor='vermelha'
Group By P.CodPec

--Frequência de 2017 (4.2 alínea c) "Indique o fornecedor (CodFor) que fez mais fornecimentos"
Select X.CodFor
From (Select CodFor, Count(*) AS Total
				    From Fornecimento
					Group By CodFor) AS X
Where X.Total=(Select Max(Total)
				From (Select Count(*) AS Total
				    From Fornecimento
					Group By CodFor) AS X)

--Frequência de 2017 (4.2 alínea d) "Liste as peças (Descricao) com mais de 10 componentes imediatos"
Select P.Descricao
From Peca P, (Select C.Maior, Count(*) AS NMenores
			  From Componente C, Peca P
			  Where C.Menor=P.CodPec
			  Group By C.Maior) AS X
Where P.CodPec=X.Maior AND X.NMenores>10

--Exame Normal de 2017 (6.2 alínea a) "Liste os fornecedores (CodFor) que forneceram todas as peças vermelhas"
Select Distinct CodFor
From Fornecimento F
Where Not Exists ( Select Distinct CodPec
				   From Peca
				   Where Cor='vermelha'
				   Except ( Select Distinct CodPec
						    From Fornecimento
							Where F.CodFor=CodFor ))

--Exame Normal de 2017 (6.2 alínea b) "Obtenha a descrição (Descricao) das peças que são compostas pela peça mais barata (e outras, eventualmente)"
Select Descricao 
From Peca
Where CodPec IN (Select Maior
				 From Componente
				 Where Menor in (Select CodPec
								  From Peca P
								  Where P.Preco=(Select MIN(Preco)
												 From Peca)))
--Exame Normal de 2017 (6.2 alínea c) "Indique a quantidade de peças vermelhas fornecidas por cada fornecedor (CodFor)"
Select CodFor, COUNT(*) AS "Total de Peças Vermelhas"
From Peca P, Fornecimento F
Where P.CodPec=F.CodPec AND P.cor='vermelha'
Group By CodFor

--Exame Normal de 2017 (6.2 alínea d) "Liste os fornecedores (CodFor) das peças compostas por, pelo menos, 5 peças vermelhas"
Select CodFor
From Fornecimento F, (Select C.Maior AS Pec, COUNT(*) AS Tot
				    From Componente C
					Where C.Menor IN (Select CodPec
								    From Peca
									Where cor='vermelha')
					Group By Maior) AS X
Where F.CodPec = X.Pec AND X.Tot>=1 

--Exame Recurso de 2017 (6.2 alínea a) "Liste os fornecedores (CodFor) que forneceram todas as peças vermelhas e, pelo menos, uma peça azul"
(Select Distinct CodFor
From Fornecimento F
Where Not Exists ( Select Distinct CodPec
				   From Peca
				   Where Cor='vermelha'
				   Except ( Select Distinct CodPec
						    From Fornecimento
							Where F.CodFor=CodFor ))) --fornecedores de todas as peças vermelhas
Intersect (Select X.CodFor
		   From (Select CodFor, Count(*) AS TotAzul
				 From Fornecimento F, Peca P
				 Where F.CodPec=P.CodPec AND P.Cor='azul'
				 Group By CodFor) AS X
		   Where X.TotAzul>=1) --fornecedores com pelo menos um fornecimento de uma peça azul

--Exame Recurso de 2017 (6.2 alínea b) "Indique o fornecedor (CodFor) que fez mais fornecimentos (independentemente da Qtd fornecida)"
Select X.CodFor
From (Select CodFor, Count(*) AS Total
				    From Fornecimento
					Group By CodFor) AS X
Where X.Total=(Select Max(Total)
				From (Select Count(*) AS Total
				    From Fornecimento
					Group By CodFor) AS X)

--Exame Recurso de 2017 (6.2 alínea b) - outra forma de fazer
Select TOP(1) CodFor
From Fornecimento, (Select COUNT(*) AS Total
					 From Fornecimento T
					 Group By CodFor) AS X
Order By Total Desc

--Exame Recurso de 2017 (6.2 alínea c) "Indique os fornecedores (CodFor) com um volume de negócio superior a 100 000€ (considerando todos os fornecimentos)"
Select X.CodFor, X.VolumeNeg AS "Volume de Negócios"
From (Select CodFor, Sum(P.preco*F.Qtd) AS VolumeNeg
	  From Fornecimento F, Peca P
	  Where F.CodPec=P.CodPec
	  Group By CodFor) AS X
Where X.VolumeNeg>100000

--Exame Recurso de 2017 (6.2 alínea d) "Sem usar funções de agregação, indique a descrição (Descricao) das peças compostas por, pelo menos, 2 peças vermelhas"
Select Distinct P1.Descricao
From Componente C1, Componente C2, Peca P1, Peca P2, Peca P3
Where P2.CodPec<>P3.CodPec AND P2.Cor='vermelha' AND P3.Cor='vermelha' AND C1.Maior=P1.CodPec AND C1.Menor=P2.CodPec AND C2.Maior=P1.CodPec AND C2.Menor=P3.CodPec
