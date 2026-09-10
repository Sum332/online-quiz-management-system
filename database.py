import os
import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME", "quiz_db")
    )

    return connection


if __name__ == "__main__":
    try:
        db = get_db_connection()
        print("Database connected successfully!")
        db.close()
    except Exception as e:
        print("Database connection failed:", e)