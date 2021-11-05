# Copyright 2021 sunehabose
# MIT License

import sys
import unittest
sys.path.insert(0, 'code')
import code.user_cli 

class TestUserCLI(unittest.TestCase):
    
    def test_user_menu(self) -> None:
        code.user_cli.user_menu()


