# Copyright 2021 auto_anki
# MIT License

import unittest
from code.google_search import get_people_also_ask_links

class TestGoogleSearch(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_people_also_ask_links(self):
        """Test the get_people_also_ask_links method"""
        test = "principal components"
        result = get_people_also_ask_links(test)
        self.assertEqual(list, type(result))
