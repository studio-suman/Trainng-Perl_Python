-- =======================================================
-- Create Stored Procedure Template for Azure SQL Database
-- =======================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      <Suman Saha, , Suman>
-- Create Date: <31st October 2022, , >
-- Description: <Description, , >
-- =============================================
CREATE PROCEDURE addUser
(
    -- Add the parameters for the stored procedure here
	@id INT,
	@name VARCHAR(200),
	@contactNumber VARCHAR(200),
	@email VARCHAR(200),
	@password VARCHAR(200),
	@status VARCHAR(10),
	@role VARCHAR(10)
)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON

    -- Insert statements for procedure here
    INSERT INTO users
	(
	id,
	name,
	contactNumber,
	email,
	password,
	status,
	role
	)
	VALUES 
	(
	@id,
	@name,
	@contactNumber,
	@email,
	@password,
	@status,
	@role
	)
END
GO