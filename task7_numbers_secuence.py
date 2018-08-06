class NumbSeq():
    def __init__(self, numb):
        self.numb = numb


    def exponentiation(self):
        res = []
        for i in range(1, self.numb):
            if i * i < self.numb:
                res.append(i)
            else:
                break
        return res

numb = int(input('Put in number: '))
seq = NumbSeq(numb)
print(seq.exponentiation())