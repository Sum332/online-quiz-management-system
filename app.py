from flask import Flask, render_template, request, redirect, session
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "quiz_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        db = get_db_connection()
        cursor = db.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (name, email, phone, password, role) VALUES (%s, %s, %s, %s, %s)",
                (name, email, phone, hashed_password, "student")
            )
            db.commit()
            return redirect("/login")

        except Exception:
            return "Email already registered!"

        finally:
            cursor.close()
            db.close()

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
 
        cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["role"] = user["role"]

            # Role according to dashboard
            if user["role"] == "admin":
                return redirect("/admin")

            return redirect("/dashboard")

        return "Invalid email or password!"

    return render_template("login.html")


# STUDENT DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "student":
        return redirect("/admin")

    return render_template(
        "dashboard.html",
        name=session["user_name"]
    )


# ADMIN DASHBOARD
@app.route("/admin")
def admin():
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return redirect("/dashboard")

    return render_template(
        "admin.html",
        name=session["user_name"]
    )

#ADD QUESTION
@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    if "user_id" not in session or session["role"] != "admin":
        return redirect("/login")

    if request.method == "POST":
        question = request.form["question"]
        option_a = request.form["option_a"]
        option_b = request.form["option_b"]
        option_c = request.form["option_c"]
        option_d = request.form["option_d"]
        correct_answer = request.form["correct_answer"]

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO questions
            (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer
        ))

        db.commit()
        cursor.close()
        db.close()

        return redirect("/admin")

    return render_template("add_question.html")

# VIEW QUESTIONS
@app.route("/view_questions")
def view_questions():
    if "user_id" not in session or session["role"] != "admin":
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM questions ORDER BY id DESC")
    questions = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "view_questions.html",
        questions=questions
    )


# EDIT QUESTION
@app.route("/edit_question/<int:id>", methods=["GET", "POST"])
def edit_question(id):
    if "user_id" not in session or session["role"] != "admin":
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":
        question = request.form["question"]
        option_a = request.form["option_a"]
        option_b = request.form["option_b"]
        option_c = request.form["option_c"]
        option_d = request.form["option_d"]
        correct_answer = request.form["correct_answer"]

        cursor.execute("""
            UPDATE questions
            SET question=%s,
                option_a=%s,
                option_b=%s,
                option_c=%s,
                option_d=%s,
                correct_answer=%s
            WHERE id=%s
        """, (
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            id
        ))

        db.commit()

        cursor.close()
        db.close()

        return redirect("/view_questions")

    cursor.execute(
        "SELECT * FROM questions WHERE id=%s",
        (id,)
    )

    question_data = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template(
        "edit_question.html",
        question=question_data
    )

# DELETE QUESTION
@app.route("/delete_question/<int:id>", methods=["POST"])
def delete_question(id):
    if "user_id" not in session or session["role"] != "admin":
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM questions WHERE id=%s",
        (id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect("/view_questions")

# SAVE ANSWER
@app.route("/save_answer", methods=["POST"])
def save_answer():

    if "user_id" not in session:
        return {"success": False}

    data = request.get_json()

    question_id = data["question_id"]
    answer = data["answer"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO quiz_answers
        (user_id, question_id, answer)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        answer = VALUES(answer)
    """, (
        session["user_id"],
        question_id,
        answer
    ))

    db.commit()

    cursor.close()
    db.close()

    return {"success": True}

# QUIZ
@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    # Login check
    if "user_id" not in session:
        return redirect("/login")

    # Admin cannot attempt quiz
    if session.get("role") == "admin":
        return redirect("/admin")

    # Only student can attempt quiz
    if session.get("role") != "student":
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # Get all questions
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    # SUBMIT QUIZ
    if request.method == "POST":

        score = 0

        for q in questions:

            answer = request.form.get("q" + str(q["id"]))

            if answer and q["correct_answer"]:
                if answer.strip().lower() == str(q["correct_answer"]).strip().lower():
                    score += 1

        # Save result
        cursor.execute(
            """
            INSERT INTO results (user_id, score, total_questions)
            VALUES (%s, %s, %s)
            """,
            (
                session["user_id"],
                score,
                len(questions)
            )
        )

        db.commit()

        cursor.close()
        db.close()

        return render_template(
            "result.html",
            score=score,
            total=len(questions)
        )

    # SHOW QUIZ
    cursor.close()
    db.close()

    return render_template(
        "quiz.html",
        questions=questions
    )

# ADMIN - VIEW STUDENT RESULTS
@app.route("/admin_results")
def admin_results():
    if "user_id" not in session:
        return redirect("/login")

    if session.get("role") != "admin":
        return  "You are not logged in as Admin"

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            results.id,
            users.name,
            users.email,
            results.score,
            results.total_questions
        FROM results
        JOIN users ON results.user_id = users.id
        ORDER BY results.id DESC
    """)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "admin_results.html",
        results=results
    )

# RESULT HISTORY
@app.route("/result_history")
def result_history():
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "student":
        return redirect("/admin")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, score, total_questions
        FROM results
        WHERE user_id = %s
        ORDER BY id DESC
    """, (session["user_id"],))

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "result_history.html",
        results=results
    )

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)