import sys
from os import path

tasks_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(path.join(tasks_path, 'validator'))
import params_validator
from params_validation_error import ParamsValidationError


class ChessBoard:
    """" This class contains properties and methods in order to
    create and print chessboard.

    """

    def __init__(self, size, symbol):
        self.size = size
        self.symbol = symbol

    def get_cell(self, ind):
        return self.symbol if ind % 2 == 0 else ' '

    def create_board(self):
        sizing = range(self.size)
        matrix = [''] * self.size  # Generating board with empty lines
        for i in sizing:  # Filling each line using list comprehension
            matrix[i] = ' '.join([self.get_cell(i - j) for j in sizing])
        return '\n'.join(matrix)

    def print_board(self):
        print(self.create_board())


def validate_params(args):
    params_validator.validate_lst(args, 3)
    params_validator.validate_int_input(args[1])
    params_validator.validate_str(args[2])


def main():
    try:
        validate_params(sys.argv)
        size = int(sys.argv[1])  # number of cells in one row
        symbol = sys.argv[2]  # symbol for filling black cells
        chess = ChessBoard(size, symbol)
        chess.print_board()
    except ParamsValidationError as err:
        print(err)


if __name__ == '__main__':
    main()
