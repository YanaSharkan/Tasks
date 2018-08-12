import sys

class FileScanner:

  def __init__(self, path):
    self.path = path
    self.__file = None

  def search_text(self, text):
    file_text = self.__read_file()
    return len(file_text.split(text)) - 1

  def replace_text(self, text, new_text):
    file_text = self.__read_file()
    new_file_text = file_text.replace(text, new_text)
    self.__write_file(new_file_text)

  def __read_file(self):
    f = self.__open_file()
    res = f.read()
    f.close()
    return res

  def __write_file(self, text):
    f = self.__open_file('w')
    f.write(text)

  def __open_file(self, mode = 'r'):
    return open(self.path, mode)
    

def process_input_params():
  if len(sys.argv) == 3 or len(sys.argv) == 4:
    file_scanner = FileScanner(sys.argv[1])
  
    #try:
    if len(sys.argv) == 4:
      file_scanner.replace_text(sys.argv[2], sys.argv[3])
      print('Text "%s" was replaced by text "%s" in file "%s"' % (sys.argv[2], sys.argv[3], sys.argv[1]))
    else:
      occurences_count = file_scanner.search_text(sys.argv[2])
      print('Number of search matches found: %s' % occurences_count)
    #except IOError as err:
    #  print('Could not open specified file.')
    #  print(err)
  else:
    print('Invalid input prams. Please pass params <filename> <searchstring> (<replacestring>)')

if __name__ == '__main__':
  process_input_params()
