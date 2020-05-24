from flask import render_template,redirect,url_for,flash,abort,request
from todoapp.forms import RegisterForm, LoginForm, TaskForm #,SearchForm

from todoapp import app,bcrypt,db
from todoapp.models import User, Task
from flask_login import login_user,current_user,logout_user,login_required


@app.route('/')
@login_required
def task():
    tasks = Task.query.filter_by(owner = current_user)
    return render_template('tasks.html', tasks = tasks)


@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('task'))
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = password_hash)
        db.session.add(user)
        db.session.commit()
        flash('You succesfully registered','success')
        return redirect(url_for('login'))
    return render_template('accounts/register_edit.html', form=form, title = 'Register')


@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('task'))
        else:
            flash('Something went wrong, please enter valid email and password', 'danger')

    return render_template('accounts/login.html',form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/post/create', methods = ['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task( title = form.title.data, description = form.description.data,deadline = form.deadline.data, owner = current_user)
        db.session.add(task)
        db.session.commit()
        flash('You succesfully create task', 'success')
        return redirect(url_for('task'))
    return render_template('create_update.html', form = form, title = 'Create Task')



@app.route('/tasks/<int:task_id>')
@login_required
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    return render_template('detail.html', title = task.title, task = task)



@app.route('/tasks/<int:task_id>/update', methods = ['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.deadline = form.deadline.data
        db.session.commit()
        flash('You successfully update task', 'success')
        return redirect(url_for('task_detail', task_id = task.id))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.deadline.data = task.deadline
    
    return render_template('create_update.html', form = form, title = 'Update Task')


@app.route('/tasks/<int:task_id>/delete', methods = ['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Your task succesfully deleted','success')
    return redirect(url_for('task'))



@app.route('/account')
@login_required
def account():
    return render_template('accounts/account.html', user = current_user)

@app.route('/account/<int:user_id>/update', methods = ['GET', 'POST'])
@login_required
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    form = RegisterForm()
    
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = password_hash
        db.session.commit()
        flash('You successfully edit your informations', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        form.password.data = user.password
    
    return render_template('accounts/register_edit.html', form = form, title = 'Update User')

@app.route('/account/<int:user_id>/delete', methods = ['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    tasks = Task.query.filter_by(owner = current_user)
    for task in tasks:
        db.session.delete(task)
    db.session.delete(user)
    db.session.commit()
    flash('Your account succesfully deleted','success')
    return redirect(url_for('register'))



# @app.route('/search', methods=['GET', 'POST'])
# @login_required
# def search():
#     searchForm = SearchForm()
#     tasks = Task.query.filter_by(owner = current_user)

#     if SearchForm.validate_on_submit():
#         found_tasks = tasks.filter_by(form.title_name)

#     return render_template('tasks.html', tasks = found_tasks, form = form )