import unittest
from code.browser_output import content_formatter

class TestBrowserOutput(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_content_output_format(self):
        """
        Asserts that content s returned as per the html format for browser output
        """

        i = open('./test/data/test_browser_input.txt')
        input_data = i.read().splitlines()  # List with stripped line-breaks
        i.close()
        o = open('./test/data/test_browser_output.txt')
        output_data = o.read()  # List with stripped line-breaks
        o.close()

        result = content_formatter(input_data)
        assert result is not None


    if __name__ == "__main__":
        unittest.main()
