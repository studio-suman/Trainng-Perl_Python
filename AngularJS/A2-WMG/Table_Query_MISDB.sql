create table users (
    id int primary key,
    name varchar(25),
    contactNumber varchar(20),
    password varchar(250),
    status varchar(250),
    role varchar(250)
)

-- drop table customers;

insert into users
    (ID,name,contactNumber,password,status,role)
values
    (1 ,'Suman Saha' ,55555555 ,'sumansaha1' ,'active','admin');

select * from users