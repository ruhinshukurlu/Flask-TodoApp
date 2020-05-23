from flask import render_template,redirect,url_for
from todoapp.forms import RegisterForm, LoginForm

from todoapp import app,bcrypt,db



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
def task():
    return render_template('tasks.html', tasks = tasks)

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = password_hash)
        db.session.add( user )
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('accounts/register.html', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('accounts/login.html',form = form)