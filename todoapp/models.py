from todoapp import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    image = db.Column(db.String(120), nullable = True, default = 'iamges/profile.png')
    tasks = db.relationship('Task', backref = 'owner', lazy = True)

    def __repr__(self):
        return f'<User({self.username})>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable = False)
    deadline = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f'<Task({self.title}, {self.deadline})>'
         