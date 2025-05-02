from flask import Flask, render_template, session, request, redirect
from flask_session import Session
from sqlalchemy import create_engine, text


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
    return redirect("login")


@app.route("/register", methods=["GET", "POST"])
def register():
    return "TODO"

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    if request.method == "POST":

        # PRUEBA
        username = request.form.get("username")
        password = request.form.get("password")
        conn = db.connect()
        conn.execute(text("INSERT INTO users (username, password) VALUES (:username, :password)"), {"username": username, "password": password})
        conn.commit()
        conn.close()
        # PRUEBA

        return redirect("/login")

    else:
        return render_template("login.html")
 

if __name__ == '__main__':
    app.run(debug=True, port=5002)
