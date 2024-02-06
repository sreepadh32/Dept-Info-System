from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import mysql.connector




app = Flask(__name__)


department = {
    "name": "Computer Science Department",
    "description": "The Computer Science Department is dedicated to the advancement of knowledge in the field of computer science and its applications.",
    "professors": [
        {
            "name": "Professor A",
            "email": "professor_a@example.com",
            "research_interests": ["Machine Learning", "Deep Learning"]
        },
        {
            "name": "Professor B",
            "email": "professor_b@example.com",
            "research_interests": ["Natural Language Processing", "Computer Vision"]
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html" )

@app.route("/Faculty")
def Faculty():
    return render_template("Faculty.html", department=department)

if __name__ == "__main__":
    app.run(debug=True)