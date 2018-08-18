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

    def create_board(self):
        matrix = []
        sizing = range(0, self.size)
        for i in sizing:
            row = []
            for j in sizing:
                if (j - i) % 2 == 1:
                    row.append(' ')
                else:
                    row.append(self.symbol)
            matrix.append(row)
        return matrix

    def print_board(self):
        matrix = self.create_board()
        for row in matrix:
            print(' '.join(row))


def validate_params(args):
    params_validator.validate_lst(args, 3)
    params_validator.validate_positive_int(args[1])
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