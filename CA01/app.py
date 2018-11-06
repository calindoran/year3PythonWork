from flask import Flask, render_template, request

app = Flask(__name__)  # "dunder name".


@app.route("/")
@app.route("/displayform")
def display_form():
    return render_template("form.html", the_title="Tell me about yourself")


@app.route("/processform", methods=["POST"])
def process_form():
    name = request.form["thename"]
    age = request.form["theage"]
    loc = request.form["thelocation"]
    with open("webapp.log", "a") as lf:
        print(name, file=lf)
        print(age, file=lf)
        print(loc, file=lf)
    return render_template(
        "thanks.html", person_name=name, the_title="Thanks for your data!"
    )


app.run(debug=True)
