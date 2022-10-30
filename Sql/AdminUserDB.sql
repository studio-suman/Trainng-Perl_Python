-- Script to create SQL Authentication User in an Azure SQL DB
-- Switch to Master
CREATE LOGIN db_u WITH password='welcome@123'
GO

CREATE USER db_u FOR LOGIN db_u WITH DEFAULT_SCHEMA=[dbo] 
GO

-- Syntax for Azure Active Directory authentication contained database user (if you have configured your environment for Azure AD authentication)
-- CREATE USER [userid@domain.com] FROM EXTERNAL PROVIDER;


-- Switch to database
CREATE USER db_u FOR LOGIN db_u WITH DEFAULT_SCHEMA=[dbo]
GO

EXEC sp_addrolemember 'db_datareader', 'db_u';
GO

GRANT EXECUTE ON SCHEMA :: dbo TO db_u;

EXEC sp_addrolemember 'db_datawriter', 'db_u';
GO

DROP LOGIN [db_u]
GO

