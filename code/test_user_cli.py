# Copyright 2021 sunehabose
# MIT License

import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, 'code')
import user_cli 

class TestUserCLI(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_user_menu_1(self, mock_input) -> None:
        user_cli.user_menu()

    @patch('builtins.input', return_value='2')
    def test_user_menu_2(self, mock_input) -> None:
        user_cli.user_menu()

    @patch('builtins.input', return_value='q')
    def test_user_menu_q(self, mock_input) -> None:
        with self.assertRaises(SystemExit) as cm:
            user_cli.user_menu()
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 0)

   
    


