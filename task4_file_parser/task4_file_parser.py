import sys


class FileScanner:
    """Class is working in two modes. There is read mode used for scanning
    file for number of occurrences of string. This is implemented in search text method.
    There is write mode which replaces occurrences in text implemented in replace text method.

    """

    def __init__(self, path):
        self.path = path
        self.f = None

    def search_text(self, text):  # calculates number of matches of text in file contents
        file_text = self.read_file()
        return len(file_text.split(text)) - 1

    def replace_text(self, text, new_text):  # Replaces string with replacement in file contents
        file_text = self.read_file()
        new_file_text = file_text.replace(text, new_text)
        self.write_file(new_file_text)

    def read_file(self):  # Opens file and return contents of file
        self.f = self.open_file()
        res = self.f.read()
        self.close_file()
        return res

    def write_file(self, text):  # Open file and rewrites
        self.f = self.open_file('w')
        self.f.write(text)
        self.close_file()

    def open_file(self, mode='r'):
        return open(self.path, mode)

    def close_file(self):
        if self.f:
            self.f.close()
            self.f = None
    

def process_input_params():
    if sys.argv[1]:
        file_scanner = FileScanner(sys.argv[1])
        try:
            if len(sys.argv) == 4:  # Case of replacing text with new text
                file_scanner.replace_text(sys.argv[2], sys.argv[3])
                print('Text "%s" was replaced by text "%s" in file "%s"' % (sys.argv[2], sys.argv[3], sys.argv[1]))
            elif len(sys.argv) == 3:  # Scanning of the text and calculation number of occurrence
                file_scanner = FileScanner(sys.argv[1])
                occurrences_count = file_scanner.search_text(sys.argv[2])
                print('Number of search matches found: %s' % occurrences_count)
            else:
                print('Invalid input params. Please pass params <filename> <search string> (<replace string>)')
        except IOError as err:  # Read/write exception
            print('Could not open specified file.')
            print(err)
        finally:
            file_scanner.close_file()
    else:
        print('Please specify file name in first param')


if __name__ == '__main__':
    process_input_params()
