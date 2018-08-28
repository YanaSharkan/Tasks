import sys
import numbers


class NumberConverter:
    def convert(self, num, skip_zero=False):
        res = ''
        if num < 10:
            res = self.__convert_ones(num, skip_zero)
        elif num < 20:
            res = self.__convert_teens(num)
        elif num < 100:
            res = self.__convert_tens(num)
        elif num < 1000:
            res = self.__convert_hundreds(num)
        elif num < 1000000:
            res = self.__convert_thousands(num)
        return res

    def __convert_ones(self, num, skip_zero):
        res = numbers.ones[num]
        if res == '' and skip_zero == False:
            res = 'Zero'
        return res

    def __convert_teens(self, num):
        return numbers.teens[num - 10]

    def __convert_tens(self, num):
        res = numbers.ties[num // 10]
        modulus = num % 10
        if modulus != 0:
            res = (res + ' ' + self.convert(modulus, True)).strip()
        return res

    def __convert_hundreds(self, num):
        res = numbers.ones[num // 100] + ' HUNDRED'
        modulus = num % 100
        if modulus != 0:
            res = (res + ' ' + self.convert(modulus, True)).strip()
        return res

    def __convert_thousands(self, num):
        res = self.convert(num // 1000) + ' THOUSAND'
        modulus = num % 1000
        if modulus != 0:
            res = (res + ' ' + self.convert(modulus, True)).strip()
        return res


if __name__ == '__main__':
    number_to_convert = int(sys.argv[1])
    if isinstance(number_to_convert, int):
        if number_to_convert < 1000000:
            converter = NumberConverter()
            print(converter.convert(number_to_convert))
        else:
            print('Number should be less then a million')
    else:
        print('You entered a wrong number')
