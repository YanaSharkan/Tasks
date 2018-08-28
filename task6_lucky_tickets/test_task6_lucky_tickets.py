import unittest
from unittest.mock import patch
import task6_lucky_tickets
from params_validation_error import ParamsValidationError


class TestLuckyTickets(unittest.TestCase):

    ticket_args_success = ['100000', '110000']
    ticket_args_error = ['110000', 'aa']
    lucky_ticket_moscow_success = 100100
    lucky_ticket_moscow_error = 1000050
    lucky_ticket_piter_success = 100034
    lucky_ticket_piter_error = 100033

    def test_ticket_factory_success(self):
        ticket_inst1 = task6_lucky_tickets.ticket_factory(task6_lucky_tickets.ALG_MOSCOW, self.ticket_args_success)
        self.assertTrue(isinstance(ticket_inst1, task6_lucky_tickets.MoscowTicket), True)
        ticket_inst2 = task6_lucky_tickets.ticket_factory(task6_lucky_tickets.ALG_PITER, self.ticket_args_success)
        self.assertTrue(isinstance(ticket_inst2, task6_lucky_tickets.PiterTicket), True)
        self.assertEquals(ticket_inst1.start_number, int(self.ticket_args_success[0]))
        self.assertEquals(ticket_inst1.end_number, int(self.ticket_args_success[1]))

    def test_ticket_factory_error(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task6_lucky_tickets.ticket_factory(task6_lucky_tickets.ALG_MOSCOW, self.ticket_args_error)
        self.assertEqual('Argument must be an int greater then 0', str(exception_context.exception))

    def test_is_lucky_moscow(self):
        ticket_inst1 = task6_lucky_tickets.MoscowTicket(self.ticket_args_success[0], self.ticket_args_success[1])
        self.assertTrue(ticket_inst1.is_lucky(self.lucky_ticket_moscow_success))
        self.assertFalse(ticket_inst1.is_lucky(self.lucky_ticket_moscow_error))

    def test_is_lucky_piter(self):
        ticket_inst1 = task6_lucky_tickets.PiterTicket(self.ticket_args_success[0], self.ticket_args_success[1])
        self.assertTrue(ticket_inst1.is_lucky(self.lucky_ticket_piter_success))
        self.assertFalse(ticket_inst1.is_lucky(self.lucky_ticket_piter_error))


if __name__ == '__main__':
    unittest.main()
