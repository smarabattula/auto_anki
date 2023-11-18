# MIT License
#
# Copyright 2023 auto_anki
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import genanki
import os

def get_model():
    """
    Define an Anki flashcard model with fields for questions and answers suitable for use in the Anki flashcard application
    """
    my_model = genanki.Model(
        1607392319,
        'Anki Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])
    return my_model


def get_deck(deck_name):
    """
    Define and initialize an anki deck, where we can add cards.

    Returns
    ------
    anki deck
    """

    my_deck = genanki.Deck(
        2059400110,
        deck_name)
    return my_deck


def add_question(question, answer, curr_model):
    """
    Create a card for a question, answer pair.

    Returns
    ------
    anki card
    """

    my_note = genanki.Note(
        model=curr_model,
        fields=[question, answer])
    return my_note


def add_package(deck, output_fname):
    """
    Create a package for a deck

    Returns
    ------
    None
    """
    anki_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"anki_decks")
    if not os.path.exists(anki_path):
        os.makedirs(anki_path)
    genanki.Package(deck).write_to_file(f'{anki_path}/{output_fname}.apkg')
