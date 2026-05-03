import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9337",
    database="db_project"
)
table_name = "Customer"
cursor = conn.cursor()

print("Connected successfully!")