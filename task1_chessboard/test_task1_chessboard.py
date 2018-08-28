import unittest
import task1_chessboard
from params_validation_error import ParamsValidationError


class TestTask1Chessboard(unittest.TestCase):

    data_set_error1 = []
    data_set_error2 = ['', '1', '']
    data_set_error3 = ['', 'a', '#']
    data_set_success = ['', '8', '*']

    def test_params_not_specified(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task1_chessboard.build_chessboard(self.data_set_error1)
        self.assertEqual('Not enough arguments specified', str(exception_context.exception))

    def test_invalid_symbol(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task1_chessboard.build_chessboard(self.data_set_error2)
        self.assertEqual('Argument should be non-empty string', str(exception_context.exception))

    def test_invalid_sizing(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task1_chessboard.build_chessboard(self.data_set_error3)
        self.assertEqual('Argument should be a positive int', str(exception_context.exception))

    def test_chessboard_success(self):
        chessboard = task1_chessboard.build_chessboard(self.data_set_success)
        self.assertIn(self.data_set_success[2], chessboard)


if __name__ == '__main__':
    unittest.main()
