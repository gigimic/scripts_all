import mysql.connector

# to install mysql connector run the following:
# pip install mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gigi123",
    # database="testdatabase"
    )

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE testdatabase")