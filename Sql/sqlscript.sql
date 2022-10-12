

create table customers ( 
ID int not null , 
name varchar(10) not null, 
age int not null, 
Address char(25), 
sal decimal(18,2), 
primary key (ID) 
);

--desc customers


create table customers ( 
ID int not null , 
name varchar(10) not null, 
age int not null, 
Address char(25), 
sal decimal(18,2), 
primary key (ID) 
);

--desc customers


alter table customers ADD emailid varchar(25);

--desc customers


alter table customers DROP emailid;

alter table customers DROP column emailid;

--desc customers


alter table customers modify column Address varchar(25);

alter table customers MODIFY COLUMN Address varchar(25) not null;

alter table customers MODIFY COLUMN Address char(25) not null;

alter table customers MODIFY COLUMN address char(25) not null;

alter table customers MODIFY address char(25);

alter table customers MODIFY address varchar(25);

desc customers


drop table customers;

select * from customers;

desc customers


create table customers ( 
ID int not null , 
name varchar(10) not null, 
age int not null, 
Address char(25), 
sal decimal(18,2), 
primary key (ID) 
);

desc customers


insert into customers (ID,Name,Age,Address,Sal) values (1,nnnn,25,chennai,10000);

insert into customers (ID,Name,Age,Address,Sal) values (1,'nnnn',25,'chennai',10000);

insert into customers (ID,Name,Age,Address,Sal) values (2,'eeee',26,'Pune',100000);

insert into customers (ID,Name,Age,Address,Sal) values (3,'gas',29,'Mumbai',50000);

insert into customers (ID,Name,Age,Address,Sal) values (4,'from',35,'Bangalore',70000);

insert into customers (ID,Name,Age,Address,Sal) values (5,'nttt',55,'chennai',80000);

select * from customers;

insert into customers  values (6,'nyyt',45,'chennai',800000);

select * from customers;

create table customers1 ( 
ID int not null , 
name varchar(10) not null, 
age int not null, 
Address char(25), 
sal decimal(18,2), 
primary key (ID) 
);

insert into customers1 (ID,Name,Age,Address,Sal) select * from customers;

select * from customers1;

update customers set sal = 100000 ,Address = 'chennai';

select * from customers;

update customers set sal = 100000 ,Address = 'Pune' where Age = 35;

select * from customers;

delete from customers where age = 55;

select * from customers;

delete from customers;

select * from customers;

select * from scott.emp;

select empno,ename,job from scott.emp;

select distinct sal from scott.emp;

select count(*) from scott.emp;

select distinct count(sal) from scott.emp;

select distinct count(*) from scott.emp;

select count(*), distinct  sal from scott.emp;

select  distinct sal from scott.emp;

select  distinct (count(*)) from scott.emp;

select  count (distinct(job)) from scott.emp;

select * from scott.emp where sal >2000;

select * from scott.emp where sal >2000 AND Job = 'CLERK';

select * from scott.emp where sal >2000;

select * from scott.emp where sal >2000 AND Job = 'CLERK';

select * from scott.emp where sal >2000 OR Job = 'CLERK';

select * from scott.emp where deptno in (10,20,30,40,50);

select * from scott.emp where sal between 1000 and 3000;

select * from scott.emp where ename like 'A%';

select * from scott.emp where ename like '%S';

select * from scott.emp where ename like 'J%S';

select * from scott.emp where ename like 'a%';

select * from scott.emp where ename like 'A%' or ename like 'a%';

select * from scott.emp where ename like '%A%';

select * from scott.emp where job like '%ANG%';

select * from scott.emp where job like '%ang%';

select * from scott.emp where job like '%anag%';

select * from scott.emp where job like '%ANA%';

select * from scott.emp where ename like '_____';

select * from scott.emp where ename like '__A%';

select * from scott.emp where cast (sal as varchar(25)) like '%'5;

select * from scott.emp where cast (sal as varchar(25)) like '%5';

select * from scott.emp where rownum >=3;

select * from scott.emp where rownum <= 3;

select * from scott.emp where rownum <= 6;

select * from scott.emp where rownum <= 6 order by sal;

select * from scott.emp where rownum <= 6 order by sal desc;

select * from scott.emp where comm is null;

select * from scott.emp where comm is not null;

select * from scott.emp where comm is null;

select sum(sal),min(sal),max(sal),avg(sal),count(sal) from scott.emp where deptno in (10,20,30) group by sal ;

select sum(sal),min(sal),max(sal),avg(sal),count(sal) from scott.emp where deptno in (10,20,30) group by sal  order by sal;

select sum(sal),min(sal),max(sal),avg(sal),count(sal) from scott.emp where deptno in (10,20,30) group by sal  order by sal desc;

select sum(sal),min(sal),max(sal),avg(sal),count(sal) from scott.emp where deptno in (10,20,30) group by sal  having (sum(sal) > 5000) ;

select sum(sal),min(sal),max(sal),avg(sal),count(sal) from scott.emp where deptno in (10,20,30) group by sal  having count (*) > 1;

select empno,ename,sal from scott.emp order by ename;

select empno,ename,sal from scott.emp order by 2;