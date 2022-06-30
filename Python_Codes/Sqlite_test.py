import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute(''' SELECT count('pay') FROM sqlite_master WHERE type='table' AND name='employees' ''')

if c.fetchone()[0]==0 : {
c.execute("""CREATE TABLE employees (
				first text,
				last text,
				pay integer
				)""")
}

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

				  
# def delete_table(table):
	# with conn:
		# c.execute('DROP TABLE from', (table,))
	
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

#delete_table('employees')

conn.close()