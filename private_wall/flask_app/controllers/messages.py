from email import message
from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/post',methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "sender_id":  request.form['sender_id'],
        "reciever_id" : request.form['reciever_id'],
        "content": request.form['content']
    }
    Message.save(data)
    return redirect('/wall')

@app.route('/delete/message/<int:id>')
def delete_message(id):
    data = {
        "id": id
    }
    Message.delete(data)
    return redirect('/wall')