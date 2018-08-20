import sys
from abc import ABC, abstractmethod
from os import path

tasks_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(path.join(tasks_path, 'validator'))
import params_validator
from params_validation_error import ParamsValidationError

class Ticket(ABC):
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number

    def get_lucky(self):
        res = []

        for i in range(self.start_number, self.end_number):
            if self.is_lucky(i):
                res.append(i)

        return res

    @staticmethod
    def validate(args):
        params_validator.validate_int_input(args[1])
        params_validator.validate_int_input(args[2])

    @abstractmethod
    def is_lucky(self, ticket_number):
        pass


class MoscowTicket(Ticket):

    def __init__(self, start_number, end_number):
        super().__init__(start_number, end_number)

    def is_lucky(self, ticket_number):
        ticket_str = str(ticket_number)
        res = False

        if len(ticket_str) == 6:
            first_sum = int(ticket_str[0]) + int(ticket_str[1]) + int(ticket_str[2])
            second_sum = int(ticket_str[3]) + int(ticket_str[4]) + int(ticket_str[5])
            res = first_sum == second_sum
        return res


class PiterTicket(Ticket):

    def __init__(self, start_number, end_number):
        super().__init__(start_number, end_number)

    def is_lucky(self, ticket_number):
        ticket_str = str(ticket_number)
        even_sum = 0
        odd_sum = 0

        for i in range(0, len(ticket_str)):
            if i % 2 == 0:
                even_sum = even_sum + int(ticket_str[i])
            else:
                odd_sum = odd_sum + int(ticket_str[i])

        return even_sum == odd_sum


def read_file(file_path):
    file_content = open(file_path, 'r')
    return file_content.read()


def ticket_factory(calc_type, start, end):
    res = None
    if calc_type == 'Piter':
        res = PiterTicket(start, end)
    elif calc_type == 'Moscow':
        res = MoscowTicket(start, end)
    return res


def main():
    args = sys.argv
    try:
        Ticket.validate(args)
        start = int(args[1])
        end = int(args[2])
        ticket_method = read_file(args[3])
        tickets_seq = ticket_factory(ticket_method.strip(), start, end)
        lucky_tickets = tickets_seq.get_lucky()
        print(lucky_tickets)
    except ParamsValidationError as err:
        print(err)


if __name__ == '__main__':
    main()
