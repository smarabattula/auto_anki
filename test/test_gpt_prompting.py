import unittest
from code.gpt_prompting import get_gpt_answers

class TestGPTSearch(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def test_get_people_also_ask_links(self):
        """Test the get_people_also_ask_links method"""
        test = "principal components"
        result = get_gpt_answers(test)
        self.assertEqual(list, type(result))
