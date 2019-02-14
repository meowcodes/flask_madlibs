"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["animal", "gerund", "adjective", "plural_noun", "verb", "noun"],
    """Long ago there was a {animal} that enjoyed {gerund} {adjective} {plural_noun}.  It never {verb} for {noun}."""
)

story3 = Story(
    ["number", "animal", "city", "past_tense_verb", "dessert"],
    """{number} years ago {animal} took over the {city} observatory. Everyone {past_tense_verb} {dessert} in celebration."""
)

story_dict = {
    "story1": story1,
    "story2": story2,
    "story3": story3
}