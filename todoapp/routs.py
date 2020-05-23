from flask import render_template,redirect,url_for,flash
from todoapp.forms import RegisterForm, LoginForm

from todoapp import app,bcrypt,db
from todoapp.models import User
from flask_login import login_user,current_user,logout_user,login_required



tasks = [
    {
        'title' : 'Task 1',
        'description' : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1",
        'deadline' : '23 May 14:00',
        'author' : 'Sara'
    },
    {
        'title' : 'Task 2',
        'description' : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1",
        'deadline' : '23 May 14:00',
        'author' : 'Ruhin'
    },
    {
        'title' : 'Task 3',
        'description' : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1",
        'deadline' : '23 May 14:00',
        'author' : 'Murad'
    }
]

@app.route('/')
@login_required
def task():
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
    return render_template('accounts/register.html', form=form)

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