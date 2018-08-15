import sys


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


def main():
    size = int(sys.argv[1])          # number of cells in one row
    symbol = sys.argv[2]             # symbol for filling black cells
    chess = ChessBoard(size, symbol)
    chess.print_board()
    print('This is a %s' % sys.argv[0])

if __name__ == '__main__':
    main()