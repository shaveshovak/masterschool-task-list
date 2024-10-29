from flask import Flask, render_template, request, redirect, url_for
from db import db  # Import db here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with the app context
db.init_app(app)

# Import models only after db has been initialized
with app.app_context():
    from models import ToDo  # Move the import inside the app context

# Define routes here
@app.route('/')
def index():
    tasks = ToDo.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        new_task = ToDo(task=task_text)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update_task(task_id):
    task = ToDo.query.get(task_id)
    if task:
        task.done = not task.done
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = ToDo.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
