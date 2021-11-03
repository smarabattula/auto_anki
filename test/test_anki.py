# Copyright 2021 sunehabose

from os import name
from genanki import deck
import unittest

from code.anki import get_deck, get_model


class TestAnki(unittest.TestCase):
    def test_get_model(self) -> None:
        get_model()

    def test_get_deck(self):
        my_deck = get_deck(deck_name='Test Deck Name')
        self.assertEqual(deck , type(my_deck))