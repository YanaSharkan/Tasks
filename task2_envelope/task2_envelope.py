import sys
import params_validator
from params_validation_error import ParamsValidationError

CONTINUE_CONFIRM_SHORT = 'y'
CONTINUE_CONFIRM_FULL = 'yes'


class Envelope:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def compare_envelopes(self, other_env):
        return (self.width > other_env.width and
                self.height > other_env.height) or \
                (self.width > other_env.height and
                    self.height > other_env.width)

    @staticmethod
    def validate(args):
        params_validator.validate_lst(args, 2)
        params_validator.validate_int_input(args[0])
        params_validator.validate_int_input(args[1])


def get_input():
    return str(input('Input envelope params:'))


def define_envelope():
    dimensions_str = get_input()
    dimensions_arr = dimensions_str.split(',')
    Envelope.validate(dimensions_arr)
    return Envelope(dimensions_arr[0], dimensions_arr[1])


def compare_envelopes():
    try:
        first_envelope = define_envelope()
        second_envelope = define_envelope()

        if first_envelope.compare_envelopes(second_envelope):
            print('You can put second envelope into first')
        elif second_envelope.compare_envelopes(first_envelope):
            print('You can put first envelope into second')
        else:
            print('You can not put any envelope into other envelope')
    except ParamsValidationError as err:
        print(err)


def check_continue(continue_cmd):
    return continue_cmd.lower() == CONTINUE_CONFIRM_SHORT \
    or continue_cmd.lower() == CONTINUE_CONFIRM_FULL


if __name__ == '__main__':
    while True:
        compare_envelopes()
        continue_command = input('Do you want to continue? yes / no: ')
        if not check_continue(continue_command):
            break
