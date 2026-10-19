
from database import get_db_connection

questions = [
    {
        "question": "What is Python?",
        "option_a": "A programming language",
        "option_b": "An operating system",
        "option_c": "A database",
        "option_d": "A web browser",
        "correct_answer": "A",
        "explanation": "Python is a high-level, general-purpose programming language known for its readable syntax.",
        "exam_answer": "Python is a high-level, interpreted, general-purpose programming language. It supports procedural, object-oriented, and functional programming.",
    },
    {
        "question": "Who created Python?",
        "option_a": "Dennis Ritchie",
        "option_b": "Guido van Rossum",
        "option_c": "James Gosling",
        "option_d": "Bjarne Stroustrup",
        "correct_answer": "B",
        "explanation": "Guido van Rossum created Python and released its first public version in 1991.",
        "exam_answer": "Python was created by Guido van Rossum and first released in 1991.",
    },
    {
        "question": "Which extension is commonly used for Python source files?",
        "option_a": ".html",
        "option_b": ".java",
        "option_c": ".py",
        "option_d": ".css",
        "correct_answer": "C",
        "explanation": "The .py extension is commonly used for Python source-code files.",
        "exam_answer": "Python source files commonly use the .py file extension.",
    },
    {
        "question": "Which function displays output in Python?",
        "option_a": "input()",
        "option_b": "print()",
        "option_c": "show()",
        "option_d": "displayText()",
        "correct_answer": "B",
        "explanation": "The print() function writes output to the standard output stream.",
        "exam_answer": "The print() function is used to display output in Python.",
    },
    {
        "question": "Which symbol begins a single-line comment in Python?",
        "option_a": "//",
        "option_b": "/*",
        "option_c": "#",
        "option_d": "<!--",
        "correct_answer": "C",
        "explanation": "In Python, a # symbol begins a single-line comment.",
        "exam_answer": "Python uses the hash symbol (#) to begin a single-line comment.",
    },
]

db = None
cursor = None

try:
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM questions
        WHERE year = %s AND subject = %s AND chapter = %s
    """, (
        "3rd Year",
        "Python Programming",
        "Unit 1: Introduction"
    ))

    existing_count = cursor.fetchone()[0]

    if existing_count > 0:
        print(
            f"Questions already exist for this unit ({existing_count}). "
            "No questions were added to avoid duplicates."
        )
    else:
        for q in questions:
            cursor.execute("""
                INSERT INTO questions (
                    question, option_a, option_b, option_c, option_d,
                    correct_answer, created_by, year, subject, chapter,
                    explanation, exam_answer
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                q["question"],
                q["option_a"],
                q["option_b"],
                q["option_c"],
                q["option_d"],
                q["correct_answer"],
                2,
                "3rd Year",
                "Python Programming",
                "Unit 1: Introduction",
                q["explanation"],
                q["exam_answer"],
            ))

        db.commit()
        print("Successfully added 5 questions to Aiven MySQL.")

except Exception as e:
    if db:
        db.rollback()
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if db:
        db.close()
