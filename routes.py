from app import app
from flask import render_template
from models import Task

import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about', methods =['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title = form.title.data, date = datetime.utcnow())
        db.session.add(t)
        db.session.commit(t)
        print('Submitted title', form.title.data)
        return render_template('about.html', form = form, title = form.title.data)
    return render_template('about.html', form =form)