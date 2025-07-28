from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Add a new task
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        tasks.append({'title': title, 'done': False})
    return redirect(url_for('index'))

# Mark task as done
@app.route('/done/<int:task_id>')
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))


app.run()
