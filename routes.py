from flask_main import app,db
from flask import render_template,url_for,redirect
from models import Task
from datetime import datetime
import forms

@app.route("/")
def index():
    return render_template('index.html', title='Home')

@app.route("/chatbot")
def chat():
    return render_template('chatbot.html', title='Home')


@app.route("/sampleform",methods=['get','post'])
def sampleform():
    form=forms.SampleForm()
    if form.validate_on_submit():
        t=Task(title=form.title.data,date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('sampleform_output'))
    return render_template("sampleform.html",form=form)

@app.route("/sampleform_out")
def sampleform_output():
    t=Task.query.all()
    return render_template('sampleform_out.html',tasks=t)

@app.route("/edit/<int:task_id>",methods=['get','post'])
def edit(task_id):
    task=Task.query.get(task_id)
    form=forms.SampleForm()
    if task:
        if form.validate_on_submit():
            task.title=form.title.data
            task.date=datetime.utcnow()
            db.session.commit()
            return redirect(url_for("sampleform_output"))
        form.title.data=task.title
        return render_template("edit.html",form=form,task_id=task_id)
    return redirect(url_for("sampleform_output"))

@app.route("/delete/<int:task_id>",methods=['get','post'])
def delete(task_id):
    task=Task.query.get(task_id)
    if task:
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for("sampleform_output"))
    return redirect(url_for("sampleform_output"))
