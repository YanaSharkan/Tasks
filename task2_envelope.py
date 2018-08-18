class Envelope:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compare_envelopes(self, other_env):
        return (self.width > other_env.width and self.height > other_env.height) or \
               (self.width > other_env.height and self.height > other_env.width)


def main():
    print('Input envelope sizes: ')
    a = float(input('First envelope width = '))
    b = float(input('First envelope height = '))
    c = float(input('Second envelope width = '))
    d = float(input('Second envelope height = '))

    first_envelope = Envelope(a, b)
    second_envelope = Envelope(c, d)

    if first_envelope.compare_envelopes(second_envelope):
        print('You can input second envelope into first')
    else:
        print('You can NOT input second envelope into first ')

    continue_command = input('Do you want to continue? yes / no: ')
    if continue_command.lower() == 'y' or continue_command.lower() == 'yes':
        main()
    else:
        exit()


if __name__ == '__main__':
    main()
