from flask import redirect , render_template , request , session , Blueprint , url_for , flash
from app import db
from app.models import Task

task_bp = Blueprint('tasks' , __name__)

@task_bp.route('/')
def view():
    if 'user' not in session :
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html' , tasks=tasks)


@task_bp.route('/add' , methods = ['POST'])
def add():

    if 'user' not in session :
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title :
        new_tasks = Task(title = title , status = 'Pending')
        db.session.add(new_tasks)
        db.session.commit()
        flash('TASK ADD SUCCESSFULLY' , 'success')
    return redirect(url_for('tasks.view'))

@task_bp.route('/toggle/<int:task_id>' , methods = ['POST'])
def toggle(task_id):
    tasks = Task.query.get(task_id)
    if tasks:
        if tasks.status == 'Pending':
            tasks.status = 'Working'
        elif tasks.status == 'Working':
            tasks.status = 'Done'
        else:
            tasks.status = 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view'))


@task_bp.route('/clear' , methods = ['POST'])
def clear_task():
    Task.query.delete()
    db.session.commit()
    flash('All Record Are Deleted' , 'info')
    return redirect(url_for('tasks.view'))


