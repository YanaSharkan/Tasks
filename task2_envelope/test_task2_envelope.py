import unittest
import task2_envelope
from params_validation_error import ParamsValidationError


class TestTask2Envelope(unittest.TestCase):

    params_success = '1,2'
    params_success1 = '2,3'
    params_error_args = '1'
    params_error_num1 = 'b,1'
    params_error_num2 = '1,a'

    def test_define_envelope_success(self):
        envelope_model = task2_envelope.define_envelope(self.params_success)
        self.assertEqual(envelope_model.height, 2)
        self.assertEqual(envelope_model.width, 1)

    def test_define_envelope_error_args(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task2_envelope.define_envelope(self.params_error_args)
        self.assertEqual('Not enough arguments specified', str(exception_context.exception))

    def test_define_envelope_error_size1(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task2_envelope.define_envelope(self.params_error_num1)
        self.assertEqual('Argument must be an int greater then 0', str(exception_context.exception))

    def test_define_envelope_error_size2(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task2_envelope.define_envelope(self.params_error_num2)
        self.assertEqual('Argument must be an int greater then 0', str(exception_context.exception))

    def test_compare_envelopes(self):
        envelope_model1 = task2_envelope.define_envelope(self.params_success)
        envelope_model2 = task2_envelope.define_envelope(self.params_success1)
        self.assertTrue(envelope_model2.compare_envelopes(envelope_model1))


if __name__ == '__main__':
    unittest.main()
