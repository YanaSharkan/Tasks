class FibRange:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        if type(self.min_num) is not int or type(self.max_num) is not int:
            raise ValueError('Invalid range')

    def calculate(self):
        fib_seq = []
        a, b = 1, 1
        for i in range(0, self.max_num - 1):
            a, b = b, a + b
            if self.max_num < a:
                break
            elif self.min_num < a:
                fib_seq.append(a)
        return fib_seq


try:
    my_seq = FibRange(2, 1000)
    print(my_seq.calculate())
except ValueError:
    print('Invalid arguments')








