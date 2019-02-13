from flask import Flask, request, render_template
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

@app.route("/")
def generate_form():
    """Shows MadLib form input words"""

    q_list = story.prompts

    return render_template("madlib-form.html", q_list = q_list)


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )