import unittest
from code.gpt_prompting import get_gpt_answers

class TestGPTSearch(unittest.TestCase):

    def test_get_people_also_ask_links(self):
        """Test the get_people_also_ask_links method"""
        test = "principal components"
        result = get_gpt_answers(test)
        self.assertEqual(list, type(result))

if __name__ == '__main__':
    unittest.main()