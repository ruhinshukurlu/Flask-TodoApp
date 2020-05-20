from flask import Flask,render_template
app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__' :
    app.run(debug=True)
