from flask import Flask, render_template, request, redirect, session
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import smtplib
import resend

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

# SEND PASSWORD RESET EMAIL
def send_reset_email(name, email, reset_token):

    receiver_email = email
    resend.api_key = os.environ.get("RESEND_API_KEY")

    base_url = base_url = base_url = "https://online-quiz-management-system-1mqm.onrender.com"

    reset_url = f"{base_url}/reset-password/{reset_token}"

    subject = "Reset Your Password"

    html_message = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">

        <h2>Password Reset Request</h2>

        <p>Hello <b>{name}</b>,</p>

        <p>
            We received a request to reset your password
            for your Online Quiz Management System account.
        </p>

        <p>Click the button below to create a new password:</p>

        <br>

        <a href="{reset_url}"
           style="background-color:#2563eb;
                  color:white;
                  padding:12px 20px;
                  text-decoration:none;
                  border-radius:6px;
                  display:inline-block;">
            Reset Password
        </a>

        <br><br>

        <p>
            If you did not request a password reset,
            you can ignore this email.
        </p>

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

        print("Password reset email sent:", response)

        return True

    except Exception as e:

        print("Password reset email failed:", e)

        return False

def send_admin_request(name, email, phone, user_id):
    receiver_email = os.environ.get("ADMIN_EMAIL")
    resend.api_key = os.environ.get("RESEND_API_KEY")

    base_url = "https://online-quiz-management-system-1mqm.onrender.com"

    # Generate secure approval token
    import secrets
    approval_token = secrets.token_urlsafe(32)

    # Save token in database
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE users SET approval_token = %s WHERE id = %s",
        (approval_token, user_id)
    )

    db.commit()

    cursor.close()
    db.close()

    # Approval links using secure token
    approve_url = f"{base_url}/admin/approve/{approval_token}"
    reject_url = f"{base_url}/admin/reject/{approval_token}"

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

@app.route("/admin/approve/<approval_token>")
def approve_admin(approval_token):

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id FROM users "
        "WHERE approval_token = %s "
        "AND role = 'admin' "
        "AND admin_status = 'pending'",
        (approval_token,)
    )

    user = cursor.fetchone()

    if not user:
        cursor.close()
        db.close()
        return "Invalid or already used approval link!"

    cursor.execute(
        "UPDATE users SET admin_status = 'approved', approval_token = NULL "
        "WHERE id = %s",
        (user["id"],)
    )

    db.commit()

    cursor.close()
    db.close()

    return "Admin approved successfully! You can now login."


@app.route("/admin/reject/<approval_token>")
def reject_admin(approval_token):

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id FROM users "
        "WHERE approval_token = %s "
        "AND role = 'admin' "
        "AND admin_status = 'pending'",
        (approval_token,)
    )

    user = cursor.fetchone()

    if not user:
        cursor.close()
        db.close()
        return "Invalid or already used rejection link!"

    cursor.execute(
        "UPDATE users SET admin_status = 'rejected', approval_token = NULL "
        "WHERE id = %s",
        (user["id"],)
    )

    db.commit()

    cursor.close()
    db.close()

    return "Admin request rejected successfully."

