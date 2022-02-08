from flask import Flask, request, render_template
from stories import Story, story, answers

app = Flask(__name__)

@app.route('/')
def get_form():
    prompts = story.prompts
    return render_template('base.html', prompts=prompts)

@app.route('/madlib')
def get_madlib():
    madlib = story.generate(request.args)
    return render_template('madlib.html', madlib=madlib)