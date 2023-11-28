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


from os import name
import genanki
import unittest

from anki import add_package, add_question, get_deck, get_model


class TestAnki(unittest.TestCase):

    def test_get_model(self) -> None:
        """
        Define model that describes the template
        for anki deck.

        Returns
        ------
        anki model
        """
        get_model()

    def test_get_deck(self):
        """
        Define and initialize an anki deck, where we can add cards.
        Returns
        ------
        anki deck
        """
        my_deck = get_deck(deck_name='Test Deck Name')
        self.assertEqual(genanki.deck.Deck , type(my_deck))

    def test_add_question(self):
        """
        Create a card for a question, answer pair.
        Returns
        ------
        anki card
        """
        model = get_model()
        note = add_question(question='Test Ques', answer='Ans', curr_model=model)
        self.assertEqual(genanki.Note, type(note))

    def test_add_package(self)-> None:
        """
        Create a package for a deck
        Returns
        ------
        None
        """
        my_deck = get_deck(deck_name='Test Deck Name')
        add_package(my_deck, 'output_name')
        pass
