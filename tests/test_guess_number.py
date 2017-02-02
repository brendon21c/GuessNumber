import unittest
from unittest.mock import patch
from GuessNumber import GuessNumber
import random


class TestGuessNumber(unittest.TestCase):

    @patch('random.randint', return_value = 3)
    @patch('builtins.input', side_effect = [5,2,3])
    def test_guess_number(self, mock_input, mock_randint):

        GuessNumber.play_game()
