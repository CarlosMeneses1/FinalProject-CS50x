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


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    """ Log user out """
    
    # Forget any user_id
    session.clear()

    # Redirect to the route("/login")
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

        # Connect to data base  
        conn = db.connect()

        # Search into database the username submitted in the 'log in form'
        user_information = conn.execute(text("SELECT * FROM users WHERE username = :username"), {"username": form_data["username"]}).fetchone()

        # Validate for existing username in database
        if not user_information:
            return jsonify({"message": "Username does not exist"}), 400
        
        # Validate for submitted password
        if not check_password_hash(user_information[2], form_data["password"]):
            return jsonify({"message": "Incorrect password"}), 400


        

        return redirect("/login")

    else:
        return render_template("login.html")
 

if __name__ == '__main__':
    app.run(debug=True, port=5002)
