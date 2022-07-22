from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.email import Email

#create 
@app.route('/create', methods = ['POST'])
def create_email():
    if not Email.validate(request.form):
        return redirect("/")
    Email.save(request.form)
    return redirect("/success")

#read
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def show_all():
    emails = Email.get_all()
    return render_template("success.html", emails = emails)
