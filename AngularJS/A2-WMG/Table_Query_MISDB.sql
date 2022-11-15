create table users (
    id INT NOT NULL IDENTITY(1,1) primary key,
    name varchar(25),
    contactNumber varchar(20),
    email varchar(250),
    password varchar(250),
    status varchar(250),
    role varchar(250)
)

insert into users
    (name,contactNumber,email,password,status,role)
values
    ('Subrata Sarkar' ,55555555 ,'subrata.sarkar4@gmail.com','subratasarkar1' ,'true','user')

update users set contactNumber = '77777777' where id = 3

select * from [dbo].[users]

delete from users where id = 4

drop table users
