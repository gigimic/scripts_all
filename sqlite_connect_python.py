import sqlite3
from employee import Employee

# creates a database if it doesnt exist or connect to it if it exists
# conn = sqlite3.connect('employee.db')

# The following statement connects to a db in RAM, 
# so a new one is created each time we run it

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# create a table in the database employee.db. If there is table exists in the db
# the following command throws an error

c.execute(""" CREATE TABLE employees(
        first text,
        last text,
        pay integer
        )""")

c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 5000)")

emp_1 = Employee('John', 'Doe', 800)
emp_2 = Employee('Jane', 'Doe', 200)

#Next two statements are the same, use either of these
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))
c.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp_1.first, emp_1.last, emp_1.pay))

conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
{'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

conn.commit()

c.execute("SELECT * FROM employees WHERE last='Schafer'")
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE first=:first", {'first':'Jane',})
print(c.fetchall())


conn.commit()

conn.close()
