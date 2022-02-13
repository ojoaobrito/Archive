CREATE LOGIN Joao WITH PASSWORD = 'Bases2018'
GO

IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = N'Joao')
BEGIN
    CREATE USER [Joao] FOR LOGIN [Joao]
    EXEC sp_addrolemember N'db_owner', N'Joao'
END;
GO