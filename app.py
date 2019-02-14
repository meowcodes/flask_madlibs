from flask import Flask, request, render_template
from stories import story_dict
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


@app.route("/")
def story_choice():
    """Shows list of story templates"""

    return render_template("madlib-list.html", story_dict=story_dict)


@app.route("/form")
def generate_form():
    """Shows MadLib form input words"""

    chosen_story = find_story_in_dict(request, "chosen-story")

    return render_template("madlib-form.html", chosen_story_name=request.args.get("chosen-story"), chosen_story=chosen_story)


@app.route("/story")
def generate_story():
    """Generates story from submitted data."""

    chosen_story = find_story_in_dict(request, "chosen-story")

    return render_template("madlib-story.html", complete_story=chosen_story.generate(request.args))


def find_story_in_dict(req, story_name):
    """Finds and returns story with info from request"""

    return story_dict[req.args.get(story_name)]