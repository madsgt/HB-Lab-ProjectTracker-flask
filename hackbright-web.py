from flask import Flask, request, render_template, flash

import hackbright
import jinja2

app = Flask(__name__)

app.secret_key = 'super secret'


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", 
                            first=first, 
                            last=last,
                            github=github)
    return html

@app.route("/student_search")
def get_student_form():

    """Show form for searching for student"""

    return render_template("student_search.html")

@app.route("/student_addform")
def student_addform():
    return render_template("student_add.html")


@app.route("/student_add", methods=['POST'])
def student_add():

    """ Adds a student into the database"""
    first = request.form.get("first_name")
    last = request.form.get("last_name")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    flash("Successfully added Student")

    return render_template("student_confirmation.html", first=first, last=last, github=github)




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
