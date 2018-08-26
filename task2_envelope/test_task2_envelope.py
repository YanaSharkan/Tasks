import unittest
from unittest.mock import patch
import task2_envelope
from params_validation_error import ParamsValidationError


class TestTask2Envelope(unittest.TestCase):

    @patch('task2_envelope.get_input', return_value='1,2')
    def test_define_envelope_success(self, input_mock):
        envelope_model = task2_envelope.define_envelope()
        self.assertEqual(envelope_model.height, 2)
        self.assertEqual(envelope_model.width, 1)

    @patch('task2_envelope.get_input', return_value='1')
    def test_define_envelope_error_args(self, input_mock):
        with self.assertRaises(ParamsValidationError) as thrown:
            task2_envelope.define_envelope()
        self.assertEquals('Not enough arguments specified', str(thrown.exception))

    @patch('task2_envelope.get_input', return_value='b,1')
    def test_define_envelope_error_size1(self, input_mock):
        with self.assertRaises(ParamsValidationError) as thrown:
            task2_envelope.define_envelope()
        self.assertEquals('Argument must be an int greater then 0', str(thrown.exception))

    @patch('task2_envelope.get_input', return_value='1,a')
    def test_define_envelope_error_size2(self, input_mock):
        with self.assertRaises(ParamsValidationError) as thrown:
            task2_envelope.define_envelope()
        self.assertEquals('Argument must be an int greater then 0', str(thrown.exception))

    @patch('task2_envelope.get_input', side_effect=iter(['1,2', '2,3']))
    def test_compare_envelopes(self, input_mock1):
        envelope_model1 = task2_envelope.define_envelope()
        envelope_model2 = task2_envelope.define_envelope()
        self.assertTrue(envelope_model2.compare_envelopes(envelope_model1))

if __name__ == '__main__':
    unittest.main()