# ADD QUESTION
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
            (question, option_a, option_b, option_c, option_d,
             correct_answer, created_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            session["user_id"]
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

    if session["user_id"] == 2:
        # The Main Admin will be able to see all the questions.
        cursor.execute(
            "SELECT * FROM questions ORDER BY id DESC"
        )
    else:
        # The teacher will only see their own questions.
        cursor.execute(
            """
            SELECT * FROM questions
            WHERE created_by = %s
            ORDER BY id DESC
            """,
            (session["user_id"],)
        )

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

    # The Main Admin will be able to edit all questions.
    if session["user_id"] == 2:
        cursor.execute(
            "SELECT * FROM questions WHERE id=%s",
            (id,)
        )
    else:
        # A teacher can only edit their own questions.
        cursor.execute(
            """
            SELECT * FROM questions
            WHERE id=%s AND created_by=%s
            """,
            (id, session["user_id"])
        )

    question_data = cursor.fetchone()

    if not question_data:
        cursor.close()
        db.close()
        return "You are not allowed to edit this question!"

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



# FORGOT PASSWORD
@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, name, email FROM users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        if not user:
            cursor.close()
            db.close()
            return "Email not found!"

        import secrets

        reset_token = secrets.token_urlsafe(32)

        cursor.execute(
            "UPDATE users SET reset_token = %s WHERE id = %s",
            (reset_token, user["id"])
        )

        db.commit()

        cursor.close()
        db.close()

        send_reset_email(
            user["name"],
            user["email"],
            reset_token
        )

        return "Password reset link has been sent to your email."

    return render_template("forgot_password.html")

# RESET PASSWORD
@app.route("/reset-password/<reset_token>", methods=["GET", "POST"])
def reset_password(reset_token):

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name FROM users WHERE reset_token = %s",
        (reset_token,)
    )

    user = cursor.fetchone()

    if not user:
        cursor.close()
        db.close()
        return "Invalid or expired password reset link!"

    if request.method == "POST":

        new_password = request.form["password"]

        hashed_password = generate_password_hash(new_password)

        cursor.execute(
            "UPDATE users SET password = %s, reset_token = NULL WHERE id = %s",
            (hashed_password, user["id"])
        )

        db.commit()

        cursor.close()
        db.close()

        return redirect("/login")

    cursor.close()
    db.close()

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reset Password</title>
    </head>

    <body>

        <h2>Reset Password</h2>

        <form method="POST">

            <input
                type="password"
                name="password"
                placeholder="Enter new password"
                required
            >

            <br><br>

            <button type="submit">
                Set New Password
            </button>

        </form>

    </body>
    </html>
    """

# CREATE LIVE QUIZ
@app.route("/create_live_quiz", methods=["GET", "POST"])
def create_live_quiz():
    if "user_id" not in session or session["role"] != "admin":
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # Main Admin sees all questions
    if session["user_id"] == 2:
        cursor.execute("SELECT * FROM questions ORDER BY id DESC")
    else:
        cursor.execute(
            """
            SELECT * FROM questions
            WHERE created_by = %s
            ORDER BY id DESC
            """,
            (session["user_id"],)
        )

    questions = cursor.fetchall()

    if request.method == "POST":
        quiz_title = request.form["quiz_title"]
        selected_questions = request.form.getlist("question_ids")

        import random
        game_pin = str(random.randint(100000, 999999))

        cursor.execute(
            """
            INSERT INTO live_quizzes
            (teacher_id, game_pin, quiz_title)
            VALUES (%s, %s, %s)
            """,
            (session["user_id"], game_pin, quiz_title)
        )

        live_quiz_id = cursor.lastrowid

        for question_id in selected_questions:
            cursor.execute(
                """
                INSERT INTO live_quiz_questions
                (live_quiz_id, question_id)
                VALUES (%s, %s)
                """,
                (live_quiz_id, question_id)
            )

        db.commit()

        cursor.close()
        db.close()

        return f"Quiz Created! Game PIN: {game_pin}"

    cursor.close()
    db.close()

    return render_template(
        "create_live_quiz.html",
        questions=questions
    )

# JOIN LIVE QUIZ
@app.route("/join_live_quiz", methods=["GET", "POST"])
def join_live_quiz():
    if "user_id" not in session or session["role"] != "student":
        return redirect("/login")

    if request.method == "POST":
        game_pin = request.form["game_pin"]

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM live_quizzes WHERE game_pin=%s AND status='waiting'",
            (game_pin,)
        )

        quiz = cursor.fetchone()

        if not quiz:
            cursor.close()
            db.close()
            return "Invalid Game PIN or Quiz is not available!"

        cursor.execute(
            """
            INSERT IGNORE INTO live_quiz_participants
            (live_quiz_id, student_id)
            VALUES (%s, %s)
            """,
            (quiz["id"], session["user_id"])
        )

        cursor.execute(
            """
            SELECT q.*
            FROM questions q
            JOIN live_quiz_questions lq
            ON q.id = lq.question_id
            WHERE lq.live_quiz_id = %s
            """,
            (quiz["id"],)
        )

        questions = cursor.fetchall()

        cursor.close()
        db.close()

        return render_template(
            "live_quiz.html",
            quiz=quiz,
            questions=questions
        )

    return render_template("join_live_quiz.html")

# SUBMIT LIVE QUIZ
@app.route("/submit_live_quiz/<int:live_quiz_id>", methods=["POST"])
def submit_live_quiz(live_quiz_id):

    if "user_id" not in session or session["role"] != "student":
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT q.*
        FROM questions q
        JOIN live_quiz_questions lq
        ON q.id = lq.question_id
        WHERE lq.live_quiz_id = %s
    """, (live_quiz_id,))

    questions = cursor.fetchall()

    score = 0

    for question in questions:

        selected_answer = request.form.get(
            f"q{question['id']}"
        )

        correct_answer = question["correct_answer"]

        if selected_answer == correct_answer:
            score += 1

    total_questions = len(questions)

    cursor.close()
    db.close()

    return render_template(
        "live_result.html",
        score=score,
        total_questions=total_questions
    )

if __name__ == "__main__":
    app.run(debug=True)
