from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "big secret"

@app.route("/")
def index():
    return render_template("index.html",name="world")


@app.route("/<string:name>")
def salute(name):
    name = f"{name}"
    return render_template("index.html", name=name)


@app.route("/isitchristmas")
def christmas():
    import datetime as dt
    now = dt.datetime.now()
    xmas = now.month == 12 and now.day == 25
    return render_template("xmas.html", xmas=xmas)


@app.route("/names")
def names():
    names = ["Han", "Luke", "Yoda"]
    return render_template("names.html", names=names)


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/abc")
def abc():
    return render_template("form.html")


@app.route("/hello", methods=["POST"])
def hello():
    names = []
    name = request.form.get("name")
    names.append(name)
    return render_template("names.html", names=names)
    

notes = []
@app.route("/notetaking", methods=["POST", "GET"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("notes.html", notes=session["notes"])