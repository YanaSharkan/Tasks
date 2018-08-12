import sys

class NumberConverter:

  ones = [
    '', 'One', 'Two', 'Three', 'Four', 'Five',
    'Six', 'Seven', 'Eight', 'Nine'
  ]
  teens = [
    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
  ]
  ties = [
    '', '', 'Twenty', 'Thirty', 'Forty',
    'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
  ]

  def convert(self, num, skip_zero = False):
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
    res = self.ones[num]
    if res == '' and skip_zero == False:
      res = 'Zero'
    return res

  def __convert_teens(self, num):
    return self.teens[num - 10]

  def __convert_tens(self, num):
    res = self.ties[num // 10]
    modulus = num % 10
    if modulus != 0:
      res = (res + ' ' + self.convert(modulus, True)).strip()
    return res

  def __convert_hundreds(self, num):
    res = self.ones[num // 100] + ' Hundred'
    modulus = num % 100
    if modulus != 0:
      res = (res + ' ' + self.convert(modulus, True)).strip()
    return res

  def __convert_thousands(self, num):
    res = self.convert(num // 1000) + ' Thousand'
    modulus = num % 1000
    if modulus != 0:
      res = (res + ' ' + self.convert(modulus, True)).strip()
    return res


if __name__ == '__main__':
  number_to_convert = int(sys.argv[1])
  if isinstance(number_to_convert, int):
    if number_to_convert < 1000000:
      converter = NumberConverter()
      print(
        converter.convert(number_to_convert)
      )
    else:
      print('Number should be less then a million')
  else:
    print('You entered a wrong number')
