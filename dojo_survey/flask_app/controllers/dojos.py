from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo


@app.route('/')
def load():
    return render_template('index.html')

@app.route("/process", methods = ["POST"])
def process():
    if not Dojo.validate(request.form):
        return redirect('/')
    id = Dojo.save(request.form)
    return redirect(f'/result/{id}')

@app.route('/result/<int:id>')
def result(id):
    data = {'id': id}
    return render_template('return.html', dojo = Dojo.show(data))