import mysql.connector

# to install mysql connector run the following:
# pip install mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gigi123",
    database="testdatabase"
    )

mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE testdatabase")

# mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
# mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)


# mycursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

# student_sql_query = "INSERT INTO student(id,name) VALUES(01, 'John')"
# employee_sql_query = " INSERT INTO employee (id, name, salary) VALUES (01, 'Jane', 10000)"
#Execute cursor and pass query as well as student data
# mycursor.execute(student_sql_query)
# #Execute cursor and pass query of employee and data of employee
# mycursor.execute(employee_sql_query)
# db.commit()
print(mycursor.rowcount, "Record Inserted")