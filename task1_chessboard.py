class ChessBoard:
    __size = 8
    __symbol = '*'

    def print_board(self):
        matrix = []
        sizing = range(0, self.__size)
        for i in sizing:
            row = []
            for j in sizing:
                if (j - i) % 2 == 1:
                    row.append(' ')
                else:
                    row.append(self.__symbol)
            matrix.append(row)

        for row in matrix:
            print(''.join(row))

def main():
    chess = ChessBoard()
    chess.print_board()

if __name__ == '__main__':
    main()