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
    (2 ,'Sangeeta Saha' ,55555555 ,'sangeeta.25.@gmail.com','sangeetasaha1' ,'true','user')

update users set status = 'true' where id = 1;

select * from users

drop table users