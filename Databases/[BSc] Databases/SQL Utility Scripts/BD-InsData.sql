-------------------------------------------------------------------------------
-- USE DBProject: Changes the database context to the DBProject database.
--
USE Restaurante
--
-------------------------------------------------------------------------------
--
-------------------------------------------------------------------------------
------------  INSERT SOME DATA INTO TABLES  -----------------------------------
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
------------- Transaction mode: autocommit
-------------------------------------------------------------------------------

INSERT INTO Empregado(CodEmp, Nome, Data_Admissao) 
Values (1, 'José', '12-03-2015');

INSERT INTO Empregado(CodEmp, Nome, Data_Admissao) 
Values (2, 'Mário', '24-03-2015');

INSERT INTO Empregado(CodEmp, Nome, Data_Admissao) 
Values (3, 'Aníbal', '01-01-2015');

INSERT INTO Empregado(CodEmp, Nome, Data_Admissao) 
Values (4, 'Ricardo', '31-12-2015');

INSERT INTO Empregado(CodEmp, Nome, Data_Admissao) 
Values (5, 'Vítor', '19-08-2013');

INSERT INTO Empregado(CodEmp, Nome, Data_Admissao) 
Values (6, 'Paulinho', '05-10-2014');

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (1, 'Bife de Novilho', 10 , 20);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (2, 'Perna de Porco', 4 , 50);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (3, 'Ervilha', 89 , 1);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (4, 'Esparguete', 243 , 0.5);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (5, 'Caviar', 2 , 400);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (6, 'Alface', 10 , 7);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (7, 'Brócolo', 17 , 14);

INSERT INTO Produto(CodProd, Designacao, Qtd_Stock, Preco) 
Values (8, 'Beringela', 8 , 24);

INSERT INTO Refeicao(CodRef, Data_Refeicao, Hora_Inicio, Hora_Fim, CodMesa, CodEmp) 
Values (1, '25-04-2016', 19 , 22 , 26 , 4);

INSERT INTO Refeicao(CodRef, Data_Refeicao, Hora_Inicio, Hora_Fim, CodMesa, CodEmp) 
Values (2, '25-04-2016', 18 , 23 , 20 , 3);

INSERT INTO Refeicao(CodRef, Data_Refeicao, Hora_Inicio, Hora_Fim, CodMesa, CodEmp) 
Values (3, '25-04-2016', 19 , 24 , 22 , 5);

INSERT INTO Refeicao(CodRef, Data_Refeicao, Hora_Inicio, Hora_Fim, CodMesa, CodEmp) 
Values (4, '25-04-2016', 22 , 23 , 26 , 1);

INSERT INTO Pedido(CodPed, Hora, CodRef, CodEmp) 
Values (1, 19, 1 , 5);

INSERT INTO Pedido(CodPed, Hora, CodRef, CodEmp) 
Values (2, 21, 1 , 4);

INSERT INTO Pedido(CodPed, Hora, CodRef, CodEmp) 
Values (3, 20, 2 , 1);

INSERT INTO Pedido(CodPed, Hora, CodRef, CodEmp) 
Values (4, 21, 3 , 5);

INSERT INTO Pedido(CodPed, Hora, CodRef, CodEmp) 
Values (5, 22 , 4 , 2);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (1, 8 , 4 , 2);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (2, 2 , 1 , 1);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (3, 5 , 4 , 2);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (4, 3 , 20 , 19);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (5, 3 , 31 , 31);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (6, 3 , 40 , 1);

INSERT INTO PedidoProd(CodPed, CodProd, Qtd_Pedida, Qtd_Consumida) 
Values (7, 7 , 10 , 7);