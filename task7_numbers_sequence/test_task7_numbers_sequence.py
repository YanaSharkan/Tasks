import unittest
import task7_numbers_sequence


class TestTask7NumbersSequence(unittest.TestCase):

    set_success = [1, 2, 3, 4, 5, 6, 7]

    def test_exponentiation_success(self):
        num = 56
        seq = task7_numbers_sequence.NumSeq(num)
        self.assertEqual(seq.exponentiation(), self.set_success)


if __name__ == '__main__':
    unittest.main()
