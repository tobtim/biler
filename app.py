from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biler.sqlite3"

db = SQLAlchemy(app)


class biler(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    merke = db.Column("merke", db.String(100))
    modell = db.Column("modell", db.String(100))
    bilde = db.Column("bilde", db.String(100))
    årstall = db.Column("årstall", db.Integer)


def __init__(self, merke, modell, bilde, årstall):
    self.merke = merke
    self.modell = modell
    self.bilde = bilde
    self.årstall = årstall


@app.route("/")
def index():
    biler = db.engine.execute("SELECT * FROM biler ORDER BY årstall ASC")

    return render_template("index.html", biler=biler)


@app.route("/grid")
def grid():
    biler = db.engine.execute("SELECT * FROM biler ORDER BY årstall ASC")

    return render_template("grid.html", biler=biler)


@app.route("/fjell/<id>")
def bil(id):
    biler = db.engine.execute(f"SELECT * FROM biler WHERE id={id}")

    return render_template("bil.html", biler=biler)


app.run(debug=True)
