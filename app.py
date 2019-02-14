from flask import Flask, request, render_template
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


@app.route("/")
def generate_form():
    """Shows MadLib form input words"""

    q_list = story.prompts

    return render_template("madlib-form.html", q_list=q_list)


@app.route("/story")
def generate_story():
    """Generates story from submitted data."""

    return render_template("madlib-story.html", complete_story=story.generate(request.args))