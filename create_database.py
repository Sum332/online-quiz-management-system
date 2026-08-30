import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sumit@7028"
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS quiz_db")

    print("Database quiz_db created successfully!")

    cursor.close()
    connection.close()

except Exception as e:
    print("Error:", e)