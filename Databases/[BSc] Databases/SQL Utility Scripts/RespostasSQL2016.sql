--Frequência de 2016 (5.1 alínea a) "No dia 25 de abril de 2016, qual foi o valor total (€) recebido na mesa 26 (CodMesa=26)?"
Select X.Valor
From (Select R.CodMesa AS Mesa, Sum(P.Preco*PP.Qtd_Pedida) AS Valor
	  From Refeicao R, Produto P, PedidoProd PP, Pedido D
	  Where D.CodRef=R.CodRef AND PP.CodPed=D.CodPed AND P.CodProd=PP.CodProd AND R.Data_Refeicao='25-04-2016'
	  Group By R.CodMesa) AS X
Where X.Mesa=20

--Frequência de 2016 (5.1 alínea b) "Obtenha os nomes (Nome) dos empregados que receberam, pelo menos, 10 pedidos no dia 25 de abril de 2016"
Select E.Nome
From Empregado E, (Select Emp.CodEmp, COUNT(*) AS NumPed
				   From Empregado Emp, Pedido P, Refeicao R
				   Where Emp.CodEmp=P.CodEmp AND P.CodRef=R.CodRef AND R.Data_Refeicao='25-04-2016'
				   Group By Emp.CodEmp) AS X
Where E.CodEmp=X.CodEmp AND X.NumPed>10

--Frequência de 2016 (5.1 alínea c) "Obtenha as mesas (CodMesa) que no dia 25 de abril de 2016 receberam mais refeições que a mesa 26"
Select Distinct R.CodMesa
From Refeicao R, (Select CodMesa, Count(*) AS NumRef
				  From Refeicao R
				  Where R.CodMesa<>26 AND R.Data_Refeicao='25-04-2016'
				  Group By CodMesa) AS X
Where R.CodMesa=X.CodMesa AND X.NumRef>(Select Count(*)
										 From Refeicao R
										 Where R.CodMesa=26 AND R.Data_Refeicao='25-04-2016')

--Frequência de 2016 (5.1 alínea d) "Obtenha a mesa (CodMesa) onde foi servida a maior quantidade de refeições no dia 25 de abril de 2016"
Select X.CodMesa AS 'Resultado'
From (Select R.CodMesa, Count(*) AS NumRef
	  From Refeicao R
	  Where R.Data_Refeicao='25-04-2016'
	  Group By R.CodMesa) AS X
Where X.NumRef=(Select Max(Y.NumRef)
				 From (Select Count(*) AS NumRef
					   From Refeicao R
					   Where R.Data_Refeicao='25-04-2016'
					   Group By R.CodMesa) AS Y)

--Exame Normal de 2016 (4.1 alínea a) "Liste os produtos (CodProd) que não foram pedidos no dia 25 de abril de 2016"
Select X.CodProd
From (Select Distinct CodProd
	  From Produto
	  EXCEPT
	  (Select Distinct P.CodProd
	   From Produto P, Refeicao R, Pedido PE, PedidoProd D
	   Where D.CodProd=P.CodProd AND PE.CodPed=D.CodPed AND R.CodRef=PE.CodRef AND R.Data_Refeicao='25-04-2016')) AS X

--Exame Normal de 2016 (4.1 alínea b) "Liste os produtos (CodProd) que nunca foram pedidos. Deve formular a instrução SQL sem usar funções de agregação"
Select P.Designacao
From Produto P, (Select Distinct CodProd
	  From Produto
	  EXCEPT
	  (Select Distinct P.CodProd
	   From Produto P, Refeicao R, Pedido PE, PedidoProd D
	   Where D.CodProd=P.CodProd AND PE.CodPed=D.CodPed AND R.CodRef=PE.CodRef)) AS X
Where P.CodProd=X.CodProd

--Exame Normal de 2016 (4.1 alínea c) "Liste a quantidade de refeições servidas em cada mesa"
Select R.CodMesa, Count(*) AS NumRef
From Refeicao R
Group By R.CodMesa

--Exame Normal de 2016 (4.1 alínea d) "Indique a mesa (CodMesa) onde foram servidas mais refeições no dia 25 de abril de 2016"
Select X.CodMesa
From (Select R.CodMesa, Count(*) AS NumRef
	  From Refeicao R
	  Where R.Data_Refeicao='25-04-2016'
	  Group By R.CodMesa) AS X
Where X.NumRef=(Select Max(Y.Total)
				From (Select Count(*) AS Total
				      From Refeicao R
					  Where R.Data_Refeicao='25-04-2016'
					  Group By R.CodMesa) AS Y)