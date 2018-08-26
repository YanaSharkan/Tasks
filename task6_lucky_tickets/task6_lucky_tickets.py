import sys
from abc import ABC, abstractmethod
from os import path

import params_validator
from params_validation_error import ParamsValidationError

ALG_PITER = 'Piter'
ALG_MOSCOW = 'Moscow'


class Ticket(ABC):
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number

    def get_lucky(self):  # Collects lucky tickets between start number and end number
        return [num for num in range(self.start_number, self.end_number) if self.is_lucky(num)]

    @abstractmethod
    def is_lucky(self, ticket_number):  # Method implementation should check if certain method is lucky
        pass


class MoscowTicket(Ticket):

    def is_lucky(self, ticket_number):  # Abstract method implementation from Ticket
        ticket_str = str(ticket_number)
        res = False

        if len(ticket_str) == 6:
            first_sum = int(ticket_str[0]) + int(ticket_str[1]) + int(ticket_str[2])
            second_sum = int(ticket_str[3]) + int(ticket_str[4]) + int(ticket_str[5])
            res = first_sum == second_sum
        return res


class PiterTicket(Ticket):

    def is_lucky(self, ticket_number):  # Abstract method implementation from Ticket
        ticket_str = str(ticket_number)
        even_sum = 0
        odd_sum = 0

        for i in range(len(ticket_str)):
            if i % 2 == 0:
                even_sum = even_sum + int(ticket_str[i])
            else:
                odd_sum = odd_sum + int(ticket_str[i])

        return even_sum == odd_sum


def read_file(file_path):
    with open(file_path, 'r') as context:
        return context.read()


def ticket_factory(calc_type, limitations):  # Compose Ticket implementation by params
    res = None
    params_validator.validate_int_input(limitations[0])
    params_validator.validate_int_input(limitations[1])

    start = int(limitations[0])
    end = int(limitations[1])

    if calc_type == ALG_PITER:
        res = PiterTicket(start, end)
    elif calc_type == ALG_MOSCOW:
        res = MoscowTicket(start, end)
    return res


def main():
    args = sys.argv
    try:
        ticket_method = read_file(args[3])
        tickets_seq = ticket_factory(ticket_method.strip(), args[1:3])
        lucky_tickets = tickets_seq.get_lucky()
        print(lucky_tickets)
    except ParamsValidationError as err:
        print(err)


if __name__ == '__main__':
    main()
