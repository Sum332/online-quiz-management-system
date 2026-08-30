import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sumit@7028",
    database="quiz_db"
)

cursor = connection.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'student'
)
""")

# Questions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_answer VARCHAR(1) NOT NULL
)
""")

# Results table
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    score INT NOT NULL,
    total_questions INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

connection.commit()

print("All tables created successfully!")

cursor.close()
connection.close()