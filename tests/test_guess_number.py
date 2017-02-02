import unittest
from unittest.mock import patch, call
from GuessNumber import GuessNumber
import random


class TestGuessNumber(unittest.TestCase):

    @patch('GuessNumber.random_number', return_value = 3)
    @patch('GuessNumber.get_guess', side_effect = [5,2,3])
    @patch('builtins.print')
    def test_guess_number(self, mock_print, mock_input, mock_random):

        GuessNumber.play_game()

        expected_calls = [ call("Too high, guess again."), call("Too low, guess again"), call("Congratualations, you win!")]

        self.assertEqual(expected_calls, mock_print.call_args_list)

        #GuessNumber.play_game()
        #mock_print.assert_called_with("Congratualations, you win!")

        #GuessNumber.play_game()
        #mock_print.assert_called_with("Too low, guess again")

        #GuessNumber.play_game()
        #mock_print.assert_called_with("Thanks for playing")

if __name__ == '__main__':
    unittest.play_game()
