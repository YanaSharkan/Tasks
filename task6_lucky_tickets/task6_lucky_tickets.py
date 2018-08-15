import sys


class Ticket:
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number

    def get_lucky(self, method):
        res = []

        for i in range(self.start_number, self.end_number):
            if method == 'Moscow' and self.__is_lucky_moscow(i):
                res.append(i)
            elif method == 'Piter' and self.__is_lucky_piter(i):
                res.append(i)

        return res

    def __is_lucky_moscow(self, ticket_number):
        ticket_str = str(ticket_number)
        return len(ticket_str) == 6 and \
               int(ticket_str[0]) + int(ticket_str[1]) + int(ticket_str[2]) == int(ticket_str[3]) + int(
            ticket_str[4]) + int(ticket_str[5])

    def __is_lucky_piter(self, ticket_number):
        ticket_str = str(ticket_number)
        even_sum = 0
        odd_sum = 0

        for i in range(0, len(ticket_str)):
            if i % 2 == 0:
                even_sum = even_sum + int(ticket_str[i])
            else:
                odd_sum = odd_sum + int(ticket_str[i])

        return even_sum == odd_sum


def read_file(path):
    file_content = open(path, 'r')
    return file_content.read()


def main():
    args = sys.argv
    start = int(args[1])
    end = int(args[2])
    ticket_method = read_file(args[3])

    tickets_seq = Ticket(start, end)
    lucky_tickets = tickets_seq.get_lucky(ticket_method.strip())

    print(lucky_tickets)


if __name__ == '__main__':
    main()