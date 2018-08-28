class NumSeq:
    def __init__(self, num):
        self.num = num

    def exponentiation(self):
        res = []
        for i in range(1, self.num):
            if i * i < self.num:
                res.append(i)

        return res


if __name__ == '__main__':
    num = int(input('Put in border number: '))
    seq = NumSeq(num)
    print(seq.exponentiation())

