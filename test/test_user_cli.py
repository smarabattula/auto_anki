# Copyright 2021 sunehabose
# MIT License

import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, 'code')
import code.user_cli 

class TestUserCLI(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_user_menu(self, mock_input) -> None:
        code.user_cli.user_menu()


