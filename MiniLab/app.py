from flask import render_template, Blueprint

luke = Blueprint('luke', __name__)

class Intro:
    name = "Luke"

intro = Intro()

@luke.route("/luke")
def lukeRoute():
    return render_template("Introduction.html", name=intro.name)