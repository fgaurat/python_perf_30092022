from flask import Flask,render_template
from TodoDAO import TodoDAO

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    

@app.route("/todos")
def show_todos():
    dao = TodoDAO()

    return render_template('todos.html',todos=list(dao.find_all()))