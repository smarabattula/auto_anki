# Copyright 2021 auto_anki
# MIT License

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
