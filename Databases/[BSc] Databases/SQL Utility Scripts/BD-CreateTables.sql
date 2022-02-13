
-------------------------------------------------------------------------------
-- USE DBProject: Changes the database context to the DBProject database.
--
USE Restaurante
--
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
-- Criar as tabelas
-- (create the database tables)
-------------------------------------------------------------------------------

if not exists (select * from dbo.sysobjects 
               where id = object_id(N'[dbo].[Empregado]') )
begin
  CREATE TABLE Empregado (
	  CodEmp int NOT NULL 
	     CHECK (CodEmp >= 1),                    -- constraint type: check
      Nome nvarchar (30)  NOT NULL ,            -- NULL Column
	  Data_Admissão nvarchar (30) NOT NULL		-- com o formato "dd-mm-aaaa"
          
  ); 
    
end

-- ............................................................................

if not exists (select * from dbo.sysobjects 
               where id = object_id(N'[dbo].[Produto]') )
begin
  CREATE TABLE Produto (
	  CodProd int NOT NULL 
	     CONSTRAINT PK_EmpNum PRIMARY KEY (CodProd)
	     CHECK (CodProd >= 1),
	  Designacao nvarchar (50) NOT NULL ,
	  Qtd_Stock int NOT NULL
		 DEFAULT 0,
	  Preco decimal(10,2) NOT NULL 
	     DEFAULT 0.0 
	     CHECK (Preco >= 0.0),
  ); 
end

-- ............................................................................
if not exists (select * from dbo.sysobjects 
               where id = object_id(N'[dbo].[Refeicao]') )
begin
  CREATE TABLE Refeicao (
	  CodRef int NOT NULL 
	     CHECK (CodRef >= 1),
	  Data_Refeicao nvarchar (30) NOT NULL,		-- com o formato "dd-mm-aaaa"
	  Hora_Inicio int NOT NULL 
	     CHECK (Hora_Inicio >= 1),
	  Hora_Fim int NOT NULL 
	     CHECK (Hora_Fim >= 0),
	  CodMesa int NOT NULL 
	     CHECK (CodMesa >= 1),
	  CodEmp int NOT NULL 
	     CHECK (CodEmp >= 1),   
	  
  );
end

-- ............................................................................
if not exists (select * from dbo.sysobjects 
               where id = object_id(N'[dbo].[Pedido]') )
begin
  CREATE TABLE Pedido (
	  CodPed int NOT NULL 
	     CHECK (CodPed >= 1),
	  Hora int NOT NULL 
	     CHECK (Hora >= 1),
	  CodRef int NOT NULL 
	     CHECK (CodRef >= 0),
	  CodEmp int NOT NULL 
	     CHECK (CodEmp >= 1),   
	  
  );
end

-- ............................................................................
if not exists (select * from dbo.sysobjects 
               where id = object_id(N'[dbo].[PedidoProd]') )
begin
  CREATE TABLE PedidoProd (
	  CodPed int NOT NULL 
	     CHECK (CodPed >= 1),
	  CodProd int NOT NULL 
	     CHECK (CodProd >= 1),
	  Qtd_Pedida int NOT NULL 
	     CHECK (Qtd_Pedida >= 1),
	  Qtd_Consumida int NOT NULL 
	     CHECK (Qtd_Consumida >= 1),  
	  
  );
end