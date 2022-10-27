create table users (
    id int primary key,
    name varchar(25),
    contactNumber varchar(20),
    email varchar(250),
    password varchar(250),
    status varchar(250),
    role varchar(250)
)

insert into users
    (ID,name,contactNumber,email,password,status,role)
values
    (3 ,'Subrata Sarkar' ,55555555 ,'subrata.sarkar4@gmail.com','subratasarkar1' ,'true','user')

update users set contactNumber = '77777777' where id = 3

select * from [dbo].[users]

drop table users

SELECT sp.name
    , sp.default_database_name
FROM sys.server_principals sp
WHERE sp.name = SUSER_SNAME();

ALTER LOGIN db WITH DEFAULT_DATABASE = [MIS_DB];

Select * from sys.sysdatabases