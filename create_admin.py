import mysql.connector
from werkzeug.security import generate_password_hash

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sumit@7028",
    database="quiz_db"
)

cursor = connection.cursor()

name = "Admin"
email = "admin@gmail.com"
password = "admin123"

hashed_password = generate_password_hash(password)

cursor.execute("""
    INSERT INTO users (name, email, password, role)
    VALUES (%s, %s, %s, %s)
""", (name, email, hashed_password, "admin"))

connection.commit()

print("Admin account created successfully!")

cursor.close()
connection.close()