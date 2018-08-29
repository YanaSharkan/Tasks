import unittest
import task3_triangles
from params_validation_error import ParamsValidationError


class TestTask3Triangles(unittest.TestCase):

    data_set_success = ['triangle', '2', '2.5', '2']
    data_set_success1 = ['triangle1', '2', '2', '2.5']
    data_set_error1 = ''
    data_set_error2 = 'triangle1,aa,1,2'
    data_set_error3 = 'tr,5,5,11'

    def test_input_triangle_success(self):
        test_res = []
        task3_triangles.input_triangle(test_res, ','.join(self.data_set_success))
        self.assertEqual(len(test_res), 1)
        self.assertEqual(test_res[0].name, self.data_set_success[0])
        self.assertEqual(test_res[0].length1, float(self.data_set_success[1]))
        self.assertEqual(test_res[0].length2, float(self.data_set_success[2]))
        self.assertEqual(test_res[0].length3, float(self.data_set_success[3]))

    def test_input_triangle_error_params_count(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task3_triangles.input_triangle([], self.data_set_error1)
        self.assertEqual('Not enough arguments specified', str(exception_context.exception))

    def test_input_triangle_error_invalid_length(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task3_triangles.input_triangle([], self.data_set_error2)
        self.assertEqual('Argument must be a float greater then 0', str(exception_context.exception))

    def test_input_triangle_error_invalid_length_side(self):
        with self.assertRaises(ParamsValidationError) as exception_context:
            task3_triangles.input_triangle([], self.data_set_error3)
        self.assertEqual('Sum of two sides of triangle must be greater then the biggest side',
                         str(exception_context.exception))

    def test_is_continue_success_short(self):
        is_continue_res = task3_triangles.is_continue('y')
        self.assertEqual(is_continue_res, True)

    def test_is_continue_success_full(self):
        is_continue_res = task3_triangles.is_continue('yes')
        self.assertEqual(is_continue_res, True)

    def test_is_continue_error(self):
        self.assertEqual(task3_triangles.is_continue('n'), False)

    def test_get_area(self):
        test_res = []
        task3_triangles.input_triangle(test_res, ','.join(self.data_set_success))
        task3_triangles.input_triangle(test_res, ','.join(self.data_set_success1))
        self.assertEqual(test_res[0].get_area(), test_res[1].get_area())
        self.assertNotEqual(test_res[0].length3, test_res[1].length3)


if __name__ == '__main__':
    unittest.main()
