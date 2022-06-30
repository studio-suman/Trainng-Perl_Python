CREATE TABLE [dbo].[Users] (
    [EmployeeID]   INT           NOT NULL,
    [FullName]     VARCHAR (90)  NOT NULL,
    [EmailAddress] VARCHAR (50)  NULL,
    [Access]       VARCHAR (50)  NOT NULL,
    [AccessKey]    VARCHAR (255) NOT NULL,
    [Time]         VARCHAR (50)  NULL,
    PRIMARY KEY CLUSTERED ([EmployeeID] ASC)
);

