--Frequ�ncia de 2016 (5.1 al�nea a) "No dia 25 de abril de 2016, qual foi o valor total (�) recebido na mesa 26 (CodMesa=26)?"
Select X.Valor
From (Select R.CodMesa AS Mesa, Sum(P.Preco*PP.Qtd_Pedida) AS Valor
	  From Refeicao R, Produto P, PedidoProd PP, Pedido D
	  Where D.CodRef=R.CodRef AND PP.CodPed=D.CodPed AND P.CodProd=PP.CodProd AND R.Data_Refeicao='25-04-2016'
	  Group By R.CodMesa) AS X
Where X.Mesa=20

--Frequ�ncia de 2016 (5.1 al�nea b) "Obtenha os nomes (Nome) dos empregados que receberam, pelo menos, 10 pedidos no dia 25 de abril de 2016"
Select E.Nome
From Empregado E, (Select Emp.CodEmp, COUNT(*) AS NumPed
				   From Empregado Emp, Pedido P, Refeicao R
				   Where Emp.CodEmp=P.CodEmp AND P.CodRef=R.CodRef AND R.Data_Refeicao='25-04-2016'
				   Group By Emp.CodEmp) AS X
Where E.CodEmp=X.CodEmp AND X.NumPed>10

--Frequ�ncia de 2016 (5.1 al�nea c) "Obtenha as mesas (CodMesa) que no dia 25 de abril de 2016 receberam mais refei��es que a mesa 26"
Select Distinct R.CodMesa
From Refeicao R, (Select CodMesa, Count(*) AS NumRef
				  From Refeicao R
				  Where R.CodMesa<>26 AND R.Data_Refeicao='25-04-2016'
				  Group By CodMesa) AS X
Where R.CodMesa=X.CodMesa AND X.NumRef>(Select Count(*)
										 From Refeicao R
										 Where R.CodMesa=26 AND R.Data_Refeicao='25-04-2016')

--Frequ�ncia de 2016 (5.1 al�nea d) "Obtenha a mesa (CodMesa) onde foi servida a maior quantidade de refei��es no dia 25 de abril de 2016"
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

--Exame Normal de 2016 (4.1 al�nea a) "Liste os produtos (CodProd) que n�o foram pedidos no dia 25 de abril de 2016"
Select X.CodProd
From (Select Distinct CodProd
	  From Produto
	  EXCEPT
	  (Select Distinct P.CodProd
	   From Produto P, Refeicao R, Pedido PE, PedidoProd D
	   Where D.CodProd=P.CodProd AND PE.CodPed=D.CodPed AND R.CodRef=PE.CodRef AND R.Data_Refeicao='25-04-2016')) AS X

--Exame Normal de 2016 (4.1 al�nea b) "Liste os produtos (CodProd) que nunca foram pedidos. Deve formular a instru��o SQL sem usar fun��es de agrega��o"
Select P.Designacao
From Produto P, (Select Distinct CodProd
	  From Produto
	  EXCEPT
	  (Select Distinct P.CodProd
	   From Produto P, Refeicao R, Pedido PE, PedidoProd D
	   Where D.CodProd=P.CodProd AND PE.CodPed=D.CodPed AND R.CodRef=PE.CodRef)) AS X
Where P.CodProd=X.CodProd

--Exame Normal de 2016 (4.1 al�nea c) "Liste a quantidade de refei��es servidas em cada mesa"
Select R.CodMesa, Count(*) AS NumRef
From Refeicao R
Group By R.CodMesa

--Exame Normal de 2016 (4.1 al�nea d) "Indique a mesa (CodMesa) onde foram servidas mais refei��es no dia 25 de abril de 2016"
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