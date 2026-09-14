from flask import Flask, render_template, request, redirect, session
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import smtplib
import resend

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

def send_admin_request(name, email, phone, user_id):
    receiver_email = os.environ.get("ADMIN_EMAIL")
    resend.api_key = os.environ.get("RESEND_API_KEY")

    base_url = "https://online-quiz-management-system-1mqm.onrender.com"

    approve_url = f"{base_url}/admin/approve/{user_id}"
    reject_url = f"{base_url}/admin/reject/{user_id}"

    subject = "New Admin Approval Request"

    html_message = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">

        <h2>New Admin Registration Request</h2>

        <p><b>Name:</b> {name}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Phone:</b> {phone}</p>

        <br>

        <a href="{approve_url}"
           style="background-color:#28a745;
                  color:white;
                  padding:12px 20px;
                  text-decoration:none;
                  border-radius:6px;
                  display:inline-block;">
            Approve Admin
        </a>

        &nbsp;&nbsp;

        <a href="{reject_url}"
           style="background-color:#dc3545;
                  color:white;
                  padding:12px 20px;
                  text-decoration:none;
                  border-radius:6px;
                  display:inline-block;">
            Reject Admin
        </a>

        <br><br>

        <p>Please click the appropriate button to approve or reject this admin request.</p>

    </body>
    </html>
    """

    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": [receiver_email],
            "subject": subject,
            "html": html_message
        })

        print("Admin approval email sent:", response)
        return True

    except Exception as e:
        print("Email sending failed:", e)
        return False

@app.route("/admin/resend-request/<int:user_id>")
def resend_admin_request(user_id):
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return redirect("/dashboard")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name, email, phone, admin_status "
        "FROM users WHERE id = %s AND role = 'admin'",
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    db.close()

    if not user:
        return "Admin user not found!"

    if user["admin_status"] != "pending":
        return "This admin request is not pending."

    send_admin_request(
        user["name"],
        user["email"],
        user["phone"],
        user["id"]
    )

    return "Approval email sent. Check PowerShell for email status."

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
        role = request.form["role"]

        hashed_password = generate_password_hash(password)

        db = get_db_connection()
        cursor = db.cursor()

        try:
            if role == "admin":
                admin_status = "pending"
            else:
                admin_status = "approved"

            cursor.execute(
                "INSERT INTO users (name, email, phone, password, role, admin_status) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (name, email, phone, hashed_password, role, admin_status)
            )

            db.commit()

            # Get newly created user's ID
            user_id = cursor.lastrowid

            # Send approval request only for Admin
            if role == "admin":
                send_admin_request(name, email, phone, user_id)

            return redirect("/login")

        except Exception as e:
            print("REGISTER ERROR:", e)
            return "Registration error. Check Render logs."
        
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

            # Admin approval check
            if user["role"] == "admin" and user["admin_status"] != "approved":
                return "Your admin request is still pending approval."

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["role"] = user["role"]

            # Role according to dashboard
            if user["role"] == "admin":
                return redirect("/admin")

            return redirect("/dashboard")

        return "Invalid email or password!"

    return render_template("login.html")

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
@app.route("/admin/set-quiz-time", methods=["POST"])
def set_quiz_time():

    if "user_id" not in session:
        return redirect("/login")

    if session.get("role") != "admin":
        return redirect("/dashboard")

    quiz_time = int(request.form["quiz_time"])

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE quiz_settings SET quiz_time = %s WHERE id = 1",
        (quiz_time,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect("/admin")


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
@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (session["user_id"],)
    )

    user = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template("profile.html", user=user)


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        bio = request.form["bio"]

        profile_pic = request.files.get("profile_pic")

        filename = None

        if profile_pic and profile_pic.filename:
            filename = secure_filename(profile_pic.filename)

            upload_folder = os.path.join(
                app.root_path,
                "static",
                "uploads"
            )

            os.makedirs(upload_folder, exist_ok=True)

            profile_pic.save(
                os.path.join(upload_folder, filename)
            )

        if filename:

            cursor.execute(
                """
                UPDATE users
                SET name = %s,
                    phone = %s,
                    bio = %s,
                    profile_pic = %s
                WHERE id = %s
                """,
                (
                    name,
                    phone,
                    bio,
                    filename,
                    session["user_id"]
                )
            )

        else:

            cursor.execute(
                """
                UPDATE users
                SET name = %s,
                    phone = %s,
                    bio = %s
                WHERE id = %s
                """,
                (
                    name,
                    phone,
                    bio,
                    session["user_id"]
                )
            )

        db.commit()

        cursor.close()
        db.close()

        session["user_name"] = name

        return redirect("/profile")

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (session["user_id"],)
    )

    user = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template(
        "edit_profile.html",
        user=user
    )

# ADMIN APPROVAL REQUESTS
@app.route("/admin/requests")
def admin_requests():
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return redirect("/dashboard")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name, email, phone "
        "FROM users "
        "WHERE role = 'admin' AND admin_status = 'pending' "
        "ORDER BY id DESC"
    )

    requests = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "admin_requests.html",
        requests=requests
    )

@app.route("/admin/approve/<int:user_id>")
def approve_admin(user_id):
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return redirect("/dashboard")
    if session.get("user_id") != 2:
        return "Only main admin can approve requests!"

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE users SET admin_status = 'approved' "
        "WHERE id = %s AND role = 'admin'",
        (user_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect("/admin/requests")

@app.route("/admin/reject/<int:user_id>")
def reject_admin(user_id):
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return redirect("/dashboard")

    if session.get("user_id") != 2:
        return "Only main admin can reject requests!"

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE users SET admin_status = 'rejected' "
        "WHERE id = %s AND role = 'admin'",
        (user_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect("/admin/requests")

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
    cursor.execute("SELECT quiz_time FROM quiz_settings WHERE id = 1")
    quiz_setting = cursor.fetchone()

    quiz_time = quiz_setting["quiz_time"] if quiz_setting else 10

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
        questions=questions,
        quiz_time=quiz_time
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