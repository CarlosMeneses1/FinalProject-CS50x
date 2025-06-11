from flask import Flask, render_template, session, request, redirect, jsonify
from flask_session import Session
from sqlalchemy import create_engine, text
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Configure sessions
app.config["SESSION_TYPE"] = "filesystem"   # Configure session storage type
app.config["SESSION_PERMANENT"] = False     # Configure session permanence type
Session(app)

# Connect and configure databases with SQLAlchemy
db = create_engine("sqlite:///prohabit.db", echo=True)

# Before any request, ensure user session
@app.before_request
def require_login():
    """ Ensure log in by the user """

    routes = ["/", "/add_habit", "/track_habit"]
    if session.get("user_id") is None and request.path in routes:
        return redirect("/login")


@app.route("/")
def index():
    """ Show your habits """

    # User reached route via GET (as by clicking a link or by redirect)

    # Connect to database
    conn = db.connect()

    # 1. Get user habits information
    user_habits = conn.execute(text("SELECT * FROM habits WHERE user_id = :user_id"), {"user_id": session["user_id"]}).mappings().fetchall()

    # 2. Get 'completed times' of a habit
    track_habit = conn.execute(text("SELECT habit_id, COUNT(*) AS completed FROM users JOIN habits ON users.id = habits.user_id JOIN habit_logs ON habits.id = habit_logs.habit_id WHERE users.id = :user_id GROUP BY habit_logs.habit_id"), {"user_id": session["user_id"]}).mappings().fetchall()

    return render_template("index.html", user_habits=user_habits, track_habit=track_habit)


@app.route("/logout")
def logout():
    """ Log user out """
    
    # Forget any user_id
    session.clear()

    # Redirect to route("/login")
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register a new user """

    # User reached route via POST (as by submitting a 'register from' via POST)
    if request.method == "POST":

        # Get information from the 'register form' to validate a unique username
        form_data = request.json

        # Connect to database
        conn = db.connect()

        # Search into the database for the username submitted in the 'register form'
        user_information = conn.execute(text("SELECT username FROM users WHERE username = :username"), {"username": form_data["username"]}).fetchone()

        # If the submitted username is found in the database, send an error message
        if user_information:
            return jsonify({"message": "Existing username. Try another one."}), 400 
        
        # Else, add into the database the new username
        hash_password = generate_password_hash(form_data["password"])

        conn.execute(text("INSERT INTO users (username, password) VALUES (:username, :password)"), {"username": form_data["username"], "password": hash_password})
        conn.commit()

        # Get the registered user ID and remember it with 'session'
        user_id = conn.execute(text("SELECT * FROM users WHERE username = :username"), {"username": form_data["username"]}).fetchone()

        session["user_id"] = user_id[0]

        # Disconnect from the database
        conn.close()

        # Once a new username is added, redirect to the route("/")
        return jsonify({"success": True, "redirect_url": "/"})

    # User reached route via GET (as by clicking a link or by a redirect)
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in """

    # User reached via POST (as by submitting a 'Log in form' via POST)
    if request.method == "POST":

        # Get the information from 'Log in form' to validate a correct combination of username and password
        form_data = request.json

        # Connect to database  
        conn = db.connect()

        # Search into database the username submitted in the 'log in form'
        user_information = conn.execute(text("SELECT * FROM users WHERE username = :username"), {"username": form_data["username"]}).fetchone()

        # Validate for existing username in database
        if not user_information:
            return jsonify({"message": "Username does not exist"}), 400
        
        # Validate for submitted password
        if not check_password_hash(user_information[2], form_data["password"]):
            return jsonify({"message": "Incorrect password"}), 400

        # Log user in
        session["user_id"] = user_information[0]

        # Disconnect from the database
        conn.close()

        # Once a username log in, redirect to the route("/")
        return jsonify({"redirect_url": "/"})

    else:
        return render_template("login.html")


@app.route("/add_habit", methods=["POST"])
def add_habit():
    """ Add new habits into database """

    # Get the information from 'habit form' to add it into the database
    data_habit = request.json

    # Connect to database
    conn = db.connect()

    # Add information into the database
    conn.execute(text("INSERT INTO habits (habit, frequency, times, user_id) VALUES (:habit, :frequency, :times, :user_id)"), {"habit": data_habit["habit"], "frequency": data_habit["frequency"], "times": data_habit["times"], "user_id": session["user_id"]})
    conn.commit()

    # Dissconect from database
    conn.close()

    return jsonify({"success": True}), 200


@app.route("/track_habit", methods=["POST"])
def track_habit():
    """ Update the database when a habit is completed """

    # Get the information from 'habit form' to add it into the database
    track_habit = request.json

    # Connect to database
    conn = db.connect()

    # Add information into the database
    conn.execute(text("INSERT INTO habit_logs (habit_id, date, completed) VALUES (:habit_id, DATE('now'), TRUE)"), {"habit_id": track_habit["habit_id"], })
    conn.commit()

    # Dissconect from database
    conn.close()
    
    return jsonify({"success": True}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5002)
