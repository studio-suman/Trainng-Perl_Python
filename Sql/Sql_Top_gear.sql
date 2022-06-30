/*
Sql Top Gear L1 Exercise. Pls note due to issue with Livesql(oracle) timeouts I have migrated the tables to my sql server and hence [scott.emp]
and [scott.dept] are added
*/
--Select *
select * from [scott.emp]
--Select *
select * from [scott.dept]
--1) List the emps who are senior to their own manager.
select e.ENAME, m.ENAME as manager_name from [scott.emp] e join [scott.emp] m on e.EMPNO=m.MGR where e.HIREDATE>m.HIREDATE
--2) List the emps whose sal greater than blakes sal
select * from [scott.emp] where SAL > (select SAL from [scott.emp] where ENAME = 'BLAKE');
--3) List the dept 10 emps whose sal>allen sal.
select top 10 DEPTNO,ENAME,EMPNO,JOB from [scott.emp] where SAL > (select SAL from [scott.emp] where ENAME = 'ALLEN');
--4) List the mgrs who are senior to king and who are junior to smith
select * from [scott.emp] where HIREDATE BETWEEN '17-DEC-80' AND '17-NOV-81';
--5) List the empno,ename,loc,sal,dname,loc of the all the emps belonging to king dept.
select a.EMPNO, a.ENAME, b.LOC, a.sal, b.DNAME from [scott.emp] a join [scott.dept] b on a.deptno=b.DEPTNO 
where a.Deptno IN (select a.DEPTNO from [scott.emp] a where a.ename='KING')
--6) List the emps whose salgrade are greater than the grade of miller. 
select * from [scott.emp] where SAL > (select SAL from [scott.emp] where ENAME = 'MILLER');
--7) List the emps who are belonging dallas or Chicago with the grade same as adamsor exp more than smith.
select distinct a.ENAME, a.EMPNO, a.DEPTNO, a.JOB, a.HIREDATE from [scott.emp] a, [scott.dept] b where a.DEPTNO in (select DEPTNO from [scott.dept] 
where LOC = 'DALLAS' or LOC = 'CHICAGO') 
and a.JOB = (select JOB from [scott.emp] where ENAME = 'ADAMS') or a.HIREDATE = (select HIREDATE from [scott.emp] where ENAME = 'SMITH'); 
--8) List the emps whose sal is same as ford or blake.
select top 10 DEPTNO,ENAME,EMPNO,JOB from [scott.emp] where SAL IN (select SAL from [scott.emp] where ENAME = 'BLAKE' OR ENAME = 'FORD');
--9) List the emps whose sal is same as any one of the following. 
--             a) Sal of any clerk of emp1 table.
select * from [scott.emp] where SAL IN (select SAL from [scott.emp] where JOB = 'CLERK');
--             b) Any emp of emp2 joined before 82. 
select * from [scott.emp] where year(HIREDATE)<'1982'
--             c) The total remuneration (sal+comm.) of all sales person of Sales dept belonging to emp3 table. 
select *, (SAL+COMM) as RENUMERATION from [scott.emp] where deptno='30';
--             d) Any Grade 4 emps Sal of emp 4 table. 
select ENAME, SAL as GRADE from [scott.emp]
--             e) Any emp Sal of emp5 table. 
select ENAME, SAL from [scott.emp];
--10) List the details of most recently hired emp of dept 30.
select * from [scott.emp] where HIREDATE = (select max(HIREDATE) from [scott.emp] where DEPTNO=30) and DEPTNO='30';
--11) List the highest paid emp of Chicago joined before the most  recently hired emp of grade 2.
select EMPNO, ENAME  from [scott.emp]
where SAL = ( select max(SAL) from [scott.emp] e, [scott.dept] d where e.DEPTNO =
d.DEPTNO and d.LOC = 'CHICAGO' and
HIREDATE=(select max(HIREDATE) from [scott.emp] e
));
--12) List the highest paid emp working under king.
select * from [scott.emp] where sal = (select max(sal) from [scott.emp] where MGR='7839') 
--13) List the empno,ename,deptno,loc of all the emps.
select a.EMPNO, a.ENAME,a.DEPTNO,b.LOC from [scott.emp] a full join [scott.dept] b on a.DEPTNO=b.DEPTNO;
--14) List the empno,ename,loc,dname of all the depts.,10 and 20. 
select a.EMPNO, a.ENAME, b.LOC, b.DNAME, a.DEPTNO from [scott.emp] a join [scott.dept] b on a.DEPTNO=b.DEPTNO where a.DEPTNO='10' or a.DEPTNO='20'; 
--15) List the empno, ename, sal, loc of the emps working at Chicago dallas with an exp>6ys.
select e.EMPNO, e.ENAME,e.SAL, d.LOC from [scott.emp] e, [scott.dept] d where e.DEPTNO=d.DEPTNO 
and d.LOC in ('CHICAGO', 'DALLAS') and DATEDIFF(mm, HIREDATE,SYSDATETIME())/12>6;
--16) List the emps along with loc of those who belongs to dallas ,newyork with sal ranging from 2000 to 5000 joined in 81.
select * from [scott.emp] e, [scott.dept] d where e.DEPTNO=d.DEPTNO and d.LOC in ('DALLAS','NEW YORK')
and YEAR(e.HIREDATE) = '1981' and e.SAL between '2000' and '5000';
--17) List the empno,ename,sal,grade of all emps 
select EMPNO, ENAME, SAL, SAL as GRADE from [scott.emp]
--18) List the grade 2 and 3 emp of Chicago 
select e.EMPNO, e.ENAME,e.SAL as GRADE, d.LOC from [scott.emp] e, [scott.dept] d where e.DEPTNO=d.DEPTNO 
and d.LOC = 'CHICAGO'
--19) List the emps with loc and grade of accounting dept or the locs dallas or Chicago with the grades 3 to 5 &exp >6y 
select e.ENAME,e.JOB as GRADE, d.LOC, d.DNAME from [scott.emp] e, [scott.dept] d where e.DEPTNO=d.DEPTNO 
and d.LOC = 'CHICAGO' or d.LOC = 'DALLAS' and DATEDIFF(mm, e.HIREDATE,SYSDATETIME())/12>6 and d.DNAME='ACCOUNTING';
--20) List the grades 3 emps of research and operations depts.. joined after 1987 and whose names should not be either miller or allen. 
select e.ENAME,e.JOB as GRADE, d.DNAME from [scott.emp] e, [scott.dept] d where e.DEPTNO=d.DEPTNO 
and YEAR(HIREDATE)>='1987' and d.DNAME in ('OPERATIONS','RESEARCH') and e.ENAME NOT IN ('MILLER','ALLEN');
--21) List the emps whose job is same as smith. 
select * from [scott.emp] where JOB in (select JOB from [scott.emp] where ENAME = 'SMITH');
--22)  List the emps who are senior to miller.
select * from [scott.emp] where HIREDATE > (select HIREDATE from [scott.emp] where ENAME = 'MILLER');
--23) List the emps whose job is same as either allen or sal>allen
select * from [scott.emp] where JOB in (select JOB from [scott.emp] where ENAME = 'ALLEN') 
or SAL > (select SAL from [scott.emp] where ENAME ='ALLEN');
--Group by clause
--1.	List the count and average salary for employees in department 20.
select count(EMPNO) as COUNT_ , avg(SAL) as AVGSAL_ from [scott.emp] where DEPTNO='20' group by SAL;
--2.	List names of employees who are older than 30 years in the company. 
select ENAME from [scott.emp] where DATEDIFF(mm,HIREDATE, SYSDATETIME())/12>30; 
--3.	List the employee name , hire date in the descending order of the hire date.
select ENAME,HIREDATE from [scott.emp] order by HIREDATE desc; 
--4.	List employee name, salary, PF, HRA, DA and gross; order the results in the ascending order of gross. HRA is 50% of the salary and DA is 30% of the salary.
select ENAME ,SAL,(SAL*50/100) as HRA , (SAL*30/100) as DA, ((SAL*12/100)+(SAL*30/100)) as PF 
,(SAL+SAL/100*15+SAL/100*10-SAL/100*5) AS GROSS FROM [scott.emp] order by GROSS asc;
--5.	List the department numbers and number of employees in each department
select DEPTNO, count(EMPNO) as COUNT_ from [scott.emp] group by DEPTNO;
--Joins  
--1.	List employee name, department number and their corresponding department name. 
select e.ENAME, e.DEPTNO, d.DNAME from [scott.emp] e join [scott.dept] d on e.DEPTNO=d.DEPTNO;
--2.	List employee name and their manager name
select e.ENAME, m.ENAME as MGRNAME from [scott.emp] e join [scott.emp] m on e.EMPNO=m.MGR;
--3.	List employees who work in Research department
select ENAME from [scott.emp] e join [scott.dept] d on e.DEPTNO=d.DEPTNO where d.DNAME = 'RESEARCH';
--4.	List all rows from EMP table and only the matching rows from DEPT table.
select * from [scott.emp] e left join [scott.dept] d on e.DEPTNO=d.DEPTNO;
--5.	 List all rows from EMP table and only the matching rows from DEPT table
select * from [scott.emp] e left join [scott.dept] d on e.DEPTNO=d.DEPTNO;
--SUBQUERIES
--1.	List employees whose job is same as that of Smith 
select * from [scott.emp] where JOB = (select JOB from [scott.emp] where ENAME = 'SMITH')
--2.	List employees who have joined after Adam 
select * from [scott.emp] where HIREDATE > (select HIREDATE from [scott.emp] where ENAME = 'ADAMS')
--3.	List employees who salary us greater than Scott’s salary 
select * from  [scott.emp] where SAL > (select SAL from [scott.emp] where ENAME = 'SCOTT')
--4.	List employees getting the max salary
select * from [scott.emp] where SAL = (select MAX(SAL) from [scott.emp])
--5.	List employees show salary is > the max salary in deptno 30 
select * from [scott.emp] where SAL > (select MAX(SAL) from [scott.emp] where DEPTNO = '30')
--6.	List all employees whose department and designation is same as that of employee with empno 7788.
select e.ENAME, d.DNAME from [scott.emp] e join [scott.dept] d on e.DEPTNO=d.DEPTNO where e.DEPTNO = (select DEPTNO from [scott.emp] where EMPNO = '7788')
and e.JOB = (select JOB from [scott.emp] where EMPNO = '7788')